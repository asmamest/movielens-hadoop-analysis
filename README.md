# MOVIELENS - HADOOP Project

## Project Overview

This project utilizes a comprehensive Big Data ecosystem to process and analyze the MovieLens 100k dataset. By employing Hadoop's distributed storage (HDFS) and multiple data processing frameworks, we demonstrate efficient management and analysis of large-scale datasets. The workflow includes data ingestion into HDFS, followed by processing through various Hadoop ecosystem components such as MapReduce, Hive, Spark, and Pig.


Through the integration of these diverse technologies, the project illustrates the benefits and practical implementations of each component, offering a detailed guide for handling and analyzing big data in real-world scenarios. This approach not only emphasizes the unique advantages of each technology but also provides comparative insights into their performance and usability, helping to identify the most suitable tools for specific data processing requirements.


### Project Architecture

The MovieLens 100k Data Analysis Project is structured to demonstrate the capabilities of various Hadoop ecosystem components in processing and analyzing large datasets. The project follows a comprehensive data pipeline starting from data ingestion into HDFS, followed by processing using multiple Hadoop components, and concluding with data export operations. Each component is chosen to highlight its specific strengths and use cases in big data processing.

### Architecture Overview

The project architecture involves the following key steps:

1. **Data Ingestion**: The MovieLens 100k dataset is loaded into Hadoop Distributed File System (HDFS), ensuring reliable and scalable storage.
2. **Data Processing**: Multiple processing frameworks are used to transform and analyze the data:
   - **MapReduce**: The core Hadoop processing framework, illustrating fundamental distributed data processing.
   - **Hive**: A data warehousing tool that enables data querying using SQL-like syntax.
   - **Pig**: A high-level scripting language for expressing data transformations.
   - **Spark**: A fast and general-purpose cluster computing system for large-scale data processing.


### Project Structure

```
MovieLens 100k Data Analysis Project
|
|-- 1. Data Ingestion
|   |-- HDFS
|       |-- Upload data to HDFS
|
|-- 2. Data Processing
|   |-- MapReduce
|       |-- Implement MapReduce to process data
|
|   |-- Hive
|       |-- Create tables and execute queries
|
|   |-- Pig
|       |-- Write Pig scripts for data transformation
|
|   |-- Spark
|       |-- Process data using Spark
|
```

This architecture ensures that the dataset is efficiently ingested, processed, and exported, demonstrating the versatility and power of the Hadoop ecosystem in handling large-scale data processing tasks. Each component is utilized to its strengths, providing a comprehensive overview of big data processing techniques.

### Setting Up and Running the Project Locally

To set up and run this project locally, follow these steps:

#### Prerequisites

1. **Hortonworks Data Platform (HDP)**: Ensure you have HDP installed on your local machine. You can download the sandbox from the [Hortonworks website](https://www.cloudera.com/downloads/hortonworks-sandbox.html).
2. **Virtualization Software**: Install a virtualization software like VirtualBox or VMware to run the HDP sandbox.
3. **SSH Client**: Use an SSH client like PuTTY (for Windows) or terminal (for Mac/Linux) to connect to the sandbox.

#### Step-by-Step Setup

1. **Download and Set Up HDP Sandbox**:
   - Download the HDP sandbox from the Hortonworks website.
   - Import the sandbox into your virtualization software and start the virtual machine.

2. **Access the HDP Sandbox**:
   - Use an SSH client to connect to the sandbox.
   - The default username is `maria_dev`, and the password is usually `maria_dev`.

3. **Upload Data to HDP Sandbox**:
   - Use the `scp` command to transfer data from your local machine to the sandbox.
     ```bash
     scp -P <num> /local/path/to/dataset maria_dev@<sandbox-ip>:/sandbox/path
     ```


By following these steps, you can set up and run the project locally, leveraging the various Hadoop components we have used. This setup ensures a comprehensive understanding and practical application of the Hadoop ecosystem.