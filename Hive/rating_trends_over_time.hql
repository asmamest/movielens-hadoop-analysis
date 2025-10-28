-- Convert timestamp to year and create a temporary table
USE movielens; 

CREATE TEMPORARY TABLE ratings_with_year AS 
SELECT *, 
FROM_UNIXTIME(rating_timestamp, 'yyyy') AS year 
FROM ratings;

 -- Query to find the average rating per year 
INSERT OVERWRITE LOCAL DIRECTORY '/home/maria_dev/average_ratings'
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
SELECT year, AVG(rating) AS avg_rating
FROM ratings_with_year
GROUP BY year
ORDER BY year;