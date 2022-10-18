USE vk;

/* 
* ЗАДАЧА 1
*
* Пусть задан некоторый пользователь. 
* Из всех друзей этого пользователя найдите человека, 
* который больше всех общался с нашим пользователем.
* 
*/



SET @my_user = 1; -- некоторый пользователь

SELECT 
	CONCAT(u.firstname, ' ', u.lastname) AS fullname, 
	COUNT(*) AS cnt 
FROM messages m
JOIN friend_requests fr 
ON 
	m.to_user_id = @my_user AND (
	fr.initiator_user_id = m.from_user_id AND fr.target_user_id = @my_user OR
	fr.target_user_id = m.from_user_id AND fr.initiator_user_id = @my_user)
JOIN users u ON u.id = m.from_user_id 
WHERE fr.status = 'approved'
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
FROM likes l
JOIN media m ON l.media_id = m.id 
JOIN profiles p ON p.user_id = m.user_id 
WHERE timestampdiff(YEAR, p.birthday, NOW()) < @max_age;


/* 
* ЗАДАЧА 3
* 
* Определить кто больше поставил лайков (всего): мужчины или женщины.
*
*/

SELECT p.gender, COUNT(*) AS cnt 
FROM likes l 
JOIN profiles p ON l.user_id = p.user_id 
GROUP BY p.gender
ORDER BY cnt DESC;

/* 
* ЗАДАЧА 4
* 
* Список медиафайлов пользователя с количеством лайков.
*
*/


SELECT 
	m.filename,
	COUNT(l.id) AS total_likes,
	CONCAT(u.firstname, ' ', u.lastname) AS owner
FROM media m
LEFT JOIN likes l ON l.media_id = m.id
JOIN users u ON u.id = m.user_id
WHERE u.id=@my_user
GROUP BY m.id
ORDER BY total_likes DESC;

