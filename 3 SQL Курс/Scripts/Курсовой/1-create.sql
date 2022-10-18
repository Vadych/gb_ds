/*
 * ОПИСАНИЕ БД
 * 
 * Хранение и учет расходов и доходов.
 * Поддерживает использование нескольких валют
 * Поддерживает использование нескольких счетов разных типов
 * Поддерживает совместное ведение счетов
 * 
 */

/*
 * Создание таблиц, индексов и т.д.
 * 
 */

DROP DATABASE IF EXISTS money;
CREATE DATABASE money;
USE money;


-- Таблица пользователей
DROP TABLE IF EXISTS users;
CREATE TABLE users (
	id SERIAL PRIMARY KEY,
    firstname VARCHAR(50),
    lastname VARCHAR(50),
    email VARCHAR(120) UNIQUE,
    phone BIGINT UNIQUE,
    password_hash varchar(100)
);


-- Профиль пользователя.
-- Содержит различную дополнительную информацию о пользователе
DROP TABLE IF EXISTS user_profiles;
CREATE TABLE user_profiles (
	user_id SERIAL PRIMARY KEY,
    gender CHAR(1),
    birthday DATE,
    created_at DATETIME DEFAULT NOW(),
    FOREIGN KEY (user_id) REFERENCES users(id)  ON UPDATE CASCADE ON DELETE CASCADE
);


-- Таблица банков
DROP TABLE IF EXISTS banks;
CREATE TABLE banks (
	id SERIAL PRIMARY KEY,
	name VARCHAR(255),
	BIK BIGINT,
	message_template TEXT -- Шаблон для парсинга сообщения из банка
);


-- Типы счетов
DROP TABLE IF EXISTS account_types;
CREATE TABLE account_types(
	id SERIAL PRIMARY KEY,
	name VARCHAR(255)
);

-- Список валют
DROP TABLE IF EXISTS currencies;
CREATE TABLE currencies (
	id SERIAL PRIMARY KEY,
	short_name CHAR(3), -- Индентификатор на бирже
	name VARCHAR(100)
);


-- Курсы валют
DROP TABLE IF EXISTS currency_courses;
CREATE TABLE currencies_courses (
	currency_id BIGINT UNSIGNED,
	course DECIMAL(8,4), -- Рублей за еденицу
	date_course DATE DEFAULT (CURRENT_DATE),
	PRIMARY KEY (currency_id, date_course),
	FOREIGN KEY (currency_id) REFERENCES currencies(id) ON UPDATE CASCADE ON DELETE CASCADE
);


-- Таблица счетов
DROP TABLE IF EXISTS accounts;
CREATE TABLE accounts(
	id SERIAL PRIMARY KEY,
	owner_id BIGINT UNSIGNED, -- владелец счета
	name VARCHAR(200), -- Название счета
	bank_id BIGINT UNSIGNED, -- Банк, где открыт. NULL - наличные
	account_type_id BIGINT UNSIGNED, -- Тип счета
	currency_id BIGINT UNSIGNED,
	balance DECIMAL(12, 2), -- Баланс счета. Милиардеры в пролете
	start_balance DECIMAL(12, 2) DEFAULT 0, -- Начальный баланс на момент заведения счета
	is_private BOOLEAN DEFAULT b'0', -- Если счет доступен только владельцу
	is_archive BOOLEAN DEFAULT b'0', -- Если счет в архиве
	FOREIGN KEY (owner_id) REFERENCES users(id) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY (bank_id) REFERENCES banks(id) ON UPDATE CASCADE ON DELETE RESTRICT,
	FOREIGN KEY (currency_id) REFERENCES currencies(id) ON UPDATE CASCADE ON DELETE RESTRICT,	
	FOREIGN KEY (account_type_id) REFERENCES account_types(id)  ON UPDATE CASCADE ON DELETE RESTRICT
);


-- Таблица доступа к счету другим пользователям
DROP TABLE IF EXISTS permitions;
CREATE TABLE permitions(
	account_id BIGINT UNSIGNED, -- счет к которому дают доступ
	user_id BIGINT UNSIGNED, -- кому дают доступ
	PRIMARY KEY (account_id, user_id),
	FOREIGN KEY (account_id) REFERENCES accounts(id) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY (user_id) REFERENCES users(id) ON UPDATE CASCADE ON DELETE CASCADE
);


-- Категории операций
DROP TABLE IF EXISTS categories;
CREATE TABLE categories(
	id SERIAL PRIMARY KEY,
	name VARCHAR(100),
	is_expenses BOOLEAN DEFAULT b'1', -- Может быть расходом
	is_income BOOLEAN DEFAULT b'1', -- Может быть доходом
	parrent_id BIGINT UNSIGNED, -- ссылка на родительскую категорию
	FOREIGN KEY (parrent_id) REFERENCES categories(id) ON UPDATE CASCADE ON DELETE CASCADE
);


-- Таблица проводок
DROP TABLE IF EXISTS transactions;
CREATE TABLE transactions(
	id SERIAL PRIMARY KEY,
	from_id BIGINT UNSIGNED, -- с какого счета. NULL - доход
	to_id BIGINT UNSIGNED, -- на какой счет. NULL - расход
	category_id BIGINT UNSIGNED, -- категория. NULL - перевод
	sum_credit DECIMAL(12, 2), -- сумма списания
	sum_debit DECIMAL(12, 2), -- сумма зачисления
	date_transactiont DATETIME DEFAULT NOW(), -- дата и время транзакции
	comment VARCHAR(255), -- комментарий к транзакции
	FOREIGN KEY (from_id) REFERENCES accounts(id) ON UPDATE CASCADE ON DELETE RESTRICT,
	FOREIGN KEY (to_id) REFERENCES accounts(id) ON UPDATE CASCADE ON DELETE RESTRICT,
	FOREIGN KEY (category_id) REFERENCES categories(id) ON UPDATE CASCADE ON DELETE RESTRICT
);
