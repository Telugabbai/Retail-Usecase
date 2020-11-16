from pyspark.sql import SparkSession

from pyspark.sql import functions as F

spark = SparkSession.builder.master("local").appName("dslsd").getOrCreate()