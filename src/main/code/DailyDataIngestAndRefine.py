from pyspark.sql import SparkSession
from pyspark.sql.types import StringType,StructType,StructField,IntegerType,DoubleType,TimestampType
import configparser
from pyspark.sql import functions as F

# Initiating Spark Session

spark = SparkSession.builder.master("local").appName("DataIngestAndRefine").getOrCreate()


# Reading the configs
config=configparser.ConfigParser()
config.read(r'../projectconfigs/config.ini')
inputLocation=config.get('paths','inputLocation')

#Reading the landing zone files

LandingFileSchema=StructType([
    StructField('Sale_ID',StringType(),True),
    StructField('Product_ID',StringType(),True),
    StructField('Quantity_Sold',IntegerType(),True),
    StructField('Vendor_ID',StringType(),True),
    StructField('Sale_Date',TimestampType(),True),
    StructField('Sale_Amount',DoubleType(),True),
    StructField('Sale_Currency',StringType(),True)
])

#Dataframe defining

landingFileDF=spark.read.schema(LandingFileSchema).\
    option("delimiter","|").\
    csv(inputLocation)
landingFileDF.show()