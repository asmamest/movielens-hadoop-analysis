from pyspark.sql import SparkSession
from pyspark.sql.functions import avg

# Initialize Spark Session
spark = SparkSession.builder.appName("TopRatedMovies").getOrCreate()

# Load the ratings data
ratings = spark.read.csv("/user/maria_dev/ml-100k/u.data", sep="\t", inferSchema=True)
ratings = ratings.withColumnRenamed("_c0", "user_id") \
                 .withColumnRenamed("_c1", "movie_id") \
                 .withColumnRenamed("_c2", "rating") \
                 .withColumnRenamed("_c3", "timestamp")

# Calculate the average rating per movie
average_ratings = ratings.groupBy("movie_id").agg(avg("rating").alias("avg_rating"))

# Filter movies with at least a certain number of ratings for reliability
minimum_ratings = 50
movies_with_min_ratings = ratings.groupBy("movie_id").count().filter("count >= {}".format(minimum_ratings))

# Join the dataframes to only include movies with sufficient ratings
top_rated = average_ratings.join(movies_with_min_ratings, "movie_id")

# Show the top-rated movies
top_rated.orderBy("avg_rating", ascending=False).show(10)

# Stop the Spark session
spark.stop()
