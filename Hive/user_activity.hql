-- Query to find the number of ratings per user
SELECT user_id, COUNT(*) AS num_ratings
FROM ratings
GROUP BY user_id
ORDER BY num_ratings DESC
LIMIT 10;
