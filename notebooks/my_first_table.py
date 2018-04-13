# Databricks notebook source
# MAGIC %md ## SQL

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

spark.catalog.listDatabases()

# COMMAND ----------

spark.catalog.listTables()

# COMMAND ----------

tab = spark.read.table('demo_csv')
print(tab.schema)

# COMMAND ----------

tab.count()

# COMMAND ----------

tab.show(10)

# COMMAND ----------

tab.write.saveAsTable('demo_orc', format='orc', mode='overwrite')

# COMMAND ----------

# MAGIC %sql describe formatted demo_orc

# COMMAND ----------

# MAGIC %md ## Custom database location

# COMMAND ----------

dbutils.fs.mkdirs('/user/jleerdam/warehouse')

# COMMAND ----------

# MAGIC %sql create database if not exists test location '/user/jleerdam/warehouse/test.db'

# COMMAND ----------

tab.write.saveAsTable('test.demo_orc', format='orc', mode='overwrite')

# COMMAND ----------

dbutils.fs.ls('/user/jleerdam/warehouse/test.db/demo_orc')