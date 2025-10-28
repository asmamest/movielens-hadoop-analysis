-- Query to find the distribution of ratings
SELECT rating, COUNT(*) AS count
FROM ratings
GROUP BY rating
ORDER BY rating;
