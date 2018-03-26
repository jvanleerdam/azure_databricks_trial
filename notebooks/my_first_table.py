# Databricks notebook source
# MAGIC %md ## SQL table

# COMMAND ----------

# MAGIC %sql show tables

# COMMAND ----------

# MAGIC %sql select count(*) from demo_csv

# COMMAND ----------

# MAGIC %sql select * from demo_csv limit 10

# COMMAND ----------

# MAGIC %md ## Spark CSV

# COMMAND ----------

df = spark.read.csv('dbfs:/FileStore/tables/demo.csv', header=True, inferSchema=True)
print(df.schema)

# COMMAND ----------

df.count()

# COMMAND ----------

df.show(10)

# COMMAND ----------

# MAGIC %md ## Spark table

# COMMAND ----------

tab = spark.read.table('demo_csv')
print(tab.schema)

# COMMAND ----------

tab.count()

# COMMAND ----------

tab.show(10)