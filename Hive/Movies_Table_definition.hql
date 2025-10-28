-- Create the movies table (assuming the u.item file is loaded)
USE movielens;

CREATE TABLE IF NOT EXISTS movies (
    movie_id INT,
    title STRING,
    release_date STRING,
    video_release_date STRING,
    IMDb_URL STRING,
    genre STRING
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '|'
COLLECTION ITEMS TERMINATED BY ',';

-- Load data into the movies table
LOAD DATA INPATH '/user/maria_dev/ml-100k/u.data' INTO TABLE movies;