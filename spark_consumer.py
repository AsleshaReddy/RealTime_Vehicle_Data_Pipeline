from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StringType, FloatType, DoubleType

spark = SparkSession.builder     .appName("VehicleDataConsumer")     .getOrCreate()

schema = StructType()     .add("vehicle_id", StringType())     .add("speed", FloatType())     .add("fuel_level", FloatType())     .add("engine_temp", FloatType())     .add("timestamp", DoubleType())

df = spark.readStream     .format("kafka")     .option("kafka.bootstrap.servers", "localhost:9092")     .option("subscribe", "vehicle_data")     .load()

df_parsed = df.selectExpr("CAST(value AS STRING)")     .select(from_json(col("value"), schema).alias("data"))     .select("data.*")

query = df_parsed.writeStream     .outputMode("append")     .format("console")     .start()

query.awaitTermination()
