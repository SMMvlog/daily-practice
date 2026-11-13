from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("MyFirstSpark").master("local[*]").getOrCreate()

print("Spark started successfully!")
