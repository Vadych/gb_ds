USE money;
/*
 * Запросы 
 * 
 */

-- Остатки по счетам
-- Выводит все счета с суммой остатка в валюте счета и в рублях

SELECT 
	CONCAT(u.firstname, ' ', u.lastname) AS 'Полное имя',
	a.name AS 'Счет',
	ab.balance AS 'Баланс',
	c.short_name AS 'Валюта',
	ROUND(course_to_data(ab.currency_id, CURDATE()) * a.balance, 2) AS 'Баланс в рублях'
FROM 
	accounts_balanse ab  
JOIN
	accounts a ON a.id = ab.id 
JOIN 
	users u ON ab.owner_id = u.id 
LEFT JOIN 
	currencies c 
ON 
	a.currency_id = c.id
-- WHERE u.id = 1  -- Включить для выбора пользователя
ORDER BY 
	u.id, ab.bank_id, a.account_type_id;
	
	
	
-- Рейтинг богатства
-- 
SELECT 
	CONCAT(u.firstname, ' ', u.lastname) AS 'Полное имя',
	SUM(ROUND(course_to_data(ab.currency_id, CURDATE()) * ab.balance, 2)) AS 'Баланс в рублях'
FROM 
	users u 
LEFT JOIN 
	accounts_balanse ab   
ON 
	ab.owner_id = u.id 
GROUP BY 
	u.id 
ORDER BY
	`Баланс в рублях` DESC;

-- Самый доходный месяц. 
-- Месяц (не месяц и год), когда была наибольшая прибыль
SELECT cd.owner_id, MONTH(t.date_transactiont) AS m_debit, sum(t.sum_debit) AS s_debit
FROM categories_debit cd
JOIN transactions t ON cd.id = t.id 
	-- AND cd.owner_id = 1 - включить для выбора конкретного пользователя
GROUP BY cd.owner_id, m_debit
ORDER BY cd.owner_id, s_debit DESC;


-- Денежный поток по месяцам
-- Разница между прибылью и расходами по месяцам.
-- Тут имеется ввиду календарный месяц и год

SELECT COALESCE(a.owner_id, a2.owner_id) AS user_id,
		EXTRACT(YEAR_MONTH FROM t.date_transactiont) AS m,
		SUM(CASE 
			WHEN t.from_id IS NULL THEN t.sum_debit * course_to_data(a2.currency_id, t.date_transactiont) 
			WHEN t.to_id  IS NULL THEN -t.sum_credit * course_to_data(a.currency_id, t.date_transactiont)
			ELSE 0 END) AS profit 
FROM transactions t
LEFT JOIN accounts a ON a.id = t.from_id 
LEFT JOIN accounts a2 ON a2.id = t.to_id 
-- WHERE a.owner_id = 1 OR a2.owner_id =1 - включить для выбора конкретного пользователя
GROUP BY user_id, m
ORDER BY user_id, m;


-- Траты по категориям
SELECT cd.owner_id, c2.name AS parrent, 
		if(c.id != c.parrent_id, c.name, '---') AS category,
		sum(cd.sum_debit) AS s_debit
FROM categories_debit cd 
JOIN categories c ON c.id = cd.category_id 
JOIN categories c2 ON c2.id = c.parrent_id
-- WHERE cd.owner_id = 1 - включить для выбора конкретного пользователя
GROUP BY cd.owner_id, c2.id, c.id 
ORDER BY cd.owner_id, c2.id, c.id; 

-- Самый популярный банк по количеству счетов
SELECT b.name, count(*) AS cnt -- можно использовать *, т.к. JOIN убрал все NULL в a.bank_id
FROM accounts a 
JOIN banks b ON b.id = a.bank_id 
GROUP BY b.id
ORDER BY cnt DESC;

-- Самый доходный тип счетов для пользователя
SELECT cd.owner_id, at2.name, 
		sum(cd.sum_debit * course_to_data(a.currency_id, t.date_transactiont)) AS debit
FROM categories_debit cd 
JOIN transactions t ON t.id = cd.id 
JOIN accounts a ON t.to_id = a.id 
JOIN account_types at2 ON a.account_type_id = at2.id 
GROUP BY cd.owner_id, a.account_type_id 
ORDER BY cd.owner_id, debit DESC;


/*
 * Можно было еще написать аналогичные запросы:
 * - Доходы по категориям
 * - Самый популярный тип счетов
 * 
 * но это уже не продемонстрирует уровень усвоения.
 * Запросы получились не очень сложными, т.к. я специально
 * подгонял представления под них.
 * В принципе можно было еще оптимизировать представления, но тогда бы 
 * запросы получилсь совсем элементарными
 */



	