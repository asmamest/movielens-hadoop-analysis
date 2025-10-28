from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_unixtime, year, avg

# Initialize Spark Session
spark = SparkSession.builder.appName("RatingTrendsOverTime").getOrCreate()

# Load the ratings data
ratings = spark.read.csv("/user/maria_dev/ml-100k/u.data", sep="\t", inferSchema=True)
ratings = ratings.withColumnRenamed("_c0", "user_id") \
                 .withColumnRenamed("_c1", "movie_id") \
                 .withColumnRenamed("_c2", "rating") \
                 .withColumnRenamed("_c3", "timestamp")

# Convert timestamp to year
ratings = ratings.withColumn("year", year(from_unixtime(col("timestamp"))))

# Calculate the average rating per year
average_rating_per_year = ratings.groupBy("year").agg(avg("rating").alias("avg_rating"))

# Show the trends in ratings over the years
average_rating_per_year.orderBy("year").show()

# Stop the Spark session
spark.stop()
