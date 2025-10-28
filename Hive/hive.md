# Hive.md

## Overview

Apache Hive is a data warehousing tool built on top of Hadoop. It allows for querying and managing large datasets residing in distributed storage using SQL-like syntax. Hive abstracts the complexity of Hadoop's MapReduce framework, providing an easy-to-use interface for data analysis.

## Project Implementation

### Data Storage and Schema

We used Hive to manage and query our data stored in HDFS. Hive provides a SQL-like interface called HiveQL, which is used to define data schemas, load data into tables, and perform various data manipulations.

### Data Loading

We loaded our datasets into Hive tables using the following steps:

1. **Create Database**:

   ```sql
   CREATE DATABASE movielens;
   USE movielens;
   ```

2. **Create External Tables**:

   ```sql
   CREATE EXTERNAL TABLE movies (
       movie_id INT,
       movie_title STRING,
       genre STRING
   )
   ROW FORMAT DELIMITED
   FIELDS TERMINATED BY ','
   STORED AS TEXTFILE
   LOCATION '/user/maria_dev/ml-100k/movies';
   ```

3. **Load Data**:
   Data was already present in HDFS, so we pointed the external table to the corresponding HDFS directory.

```bash
scp -P 2222 "C:\Users\user\Desktop\Hadoop-Project-master\Hive\Movies_Table_definition.hql" maria_dev@localhost:/home/maria_dev/
```

```bash
ls -l /home/maria_dev/*.hql
```

You have to see something like this :

```bash
-rw-r--r-- 1 maria_dev users 40800 Oct 21  Movies_Table_definition.hql
-rw-r--r-- 1 maria_dev users 16500 Oct 21  Ratings_Table_definition.hql
-rw-r--r-- 1 maria_dev users 30400 Oct 21  rating_trends_over_time.hql
-rw-r--r-- 1 maria_dev users 12400 Oct 21  ratings_distribution.hql
-rw-r--r-- 1 maria_dev users 27800 Oct 21  top_rated_movies.hql
-rw-r--r-- 1 maria_dev users 37600 Oct 21  user_activity.hql
```

### Query Execution

Hive provides various ways to run queries and interact with the data:

1. **Hive Shell**:
   The Hive shell is an interactive shell for Hive query execution. It can be accessed using the following command:

   ```bash
   hive
   ```

   This will open the Hive CLI where you can execute HiveQL statements.

2. **Hive Scripts**:
   Hive scripts allow you to run multiple HiveQL statements in a batch mode. Create a `.hql` file containing your queries and execute it using:

   ```bash
   hive -f script.hql
   ```

3. **Beeline**:
   Beeline is a JDBC client that is included in Hive and is used for connecting to HiveServer2. It can be accessed using:
   ```bash
   beeline
   ```
   Then, connect to HiveServer2 using:
   ```bash
   !connect jdbc:hive2://<hostname>:<port> <username> <password>
   ```

### Points to Remember

- **Using External Tables**: External tables in Hive are used to manage data outside the warehouse directory. The data is not deleted when dropping an external table.
- **Hive Optimization**: Consider using partitioning and bucketing for optimizing large datasets.
- **Data Types and Schema**: Ensure correct data types and schema are defined for Hive tables to avoid errors during querying.

### Important Commands

1. **Start Hive Shell**:

   ```bash
   hive
   ```

2. **Execute Hive Script**:

   ```bash
   hive -f script.hql
   ```

3. **Start Beeline**:

   ```bash
   beeline
   ```

4. **Connect to HiveServer2 Using Beeline**:
   ```bash
   !connect jdbc:hive2://<hostname>:<port> <username> <password>
   ```

By following the above steps and remembering the key points, one can effectively use Hive for managing and querying large datasets in a Hadoop environment.
