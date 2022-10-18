USE vk;

/* 
* ЗАДАЧА 1
*
* Пусть задан некоторый пользователь. 
* Из всех друзей этого пользователя найдите человека, 
* который больше всех общался с нашим пользователем.
* 
Определить кто больше поставил лайков (всего): мужчины или женщины.
*/

-- Я забежал вперед, но вся моя программисткая сущность протестует против
-- констант в виде цифр в коде

SET @my_user = 1; -- некоторый пользователь

-- Исходил из того, что больше всего общался значит посылал сообщения.
-- Поэтому игнорировал ситуацию, когда сообщения посылал наш пользователь
-- Сортировка и Limit позволяют получить одного пользователя

SELECT from_user_id, COUNT(*) AS cnt FROM messages
WHERE to_user_id = @my_user AND from_user_id IN (	
	SELECT IF(initiator_user_id = @my_user, target_user_id, initiator_user_id) AS friend_id
	FROM friend_requests
	WHERE (initiator_user_id = @my_user OR target_user_id = @my_user) AND 
			status = 'approved')
GROUP BY from_user_id
ORDER BY cnt DESC 
LIMIT 1;

/* 
* ЗАДАЧА 2
* 
* Подсчитать общее количество лайков, которые получили пользователи младше 11 лет.
* 
*/

SET @max_age = 11;

SELECT COUNT(*) AS cnt 
FROM likes
WHERE user_id IN (
	SELECT user_id
	FROM profiles 
	WHERE timestampdiff(YEAR, birthday, NOW()) < @max_age);


/* 
* ЗАДАЧА 3
* 
* Определить кто больше поставил лайков (всего): мужчины или женщины.
*
*/

-- Как-то сложно все получилось.
-- Есть ли простой способ тарвернуть строки в столбцы?
-- Буду с нетерпением ждать разбора этого ДЗ

SELECT CASE 
	WHEN F > M THEN 'Больше лайков от женщин'
	WHEN F < M THEN 'Больше лайков от мужчин'
	ELSE 'Лайков поровну'
END AS result

FROM (
	SELECT 
		sum(case when gender = 'f' then cnt ELSE 0 end) as F,
		sum(case when gender = 'm' then cnt ELSE 0 end) as M		
	FROM (
		SELECT count(*) AS cnt, (	
			SELECT gender 
			FROM profiles
			WHERE profiles.user_id = likes.user_id) AS gender
		FROM likes
		GROUP BY gender) AS gender_table) AS cnt_table;


