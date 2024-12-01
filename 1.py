from pyspark.sql import SparkSession
from pyspark.sql.functions import sum

# Initialize SparkSession
spark = SparkSession.builder \
.appName("Pivot Table Example") \
.getOrCreate()

# Sample Sales Data
data = [
 ("John", "Electronics", "2023-01", 4500),
 ("Jane", "Clothing", "2023-01", 7500),
 ("Sam", "Grocery", "2023-01", 3000),
 ("Alice", "Electronics", "2023-02", 9000),
 ("Bob", "Clothing", "2023-02", 1200),
 ("Jane", "Grocery", "2023-02", 5500),
 ("John", "Clothing", "2023-03", 8500),
 ("Alice", "Electronics", "2023-03", 4000),
 ("Sam", "Grocery", "2023-03", 1000)
]
columns = ["name", "category", "month", "sales"]

# Create DataFrame
df = spark.createDataFrame(data, schema=columns)

# Create a Pivot Table
pivot_table = df.groupBy("month") \
 .pivot("category") \
 .agg(sum("sales"))

# Show the Result
pivot_table.show()