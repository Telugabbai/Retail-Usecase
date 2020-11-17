from pyspark.sql import SparkSession
from src.main.code.myfunctions import read_schema
import configparser
from pyspark.sql import functions as F

# Initiating Spark Session

spark = SparkSession.builder.master("local").appName("DataIngestAndRefine").getOrCreate()


# Reading from the configs
config = configparser.ConfigParser()
config.read(r'../projectconfigs/config.ini')
inputLocation = config.get('paths','inputLocation')
landingFileSchemaFromConf = config.get('Schema','landingFileSchema')

landingFileSchema = read_schema(landingFileSchemaFromConf)

#Reading the landing zone files

# LandingFileSchema=StructType([
#     StructField('Sale_ID',StringType(),True),
#     StructField('Product_ID',StringType(),True),
#     StructField('Quantity_Sold',IntegerType(),True),
#     StructField('Vendor_ID',StringType(),True),
#     StructField('Sale_Date',TimestampType(),True),
#     StructField('Sale_Amount',DoubleType(),True),
#     StructField('Sale_Currency',StringType(),True)
# ])

#Dataframe defining

landingFileDF = spark.read.schema(landingFileSchema).\
    option("delimiter","|").\
    csv(inputLocation)
landingFileDF.show()