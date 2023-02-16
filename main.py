""" 
[Spark test]
"""
from pyspark.sql import SparkSession
# from hdfs import InsecureClient

spark = SparkSession.builder.master('local[*]').getOrCreate()

# df = spark.read.option("multiline","true").json("hdfs://namenode:9000/films-*.csv")
# hdfs_client = InsecureClient('http://localhost:9870', user='root')
# hdfs_files = hdfs_client.list('/')
df = spark.read.csv('hdfs://namenode:9000/films.csv')

print(df.head(10))
# Get data from hadoop