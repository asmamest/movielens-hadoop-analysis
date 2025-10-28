from pyspark.sql import SparkSession
from pyspark.sql.functions import avg

# Initialize Spark Session
spark = SparkSession.builder.appName("AverageRatings").getOrCreate()

# Load the ratings data
ratings = spark.read.csv("/user/maria_dev/ml-100k/u.data", sep="\t", inferSchema=True)
ratings = ratings.withColumnRenamed("_c0", "user_id") \
                 .withColumnRenamed("_c1", "movie_id") \
                 .withColumnRenamed("_c2", "rating") \
                 .withColumnRenamed("_c3", "timestamp")

# Calculate the average rating per movie
average_ratings = ratings.groupBy("movie_id").agg(avg("rating").alias("avg_rating"))

# Show the average ratings for each movie
average_ratings.show()

# Stop the Spark session
spark.stop()
