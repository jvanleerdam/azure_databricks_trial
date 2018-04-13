# Databricks notebook source
# MAGIC %md # Atlas Higgs analysis

# COMMAND ----------

import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import pyspark.sql.functions as sql_funcs

# COMMAND ----------

# MAGIC %matplotlib inline

# COMMAND ----------

# MAGIC %md ## Read input data

# COMMAND ----------

df = spark.read.csv('/databricks-datasets/atlas_higgs/atlas_higgs.csv', sep=',', header=True, inferSchema=True)
df.show()

# COMMAND ----------

df.count()

# COMMAND ----------

df.select('EventId', 'DER_mass_MMC', 'Weight', 'Label').show()

# COMMAND ----------

df.groupBy('Label').agg(sql_funcs.count('*').alias('count'),
                        sql_funcs.min('Weight').alias('min_weight'),
                        sql_funcs.max('Weight').alias('max_weight'),
                        sql_funcs.mean('Weight').alias('mean_weight')).show()

# COMMAND ----------

# MAGIC %md ## Extract masses

# COMMAND ----------

mass = df.filter((df['Label'] == 's') & (df['DER_mass_MMC'] > 50.) & (df['DER_mass_MMC'] < 250.)).select('DER_mass_MMC')
mass.show(5)

# COMMAND ----------

mass_arr = np.array([m[0] for m in mass.collect()])
mass_arr

# COMMAND ----------

# MAGIC %md ## Plot masses

# COMMAND ----------

mass.registerTempTable('mass')

# COMMAND ----------

# MAGIC %sql select * from mass

# COMMAND ----------

fig = plt.figure(figsize=(8, 5))
hist = plt.hist(mass_arr, bins=100)
plt.xlabel('Mass [GeV]')
display(fig)