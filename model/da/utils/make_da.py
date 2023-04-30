import mysql.connector

schema = mysql.connector.connect(
    host="localhost",
    user="root",
    password="saina13831383"
)

cursor = schema.cursor()

# Create Database
cursor.execute("CREATE DATABASE project_mft")

cursor.execute("CREATE TABLE project_mft.costumer_tbl "
               "(code int auto_increment primary key, "
               "costumer_name nvarchar(30),"
               "costumer_family nvarchar(30),"
               "costumer_birth_date date,"
               "costumer_active tinyint)")

cursor.execute("CREATE TABLE project_mft.user_tbl "
               "(code int auto_increment primary key, "
               "user_username nvarchar(20) NOT NULL UNIQUE,"
               "user_password nvarchar(20) NOT NULL,"
               "user_costumer_code int UNIQUE,"
               "user_active tinyint)")

cursor.execute("CREATE TABLE project_mft.device_tbl "
               "(code int auto_increment primary key, "
               "device_name nvarchar(20),"
               "device_model nvarchar(20),"
               "device_count int,"
               "device_available tinyint)")

cursor.execute("CREATE TABLE project_mft.sell_tbl "
               "(code int auto_increment primary key, "
               "costumer_code int NOT NULL,"
               "device_code int NOT NULL,"               
               "sell_price int,"
               "sell_count int,"
               "sell_date date,"
               "FOREIGN KEY (costumer_code) REFERENCES project_mft.costumer_tbl(code),"
               "FOREIGN KEY (device_code) REFERENCES project_mft.device_tbl(code))")

cursor.close()
schema.close()