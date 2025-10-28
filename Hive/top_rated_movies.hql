-- Query to find the top-rated movies with at least 50 ratings
SELECT m.title, AVG(r.rating) AS avg_rating, COUNT(r.rating) AS num_ratings
FROM ratings r
JOIN movies m ON (r.movie_id = m.movie_id)
GROUP BY m.title
HAVING COUNT(r.rating) >= 50
ORDER BY avg_rating DESC
LIMIT 10;
