from pyspark.sql.types import StringType,StructType,StructField,IntegerType,DoubleType,TimestampType


# All necessary functions
def read_schema(schema_arg):
    d_types = {
        "StringType()": StringType(),
        "IntegerType()": IntegerType(),
        "DoubleType()": DoubleType(),
        "TimestampType()": TimestampType()
    }
    split_values = schema_arg.split(",")
    sch=StructType()

    for i in split_values:
        x = i.split(" ")
        sch.add(x[0], d_types[x[1]], True)
    return sch

