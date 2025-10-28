CREATE TABLE IF NOT EXISTS ratings (
    user_id INT,
    movie_id INT,
    rating INT,
    rating_timestamp BIGINT
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '\t';