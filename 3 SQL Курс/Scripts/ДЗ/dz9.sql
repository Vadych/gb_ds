
USE shop;
/****************************************
* 										*
* Транзакции, переменные, представления *
* 										*
****************************************/

/* 
 * Задача 1
 * 
 * В базе данных shop и sample присутствуют одни и те же таблицы, учебной базы данных. 
 * Переместите запись id = 1 из таблицы shop.users в таблицу sample.users. 
 * Используйте транзакции.
 *
 */

START TRANSACTION;

DELETE FROM sample.users 
WHERE sample.users.id = 1;

INSERT INTO sample.users 
(id, name, birthday_at, created_at, updated_at)
SELECT id, name, birthday_at, created_at, updated_at
FROM shop.users 
WHERE shop.users.id = 1;

DELETE FROM shop.users 
WHERE shop.users.id = 1;

COMMIT;

/* 
 * Задача 2
 * 
 * Создайте представление, 
 * которое выводит название name товарной позиции из таблицы products 
 * и соответствующее название каталога name из таблицы catalogs.
 *
 */

DROP VIEW IF EXISTS products_catalog;
CREATE VIEW products_catalog AS
	SELECT p.name AS prod_name, c.name AS cat_name  FROM products p 
	LEFT JOIN catalogs c ON p.catalog_id = c.id 
	ORDER BY cat_name, prod_name;

SELECT * FROM products_catalog;


/* 
 * Задача 3
 * 
 * Пусть имеется таблица с календарным полем created_at. 
 * В ней размещены разряженые календарные записи за август 2018 года
 * '2018-08-01', '2018-08-04', '2018-08-16' и 2018-08-17. 
 * Составьте запрос, который выводит полный список дат за август, 
 * выставляя в соседнем поле значение 1, если дата присутствует в исходном таблице и 0, 
 * если она отсутствует.
 *
 */

WITH RECURSIVE dates as (
SELECT '2018-08-01' as dday
UNION ALL
SELECT DATE_ADD(dday, INTERVAL 1 DAY) AS dday FROM dates
WHERE dday < '2018-08-31')
SELECT 
	d.dday,
	IF (COUNT(o.created_at) > 1, 1, COUNT(o.created_at)) AS flag
FROM dates d
LEFT JOIN orders o 
ON DATE(o.created_at) = d.dday
GROUP BY d.dday
ORDER BY d.dday;


/* 
 * Задача 4
 * 
 * Пусть имеется любая таблица с календарным полем created_at. 
 * Создайте запрос, который удаляет устаревшие записи из таблицы, 
 * оставляя только 5 самых свежих записей.
 *
 */

-- Задача оказалось сложне, чем показалось на первый взгляд

DROP VIEW IF EXISTS firs_5;
CREATE VIEW firs_5 AS SELECT id FROM orders ORDER BY created_at DESC LIMIT 5;

DELETE FROM orders 
WHERE id NOT IN (SELECT * FROM firs_5);


/**************************
*    					  *
* Администрирование MySQL *
* 		 				  *
***************************/

/* 
 * Задача 1
 * 
 * Создайте двух пользователей которые имеют доступ к базе данных shop. 
 * Первому пользователю shop_read должны быть доступны только запросы на чтение данных, 
 * второму пользователю shop — любые операции в пределах базы данных shop.
 *
 */

DROP USER IF EXISTS 'shop_read'@'localhost';
CREATE USER 'shop_read'@'localhost' IDENTIFIED BY '123';
GRANT SELECT ON shop.* TO 'shop_read'@'localhost';

DROP USER IF EXISTS 'shop'@'localhost';
CREATE USER 'shop'@'localhost' IDENTIFIED BY '123';
GRANT ALL ON shop.* TO 'shop'@'localhost';


/* 
 * Задача 2
 * 
 * Пусть имеется таблица accounts содержащая три столбца id, name, password,
 * содержащие первичный ключ, имя пользователя и его пароль. 
 * Создайте представление username таблицы accounts, 
 * предоставляющий доступ к столбца id и name. 
 * Создайте пользователя user_read, который бы не имел доступа к таблице accounts, 
 * однако, мог бы извлекать записи из представления username.
 *
 */

DROP VIEW IF EXISTS username;
CREATE VIEW username AS SELECT id, name FROM accounts;

