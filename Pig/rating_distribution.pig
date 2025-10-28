-- Load the data
ratings = LOAD '/user/maria_dev/ml-100k/u.data' USING PigStorage('\t') AS (user_id:int, movie_id:int, rating:int, timestamp:int);

-- Count the number of each rating
ratings_group = GROUP ratings BY rating;
rating_distribution = FOREACH ratings_group GENERATE group AS rating, COUNT(ratings) AS count;

-- Order by rating value
ordered_rating_distribution = ORDER rating_distribution BY rating;

-- Store the result
STORE ordered_rating_distribution INTO '/output/rating_distribution';
