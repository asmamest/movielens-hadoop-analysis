# Pig.md

## Overview

Apache Pig is a high-level platform for creating MapReduce programs used with Hadoop. Pig Latin, the language for this platform, allows developers to write complex data transformations in a simpler and more intuitive manner compared to raw MapReduce code. Pig is particularly useful for processing and analyzing large data sets stored in HDFS.

## Project Implementation

### Data Storage and Schema

We utilized Apache Pig to process our datasets stored in HDFS. Pig scripts enable extensive data transformation and analysis through a series of steps written in Pig Latin.

### Data Loading and Processing

1. **Loading Data**:
   Load data into Pig using the `LOAD` function. For instance:
   ```pig
   data = LOAD '/user/maria_dev/data.csv' USING PigStorage(',') AS (field1:type1, field2:type2, ...);
   ```

2. **Viewing Data**:
   Use the `DUMP` command to display the contents of a relation:
   ```pig
   DUMP data;
   ```

3. **Storing Data**:
   Store processed data back into HDFS using the `STORE` function:
   ```pig
   STORE data INTO '/user/maria_dev/processed_data' USING PigStorage(',');
   ```

4. **Running Pig Scripts**:
   Execute Pig scripts containing Pig Latin commands using:
   ```bash
   pig -f script.pig
   ```

### Points to Remember

- **Output Directory Cleanup**: When re-running Pig scripts, ensure that the output directory does not already exist. Pig will fail if the output directory is present. Use commands to delete or empty the directory before re-running the script.
- **Procedural Language**: Pig processes data in a procedural step-by-step manner. It uses 'relations' to manage data at each step of the process.

### Important Commands

1. **Start Pig Grunt Shell**:
   ```bash
   pig
   ```

2. **Execute Pig Script**:
   ```bash
   pig -f script.pig
   ```

3. **Load Data in Pig**:
   ```pig
   data = LOAD '/user/maria_dev/data.csv' USING PigStorage(',') AS (field1:type1, field2:type2, ...);
   ```

4. **View Data in Pig**:
   ```pig
   DUMP data;
   ```

5. **Store Data in Pig**:
   ```pig
   STORE data INTO '/user/maria_dev/processed_data' USING PigStorage(',');
   ```

By following these guidelines and utilizing the key points mentioned, one can effectively use Apache Pig for data processing and transformation in a Hadoop environment.