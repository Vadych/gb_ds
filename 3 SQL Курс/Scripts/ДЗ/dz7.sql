USE shop;

/* 
*
* ЗАДАЧА 1
* 
* Составьте список пользователей users, 
* которые осуществили хотя бы один заказ orders в интернет магазине.
* 
*/

-- Создаем данные для теста
INSERT INTO orders 
(user_id, created_at)
VALUES (1, '2020-4-15'), (3, '2022-8-12'), (1, now()), (5,'2021-7-21');


-- Немного усложнил вывод, надеюсь не будет ошибкой.
-- А то очень легко и скучно

SELECT u.id, u.name, COUNT(o.id) AS 'Count'  
FROM users u
JOIN orders o
ON user_id = u.id
GROUP BY user_id 
ORDER BY 'Count' DESC;


/* 
*
* ЗАДАЧА 2
* 
* Выведите список товаров products и разделов catalogs, 
* который соответствует товару
* 
*/

-- Немного продуктов без каталога
INSERT INTO products
(name, description, price, catalog_id)
VALUES
	('USB SSD', 'Диск из каталога 0', 10000, 0), 
	('USB HDD', 'Диск из каталога Null', 10000, NULL);

-- Интерпритировал задачу как ВСЕ продукты

SELECT p.id, p.name, p.description, p.price, c.name  
FROM products p 
LEFT JOIN catalogs c 
ON p.catalog_id = c.id ;

/* 
*
* ЗАДАЧА 3
* 
* Пусть имеется таблица рейсов flights (id, from, to) 
* и таблица городов cities (label, name). 
* Поля from, to и label содержат английские названия городов, поле name — русское. 
* Выведите список рейсов flights с русскими названиями городов.
* 
*/

-- Готовим таблицы и заполняем данными
DROP TABLE IF EXISTS flights;
CREATE TABLE flights(
	id bigint PRIMARY KEY,
	`from` varchar(100),
	 `to` varchar(100)
);
INSERT INTO flights
(id, `from`, `to`)
VALUES
	(1, 'moscow', 'omsk'), 
	(2, 'novgorod', 'kazan'), 
	(3, 'irkutsk', 'moscow'), 
	(4, 'omsk', 'irkutsk'), 
	(5, 'moscow', 'kazan'),
	(6, 'novgorod', 'sochi'), -- добавил две строки с отсутсвующими значениями в cities
	(7, 'sochi', 'moscow');


DROP TABLE IF EXISTS cities;
CREATE TABLE cities(
	label varchar(100) PRIMARY KEY,
	name varchar(100)
);
INSERT INTO cities
(label, name)
VALUES
	('moscow', 'Москва'), 
	('irkutsk', 'Иркутск'), 
	('novgorod', 'Новгород'), 
	('kazan', 'Казань'), 
	('omsk', 'Омск');

-- Сам запрос
SELECT 
	f.id,
	IF (ISNULL(c.name), f.`from`, c.name) AS 'Из',
	IF (ISNULL(c2.name), f.`to`, c2.name) AS 'В'
FROM flights f 
LEFT JOIN cities c 
ON f.`from` = c.label 
LEFT JOIN cities c2 
ON f.`to` = c2.label















