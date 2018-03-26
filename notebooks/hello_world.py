# Databricks notebook source
# MAGIC %md # Hello, world!

# COMMAND ----------

print('Hello, world!')

# COMMAND ----------

# MAGIC %scala println("Hello, world!")

# COMMAND ----------

# MAGIC %sh ls -l && echo "Hello, world!"

# COMMAND ----------

import sys
print(sys.version)

# COMMAND ----------

import pyspark
print(pyspark.__version__)

# COMMAND ----------

print(sc)

# COMMAND ----------

print(spark)

# COMMAND ----------

df = spark.createDataFrame([(0, 'Hello'), (1, ','), (2, 'world'), (3, '!')], schema=('index', 'text'))
df.orderBy('index').show()