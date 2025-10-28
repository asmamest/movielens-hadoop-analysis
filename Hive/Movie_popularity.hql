-- Query to find the number of ratings per movie

SELECT movie_id, COUNT(*) AS num_ratings
FROM movielens.ratings
GROUP BY movie_id
ORDER BY num_ratings DESC
LIMIT 10;