from pyspark.sql import SparkSession
from pyspark.sql.functions import count

# Initialize Spark Session
spark = SparkSession.builder.appName("RatingsDistribution").getOrCreate()

# Load the ratings data
ratings = spark.read.csv("/user/maria_dev/ml-100k/u.data", sep="\t", inferSchema=True)
ratings = ratings.withColumnRenamed("_c0", "user_id") \
                 .withColumnRenamed("_c1", "movie_id") \
                 .withColumnRenamed("_c2", "rating") \
                 .withColumnRenamed("_c3", "timestamp")

# Count the number of each rating value
rating_distribution = ratings.groupBy("rating").agg(count("rating").alias("count"))

# Show the distribution of ratings
rating_distribution.orderBy("rating").show()

# Stop the Spark session
spark.stop()
