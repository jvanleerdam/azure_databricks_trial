# Databricks notebook source
# MAGIC %sh echo $USER

# COMMAND ----------

# MAGIC %sh pwd

# COMMAND ----------

# MAGIC %sh ls -l

# COMMAND ----------

# MAGIC %sh ls -l /

# COMMAND ----------

#%sh echo 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDaE8NHhemEbx9fs1FL1XKdRgOLj+qKBjZMXM9Ajtq6iJK68K4JXarEpPbN75zPnS7AZipirKlqNJvfbTn3Txd4sMuR0314NeZG2mTtSEG4AXG2iIyq8NZ9dbLAj8HCvsEDfDQKGFyBi9I5Z3tWglp7Tok2mWOI9kKQvhJVwGcCPRwH8tUJrZh+d99Cwf98GHT3Xo5Sn7YSwGPZL2/OQGvQF24yjPYm6xqFG77QsXXvd1auIx30qnUFfG9KCb+sShCNmkYb0fECcFZ4YRE/OYQ6wGdnEgufdPeaNiqvsVbpm20/2VUSbsQRTQsAnGDr4NAYnwB/ErY4d6cqpxKlGSoHByE0B3KgViMMzgCFBxPenNMherEMHTH3gax1Yyn9pwu5GMc1b/yzzgJSaRvcUJ3mDrr8FcIjNhK0ym6qqrJCAcjAeXZprM0IHbrW/TlhskV/gIKDl5KMCcaOpBxuGzrHN+zpAAliG51mQvru1mnKJQEmVu5umDMwZQ9sgWPSBvGAqJVSumXuntnBAvCRgIv/IDigxmqdZqgAToaLI4lbAGgcA8v7/mYZOwx3bvBBUNBj5y33W4y1HkM4MzAtm/5kYWk7U1hfzyaJVPlWwhUx5+GpnX7Wv8/5SiyG1zQYk0/K4U9gq+hcnH+G/EBGvOtHDIZhaFCjAxJccTd/zPfvjQ== j.van.leerdam@gmail.com' >> /home/ubuntu/.ssh/authorized_keys

# COMMAND ----------

# MAGIC %sh cat /home/ubuntu/.ssh/authorized_keys

# COMMAND ----------

# MAGIC %sh ls /.dockerenv

# COMMAND ----------

# MAGIC %sh cat /var/run/container_type

# COMMAND ----------

# MAGIC %sh env | grep 'HIVE'

# COMMAND ----------

# MAGIC %sh df -h

# COMMAND ----------

# MAGIC %sh ls -al /local_disk0/

# COMMAND ----------

# MAGIC %sh git --version

# COMMAND ----------

# MAGIC %sh ls -al /dbfs/user/eskapade

# COMMAND ----------

dbutils.fs.ls('/')

# COMMAND ----------

vdbutils.fs.ls('/')

# COMMAND ----------

dbutils.fs.ls('/FileStore/')