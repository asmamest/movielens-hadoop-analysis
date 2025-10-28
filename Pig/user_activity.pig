-- Load the data
ratings = LOAD '/user/maria_dev/ml-100k/u.data' USING PigStorage('\t') AS (user_id:int, movie_id:int, rating:int, timestamp:int);

-- Count the number of ratings per user
user_counts = GROUP ratings BY user_id;
user_rating_counts = FOREACH user_counts GENERATE group AS user_id, COUNT(ratings) AS rating_count;

-- Order by the number of ratings in descending order
ordered_user_counts = ORDER user_rating_counts BY rating_count DESC;

-- Store the result
STORE ordered_user_counts INTO '/output/user_activity';
