/* 
 * Создание процедур, функций, тригеров и видов
 * 
 */
USE money;
DELIMITER $$


/* 
 * Процедуры и функции
 * 
 */


-- Функция возвращает курс на дату
DROP FUNCTION IF EXISTS course_to_data$$
CREATE FUNCTION course_to_data(cur int, dt date)
RETURNS decimal(8,4) READS SQL DATA 
BEGIN
	DECLARE crs decimal(8,4);
	SELECT course 
		FROM currencies_courses cc 
		WHERE cc.date_course = (
			SELECT max(cc2.date_course)
			FROM currencies_courses cc2
			WHERE cc2.date_course <= dt  AND cc2.currency_id = cur
			) AND cc.currency_id = cur
	INTO crs;
	RETURN crs;
END $$


-- Функция возвращает курс валюты1 к валюте2
DROP FUNCTION IF EXISTS exchange_to_data $$
CREATE FUNCTION exchange_to_data(cur1 int, cur2 int, dt date)
RETURNS decimal(8,4) DETERMINISTIC 
BEGIN
	RETURN course_to_data(cur1, dt) / course_to_data(cur2, dt);
END $$

DROP PROCEDURE IF EXISTS add_transacion $$
CREATE PROCEDURE add_transacion(from_id int, to_id int, cat int, sum_credit decimal(12,2),
								sum_debit decimal(12,2), date_tr date, comment varchar(255))
BEGIN
	START TRANSACTION;
	INSERT INTO transactions
	(from_id, to_id, category_id, sum_credit, sum_debit, date_transactiont, comment)
	VALUES(from_id , to_id , cat , sum_debit , sum_credit , date_tr, comment);
	IF from_id IS NOT NULL THEN
		UPDATE accounts 
		SET balance = balance - sum_credit
		WHERE id = from_id;
	END IF;
	IF to_id IS NOT NULL THEN
		UPDATE accounts 
		SET balance = balance + sum_debit
		WHERE id = to_id;
	END IF;
	COMMIT;
END $$

-- Тестирование процеуры и функции. При необходимости убрать

-- Тестирование двух функций. 
SELECT course_to_data(3, '2021-10-09') $$
SELECT exchange_to_data(2, 3, '2021-10-09') $$

-- Добавление записи в таблицу транзакций
SELECT id, balance 
FROM accounts a 
WHERE id = 1 OR id = 2 $$

CALL add_transacion(1, 2, 1, 2000, 3000, now(), 'Тест add_transacion') $$
SELECT * 
FROM transactions 
WHERE id = LAST_INSERT_ID() $$

SELECT id, balance 
FROM accounts a 
WHERE id = 1 OR id = 2 $$
-- Конец теста

/* 
 * Тригеры
 * 
 */

-- Сложно было придумывать. В этой теме тригеры не к месту, мне кажется


-- добавление профиля при вставке пользователя
DROP TRIGGER IF EXISTS users_insert $$
CREATE TRIGGER users_insert
AFTER INSERT
ON users FOR EACH ROW
BEGIN 
	INSERT INTO user_profiles
	(user_id)
	VALUES(NEW.id);
END $$

-- Если не задана родительская категория, то добавляет сама себя
DROP TRIGGER IF EXISTS categories_insert $$
CREATE  TRIGGER categories_insert
BEFORE INSERT
ON categories FOR EACH ROW
BEGIN
	DECLARE new_id bigint;
	IF NEW.parrent_id IS NULL THEN 
		SELECT `auto_increment` 
		FROM INFORMATION_SCHEMA.TABLES
	    WHERE TABLE_NAME='categories' AND TABLE_SCHEMA=DATABASE()
	   	INTO new_id;
	SET NEW.parrent_id = new_id;
	END IF;
END $$

-- Тестирование тригерров. При необходимости удалить
INSERT INTO users
(firstname, lastname, email, phone, password_hash)
VALUES('Тест', 'Тригера', concat('почта', now()), 123456678, 'crejfjerfjerffrn')$$

SELECT *
FROM users u 
JOIN user_profiles up 
ON u.id = up.user_id 
WHERE u.id = LAST_INSERT_ID()$$

INSERT INTO categories
(name, is_expenses, is_income)
VALUES('Тест триггера', 1, 1)$$

SELECT *
FROM categories 
WHERE id = LAST_INSERT_ID()$$
-- Конец тестирования
DELIMITER ;

/*
 * Представления
 */


-- Все счета пользователя. Свои + доступные
CREATE OR REPLACE VIEW user_accounts AS
SELECT a.owner_id, a.id AS account_id 
FROM accounts a 
UNION
SELECT p.user_id, p.account_id 
FROM permitions p 
JOIN accounts a2 ON a2.id = p.account_id 
WHERE a2.is_private != b'0';


-- Остатки по счетам
CREATE OR REPLACE VIEW accounts_balanse AS
SELECT a.id, a.owner_id, a.bank_id, a.balance, a.currency_id 
FROM user_accounts ua 
JOIN accounts a ON ua.account_id = a.id 
WHERE a.is_archive = b'0';

-- Расходы по категориям
CREATE OR REPLACE VIEW categories_credit AS
SELECT t.id, ua.owner_id, t.category_id, t.sum_credit
FROM transactions t
JOIN user_accounts ua ON ua.account_id = t.from_id 
	AND NOT t.category_id <=> NULL; -- Исключаем транзакции с одного счета на другой



-- Доходы по категориям
CREATE OR REPLACE VIEW categories_debit AS
SELECT t.id, ua.owner_id, t.category_id, t.sum_debit 
FROM transactions t
JOIN user_accounts ua ON ua.account_id = t.to_id AND NOT t.category_id <=> NULL;



