USE shop;

/*
 * ЗАДАЧА 1
 * 
 * Создайте таблицу logs типа Archive. 
 * Пусть при каждом создании записи в таблицах users, catalogs и products 
 * в таблицу logs помещается время и дата создания записи, название таблицы, 
 * идентификатор первичного ключа и содержимое поля name.
 */


DROP TABLE IF EXISTS logs;

-- В лекции по это ничего не было, но как я понял 
-- в архивной таблице не можед быть первичного ключа

CREATE TABLE logs (
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	table_name varchar(100) NOT NULL,
	object_id BIGINT UNSIGNED NOT NULL,
	name varchar(255)
)
ENGINE=ARCHIVE
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_0900_ai_ci;


DELIMITER $$

DROP TRIGGER IF EXISTS users_after_insert $$
CREATE TRIGGER users_after_insert
AFTER INSERT
ON users FOR EACH ROW
	INSERT INTO logs
	SET
		table_name = 'users',
		name = NEW.name,
		object_id = NEW.id $$
	
DROP TRIGGER IF EXISTS catalogs_after_insert $$
CREATE TRIGGER catalogs_after_insert
AFTER INSERT
ON catalogs FOR EACH ROW
	INSERT INTO logs
	SET
		table_name = 'catalogs',
		name = NEW.name,
		object_id = NEW.id $$
	
DROP TRIGGER IF EXISTS products_after_insert $$
CREATE TRIGGER products_after_insert
AFTER INSERT
ON products FOR EACH ROW
	INSERT INTO logs
	SET
		table_name = 'products',
		name = NEW.name,
		object_id = NEW.id $$
DELIMITER ;

/*
 * ЗАДАЧА 2
 * 
 * Создайте SQL-запрос, который помещает в таблицу users миллион записей.
 * 
 */

SELECT COUNT(*) AS cnt_users_before FROM users;
SELECT COUNT(*) AS cnt_logs_before FROM logs;

INSERT INTO users (name)

WITH RECURSIVE numbers as (
SELECT 0 as num
UNION ALL
SELECT num + 1 AS num FROM numbers
WHERE num < 99)

SELECT 
	CONCAT('user', n1.num * 100 + n2.num * 10000 + n3.num) AS name
FROM numbers n1
JOIN numbers n2
JOIN numbers n3;

SELECT COUNT(*) AS cnt_users_after FROM users;
SELECT COUNT(*) AS cnt_logs_after FROM logs;












