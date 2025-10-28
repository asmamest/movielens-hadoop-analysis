-- Query to calculate the average rating per movie
SELECT movie_id, AVG(rating) AS avg_rating
FROM ratings
GROUP BY movie_id
ORDER BY avg_rating DESC;
