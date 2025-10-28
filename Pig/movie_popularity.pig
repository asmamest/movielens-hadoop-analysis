-- Load the data
ratings = LOAD '/user/maria_dev/ml-100k/u.data' USING PigStorage('\t') AS (user_id:int, movie_id:int, rating:int, timestamp:int);

-- Count the number of ratings per movie
movie_counts = GROUP ratings BY movie_id;
movie_rating_counts = FOREACH movie_counts GENERATE group AS movie_id, COUNT(ratings) AS rating_count;

-- Order by the number of ratings in descending order
ordered_movie_counts = ORDER movie_rating_counts BY rating_count DESC;

-- Store the result
STORE ordered_movie_counts INTO '/output/movie_popularity';
