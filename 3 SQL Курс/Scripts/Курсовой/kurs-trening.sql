
SET @dt = '2022-06-15';

SELECT max(cc.date_course) AS max_date
FROM currencies_courses cc 
WHERE cc.date_course <= @dt AND cc.currency_id = 3;

-- Большой и сложный выбор транзакции и курса
SELECT t.id, t.from_id, t.to_id, t.sum_credit, t.sum_debit, t.date_transactiont, a_f.currency_id AS f_c, a_t.currency_id AS t_c, (
	SELECT cc.course 
	FROM currencies_courses cc 
	WHERE cc.currency_id = a_f.currency_id AND cc.date_course = (
		SELECT max(cc2.date_course)
		FROM currencies_courses cc2
		WHERE cc2.date_course <= t.date_transactiont  AND cc2.currency_id = a_f.currency_id 
		)
	) AS f_course, (
	SELECT cc3.course 
	FROM currencies_courses cc3 
	WHERE cc3.currency_id = a_t.currency_id AND cc3.date_course = (
		SELECT max(cc4.date_course)
		FROM currencies_courses cc4
		WHERE cc4.date_course <= t.date_transactiont  AND cc4.currency_id = a_t.currency_id 
		)
	) AS t_course
FROM transactions t 
LEFT JOIN accounts a_f
ON t.from_id = a_f.id 
LEFT JOIN accounts a_t 
ON t.to_id = a_t.id 

-- Обновление сумм в соответсвии с курсом 
UPDATE transactions, (
	SELECT t.id, (
		SELECT cc.course 
		FROM currencies_courses cc 
		WHERE cc.currency_id = a_f.currency_id AND cc.date_course = (
			SELECT max(cc2.date_course)
			FROM currencies_courses cc2
			WHERE cc2.date_course <= t.date_transactiont  AND cc2.currency_id = a_f.currency_id 
			)
		) AS f_course, (
		SELECT cc3.course 
		FROM currencies_courses cc3 
		WHERE cc3.currency_id = a_t.currency_id AND cc3.date_course = (
			SELECT max(cc4.date_course)
			FROM currencies_courses cc4
			WHERE cc4.date_course <= t.date_transactiont  AND cc4.currency_id = a_t.currency_id 
			)
		) AS t_course
	FROM transactions t 
	LEFT JOIN accounts a_f
	ON t.from_id = a_f.id 
	LEFT JOIN accounts a_t 
	ON t.to_id = a_t.id 
	) AS full_t
SET 
	transactions.sum_credit = transactions.sum_credit / f_course,
	transactions.sum_debit = transactions.sum_debit / t_course
WHERE 
	transactions.id = full_t.id

-- Баланс счетов	
SELECT a.id , a.balance , a.start_balance, 
	sum(IF (a.id = tf.from_id, tf.sum_credit,0)) AS credit,
	sum(IF (a.id = tf.to_id, tf.sum_debit, 0)) AS debit
FROM accounts a
LEFT JOIN transactions tf
ON a.id = tf.from_id OR a.id = tf.to_id 
GROUP BY a.id 

-- обновление балансов счета
UPDATE accounts, (
	SELECT a.id, 
		sum(IF (a.id = tf.from_id, tf.sum_credit,0)) AS s_credit,
		sum(IF (a.id = tf.to_id, tf.sum_debit, 0)) AS s_debit
	FROM accounts a
	LEFT JOIN transactions tf
	ON a.id = tf.from_id OR a.id = tf.to_id 
	GROUP BY a.id 
	) AS sum_tr
SET z
	balance = s_debit - s_credit + start_balance 
WHERE 
	accounts.id = sum_tr.id
















