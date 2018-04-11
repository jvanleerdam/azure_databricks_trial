# Databricks notebook source
from eskapade import process_manager, ConfigObject, DataStore
from eskapade import resources
from eskapade.core import execution
from eskapade.logger import LogLevel

# COMMAND ----------

settings = process_manager.service(ConfigObject)
settings['macro'] = resources.tutorial('esk104_basic_datastore_operations.py')
settings['version'] = 0
settings['logLevel'] = LogLevel.INFO

# COMMAND ----------

execution.reset_eskapade(skip_config=True)
execution.eskapade_run(settings)

# COMMAND ----------

ds = process_manager.service(DataStore)
ds