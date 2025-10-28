### HDFS: Hadoop Distributed File System

HDFS (Hadoop Distributed File System) is the primary storage system used by Hadoop applications. It provides high-throughput access to application data and is designed to store large datasets reliably, and to stream those datasets at high bandwidth to user applications.

#### Key Features of HDFS

1. **Fault Tolerance**:
   - HDFS is designed to handle hardware failures gracefully. Data is replicated across multiple nodes to ensure that it remains accessible even if some nodes fail.
   - The default replication factor is three, meaning that each data block is stored on three different nodes.

2. **Scalability**:
   - HDFS can scale to petabytes of data and thousands of nodes. It is designed to handle very large files and to support large clusters of nodes.
   - The architecture allows for horizontal scaling, which means adding more nodes to the cluster increases storage capacity and processing power.

3. **Data Locality**:
   - HDFS optimizes data access by moving computation to the location where the data resides, minimizing network congestion and improving processing speed.
   - This is achieved through the rack-aware placement of data blocks.

4. **High Throughput**:
   - HDFS is optimized for high throughput of data access, making it suitable for batch processing rather than low-latency access to small chunks of data.
   - It supports large-scale data processing applications like MapReduce, which require high data transfer rates.

5. **Streaming Data Access**:
   - HDFS provides a streaming data access pattern, which is particularly suitable for applications that need to process large datasets sequentially.
   - This design choice makes it ideal for write-once, read-many use cases.

#### Important Considerations

- **Data Replication**: Data is automatically replicated to multiple nodes. The replication factor can be configured based on reliability requirements.
- **Block Size**: HDFS breaks files into large blocks (default 128 MB), which are then distributed across the cluster.
- **NameNode and DataNodes**: HDFS follows a master-slave architecture with a single NameNode managing metadata and multiple DataNodes storing actual data.

#### Practical Implementation of HDFS in Our Project

1. **Data Ingestion**: We used HDFS to store the MovieLens 100k dataset, ensuring it is distributed and fault-tolerant.
2. **Data Access**: Various processing frameworks like MapReduce, Hive, Pig, Spark, and Tez accessed data directly from HDFS.
3. **Replication**: Ensured data reliability by configuring appropriate replication factors for our data blocks.

### Important Commands for HDFS

Here are some key commands we used during our project to interact with HDFS:

- **Uploading Data to HDFS**:
  ```bash
  hdfs dfs -put /local/path/to/dataset /hdfs/path/to/destination
  ```

- **Listing Files in HDFS**:
  ```bash
  hdfs dfs -ls /hdfs/path/to/directory
  ```

- **Checking HDFS Disk Usage**:
  ```bash
  hdfs dfs -du -h /hdfs/path/to/directory
  ```

- **Reading a File from HDFS**:
  ```bash
  hdfs dfs -cat /hdfs/path/to/file
  ```

- **Removing a File from HDFS**:
  ```bash
  hdfs dfs -rm /hdfs/path/to/file
  ```

- **Changing Replication Factor**:
  ```bash
  hdfs dfs -setrep -w 3 /hdfs/path/to/file_or_directory
  ```

- **Checking the Status of HDFS**:
  ```bash
  hdfs dfsadmin -report
  ```

### Points to Remember

- **HDFS Setup**: Ensure HDFS is properly configured and running on your Hadoop cluster.
- **Data Placement**: Pay attention to the replication factor and block size for optimal performance and reliability.
- **Fault Tolerance**: Regularly monitor the health of DataNodes and the NameNode to prevent data loss.

By leveraging HDFS, we ensured that our dataset was securely stored, easily accessible, and processed efficiently using various Hadoop components. This setup provided a robust foundation for our big data processing tasks.