DROP USER IF EXISTS 'user_read'@'localhost';
CREATE USER 'user_read'@'localhost' IDENTIFIED BY '123';
GRANT SELECT ON shop.username TO 'user_read'@'localhost';


/*****************************************
*    							 	     *
* Хранимые процедуры и функции, триггеры *
* 		 				                 *
*****************************************/

/* 
 * Задача 1
 * 
 * Создайте хранимую функцию hello(), которая будет возвращать приветствие,
 * в зависимости от текущего времени суток. 
 * С 6:00 до 12:00 функция должна возвращать фразу "Доброе утро", 
 * с 12:00 до 18:00 функция должна возвращать фразу "Добрый день", 
 * с 18:00 до 00:00 — "Добрый вечер", 
 * с 00:00 до 6:00 — "Доброй ночи".
 *
 */

DELIMITER $$ -- Иначе скрипт не выполнялся целиком

DROP FUNCTION IF EXISTS hello $$
CREATE FUNCTION hello() 
RETURNS VARCHAR(20) DETERMINISTIC 
BEGIN
	DECLARE cur_hour int DEFAULT HOUR(CURTIME());
	IF cur_hour < 6 THEN RETURN 'Доброй ночи';
	ELSEIF cur_hour < 12 THEN RETURN 'Доброе утро';
	ELSEIF cur_hour < 18 THEN RETURN 'Добрый день';
	ELSE RETURN 'Добрый вечер';
	END IF;
END$$

SELECT hello()$$


/* 
 * Задача 2
 * 
 * В таблице products есть два текстовых поля: 
 * name с названием товара и description с его описанием. 
 * Допустимо присутствие обоих полей или одно из них. 
 * Ситуация, когда оба поля принимают неопределенное значение NULL неприемлема. 
 * Используя триггеры, добейтесь того, чтобы одно из этих полей или оба поля были заполнены. 
 * При попытке присвоить полям NULL-значение необходимо отменить операцию.
 *
 */

DROP TRIGGER IF EXISTS insert_products $$
CREATE TRIGGER insert_products BEFORE INSERT ON products 
FOR EACH ROW
BEGIN
	IF NEW.name IS NULL AND NEW.description IS NULL THEN 
		SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'INSERT canceled';
	END IF;
END$$

DROP TRIGGER IF EXISTS update_products $$
CREATE TRIGGER update_products BEFORE UPDATE ON products 
FOR EACH ROW
BEGIN
	IF NEW.name IS NULL AND NEW.description IS NULL THEN 
		SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'UPDATE canceled';
	END IF;
END$$

INSERT INTO products
(name, description, price, catalog_id)
VALUES
	('Тест 1', NULL ,100 , 2),
	( NULL ,'Тест 2', 100 , 2),
-- 	(NULL, NULL ,100 , 2), Если оставить эту строчку, то отменяется вся пакетная вставка
-- Как добиться того, что бы вставлялись 3 строки, а одна нет, я не нашел.
-- Теоретически можно попробовать через AFTER удалять неправильные строки	
	('Тест 3', 'Тест 4' ,100 , 2)$$

-- Тут запланированы ошибки
INSERT INTO products
(name, description, price, catalog_id)
VALUES (NULL, NULL ,100 , 2)$$

UPDATE products 
SET 
	name = NULL,
	description = NULL 
WHERE id = 1$$
	

/* 
 * Задача 3
 * 
 * Напишите хранимую функцию для вычисления произвольного числа Фибоначчи. 
 * Числами Фибоначчи называется последовательность в которой 
 * число равно сумме двух предыдущих чисел. 
 * Вызов функции FIBONACCI(10) должен возвращать число 55.
 *
 */


DROP FUNCTION IF EXISTS fibonacci$$
CREATE FUNCTION fibonacci(n int) 
RETURNS bigint DETERMINISTIC 
BEGIN
	DECLARE a bigint DEFAULT 0;
	DECLARE b bigint DEFAULT 1;
	WHILE n > 0 DO
		-- можно как-то заставить select сначала посчитать все, а потом присвоить переменным?
		SELECT a+b, b-a, n-1 INTO b, a, n;
	END WHILE;
	RETURN a;
END$$

SELECT 
	fibonacci(0), 
	fibonacci(1),
	fibonacci(10),
	fibonacci(60)$$

DELIMITER ;







