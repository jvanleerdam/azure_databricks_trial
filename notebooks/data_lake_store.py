# Databricks notebook source
# MAGIC %md # Mount and use Azure Data Lake Store

# COMMAND ----------

import json

# COMMAND ----------

# MAGIC %md ## Credentials

# COMMAND ----------

STORE_URI = 'adl://trialdatastore.azuredatalakestore.net/databricks_trial_data'
MOUNT_POINT = '/mnt/trial_data'
DEMO_DATA_PATH = '/'.join((MOUNT_POINT, 'demo.csv'))
MOUNT_DB_PATH = '/'.join((MOUNT_POINT, 'hive/warehouse/mount_demo.db'))

# COMMAND ----------

# configs = {"dfs.adls.oauth2.access.token.provider.type": "ClientCredential",
#            "dfs.adls.oauth2.client.id": "a1234567-b1234-c123-d123-abcdef123456",
#            "dfs.adls.oauth2.credential": "ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789abcdefghi",
#            "dfs.adls.oauth2.refresh.url": "https://login.microsoftonline.com/abc12345-de12-ab34-de56-123456abcdef/oauth2/token"}

# COMMAND ----------

with open('/dbfs/FileStore/credentials/trial_data_lake_store.json', 'r') as cred_file:
    configs = json.load(cred_file)
print(configs)

# COMMAND ----------

# MAGIC %md ## Mount

# COMMAND ----------

dbutils.fs.ls('/mnt')

# COMMAND ----------

dbutils.fs.mount(source=STORE_URI, mount_point=MOUNT_POINT, extra_configs=configs)

# COMMAND ----------

dbutils.fs.ls(MOUNT_POINT)

# COMMAND ----------

#dbutils.fs.unmount(MOUNT_POINT)

# COMMAND ----------

# MAGIC %md ## Read data

# COMMAND ----------

df = spark.read.csv(DEMO_DATA_PATH, header=True, inferSchema=True)
df.show()

# COMMAND ----------

# MAGIC %md ## Write data

# COMMAND ----------

dbutils.fs.mkdirs(MOUNT_DB_PATH)

# COMMAND ----------

# MAGIC %sql create database if not exists mount_demo location '/mnt/trial_data/hive/warehouse/mount_demo.db'

# COMMAND ----------

spark.catalog.listDatabases()

# COMMAND ----------

df.write.saveAsTable('mount_demo.demo', format='orc', mode='overwrite')

# COMMAND ----------

spark.catalog.listTables('mount_demo')

# COMMAND ----------

# MAGIC %sql select * from mount_demo.demo limit 10