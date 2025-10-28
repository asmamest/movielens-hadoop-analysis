-- Load the data
ratings = LOAD '/user/maria_dev/ml-100k/u.data' USING PigStorage('\t') AS (user_id:int, movie_id:int, rating:int, timestamp:int);

-- Calculate the average rating per movie
movie_group = GROUP ratings BY movie_id;
average_ratings = FOREACH movie_group GENERATE group AS movie_id, AVG(ratings.rating) AS avg_rating;

-- Store the result
STORE average_ratings INTO '/output/average_ratings';
