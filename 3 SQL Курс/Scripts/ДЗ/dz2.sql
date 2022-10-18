/*
 * ЗАДАЧА 1
 * Установите СУБД MySQL. Создайте в домашней директории файл .my.cnf, 
 * задав в нем логин и пароль, который указывался при установке.
 */

/*
 * Созданный файл
 * 
 *[client]
 *user=root
 *password=Vadim_SQL
 */

/*
 * ЗАДАЧА 2
 * Создайте базу данных example, 
 * разместите в ней таблицу users, 
 * состоящую из двух столбцов, числового id и строкового name.
 */

DROP DATABASE IF EXISTS example;
CREATE DATABASE example;

USE example;

DROP TABLE IF EXISTS users;

CREATE TABLE users (
	id INT,
	name VARCHAR(255)
);

/*
 * ЗАДАЧА 3
 * Создайте дамп базы данных example из предыдущего задания, 
 * разверните содержимое дампа в новую базу данных sample.
 */

-- В терминале выполняем команду
-- mysqldump example > example_dump.sql

DROP DATABASE IF EXISTS sample;
CREATE DATABASE sample;

-- В терминале выполняем команду
-- mysql sample < example_dump.sql

/*
* ЗАДАЧА 4
* Ознакомьтесь более подробно с документацией утилиты mysqldump. 
* Создайте дамп единственной таблицы help_keyword базы данных mysql. 
* Причем добейтесь того, чтобы дамп содержал только первые 100 строк таблицы.
*/

-- В терминале выполняем команду
-- mysqldump --where='TRUE LIMIT 100' mysql help_keyword > help_keyword_dump.sql

/*
 * ПРИМЕЧАНИЕ
 * 
 * В командах в заданиях 3 и 4 не вводились параметры пользователя,
 * т.к. в задании 1 создан файл .my.cnf
 */


