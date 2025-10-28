from pyspark.sql import SparkSession
from pyspark.sql.functions import count

# Initialize Spark Session
spark = SparkSession.builder.appName("UserActivity").getOrCreate()

# Load the ratings data
ratings = spark.read.csv("/user/maria_dev/ml-100k/u.data", sep="\t", inferSchema=True)
ratings = ratings.withColumnRenamed("_c0", "user_id") \
                 .withColumnRenamed("_c1", "movie_id") \
                 .withColumnRenamed("_c2", "rating") \
                 .withColumnRenamed("_c3", "timestamp")

# Count the number of ratings per user
user_activity = ratings.groupBy("user_id").agg(count("rating").alias("num_ratings"))

# Show the top 10 users who rated the most movies
user_activity.orderBy("num_ratings", ascending=False).show(10)

# Stop the Spark session
spark.stop()
