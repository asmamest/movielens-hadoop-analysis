-- Load the data
ratings = LOAD '/user/maria_dev/ml-100k/u.data' USING PigStorage('\t') AS (user_id:int, movie_id:int, rating:int, timestamp:int);

-- Extract year from the timestamp (assuming timestamp is in seconds since epoch)
ratings_with_year = FOREACH ratings GENERATE movie_id, rating, (int)(timestamp / 31556926 + 1970) AS year;

-- Calculate average rating per year
year_group = GROUP ratings_with_year BY year;
average_ratings_per_year = FOREACH year_group GENERATE group AS year, AVG(ratings_with_year.rating) AS avg_rating;

-- Order by year
ordered_average_ratings_per_year = ORDER average_ratings_per_year BY year;

-- Store the result
STORE ordered_average_ratings_per_year INTO '/output/rating_trends_over_time';
