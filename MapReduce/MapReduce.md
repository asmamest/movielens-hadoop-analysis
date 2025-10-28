## MapReduce

MapReduce is a powerful programming model for processing large datasets with a distributed algorithm on a Hadoop cluster. It simplifies data processing by dividing the task into two primary phases: the map phase and the reduce phase.

### MapReduce Streaming and Libraries

**MapReduce Streaming** is a utility that allows users to create and run MapReduce jobs with any executable or script as the mapper and/or reducer. This is particularly useful for developers familiar with languages like Python, Perl, and Ruby.

In this project, we utilized **Hadoop Streaming** to integrate our Python scripts for data processing. Hadoop Streaming allows us to execute scripts using standard input (stdin) and standard output (stdout) for communication between the Hadoop framework and the user-defined scripts.

- **Standard Input (stdin)**: The input data for the mapper is passed as standard input. Each line of input is processed by the mapper.
- **Standard Output (stdout)**: The mapper writes the output key-value pairs to standard output, which is then passed to the reducer.

**mrjob**: We used the `mrjob` library, a Python package that simplifies writing and running Hadoop Streaming jobs. This library handles many complexities of Hadoop, making it easier to focus on the logic of data processing.

#### Using stdin and stdout

In our MapReduce implementation, the mapper reads input from stdin and writes output to stdout. This is how Hadoop Streaming interfaces with our Python scripts. Here’s a conceptual flow:

1. **Mapper**: Reads input from stdin, processes each line, and writes key-value pairs to stdout.
2. **Reducer**: Reads intermediate key-value pairs from stdin and writes the final output to stdout.

#### Saving and Running the Python Script

To save and execute our Python script for calculating movie popularity, we followed these steps:

1. **Save the Python Script**  
   Save the mapper and reducer logic in a Python file (e.g., `moviepopularity.py`).

2. **Run the MapReduce Job Locally**
   ```bash
   python moviepopularity.py ml-100k/u.data > output_mapreduce/output_moviepopularity.txt
   ```

**Note**: Ensure that the following are installed and set up:

- **Python**: Python should be pre-installed on your system.
- **mrjob library**: Install the `mrjob` library using pip:
  ```bash
  pip install mrjob
  ```
- **Hadoop**: Hadoop should be installed and configured on your system to run Hadoop Streaming jobs.

By understanding and utilizing Hadoop Streaming, we can leverage the power of Hadoop with the flexibility of Python for efficient data processing.
