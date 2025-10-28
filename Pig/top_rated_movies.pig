-- Load the data
ratings = LOAD '/user/maria_dev/ml-100k/u.data' USING PigStorage('\t') AS (user_id:int, movie_id:int, rating:int, timestamp:int);

-- Calculate the average rating per movie
movie_group = GROUP ratings BY movie_id;
average_ratings = FOREACH movie_group GENERATE group AS movie_id, AVG(ratings.rating) AS avg_rating;

-- Filter movies with an average rating greater than a threshold (e.g., 4.0)
top_rated_movies = FILTER average_ratings BY avg_rating > 4.0;

-- Order by average rating in descending order
ordered_top_rated_movies = ORDER top_rated_movies BY avg_rating DESC;

-- Store the result
STORE ordered_top_rated_movies INTO '/output/top_rated_movies';
