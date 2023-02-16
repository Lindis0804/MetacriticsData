""" 
[Spark test]
"""
from pyspark.sql import SparkSession
from hdfs import InsecureClient
import pandas as pd
import numpy as np
import glob
import json
import ast

# spark = SparkSession.builder.master('local').appName('test').enableHiveSupport().getOrCreate()

# df = spark.read.option("multiline","true").json("hdfs://namenode:9000/films-*.csv")
# hdfs_client = InsecureClient('http://localhost:9870', user='root')
# hdfs_files = hdfs_client.list('/')
# # df = spark.read.csv('hdfs://namenode:9000/')
# # df = pd.concat(map(pd.read_csv, glob.glob("/*.csv")))
# frames = []
# for hdfs_file in hdfs_files:
#     print(f'[x] Reading: {hdfs_file}')
#     with hdfs_client.read('/' + hdfs_file) as reader:
#         data = pd.read_csv(reader)
#         frames.append(data)

# result = pd.concat(frames)
# print(result.head(10))
# Get data from hadoop

arr1 = [1, 2, 3, 4]
arr2 = [2, 3, 4, 5]
print(arr1 + arr2)
