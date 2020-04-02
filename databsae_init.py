import sqlite3 as lite
import sys

# create table 
con = lite.connect('testDatabase.db')
with con: 
    cur = con.cursor() 
    cur.execute("DROP TABLE IF EXISTS DIST_data")
    cur.execute("CREATE TABLE DIST_data(timestamp DATETIME, dist NUMERIC)")
    cur.execute("DROP TABLE IF EXISTS MQ3_data")
    cur.execute("CREATE TABLE MQ3_data(timestamp DATETIME, MQ3 NUMERIC)")
    cur.execute("DROP TABLE IF EXISTS MQ5_data")
    cur.execute("CREATE TABLE MQ5_data(timestamp DATETIME, MQ5 NUMERIC)")
    cur.execute("DROP TABLE IF EXISTS MQ8_data")
    cur.execute("CREATE TABLE MQ8_data(timestamp DATETIME, MQ8 NUMERIC)")
    
con.commit()

# # insert data
# con = lite.connect('testDatabase.db')
# with con:
#     cur = con.cursor() 
#     cur.execute("INSERT INTO DHT_data VALUES(datetime('now'), 20.5, 30, 3)")
#     cur.execute("INSERT INTO DHT_data VALUES(datetime('now'), 25.8, 40, 4)")
#     cur.execute("INSERT INTO DHT_data VALUES(datetime('now'), 30.3, 50, 5)")
#     cur.execute("INSERT INTO DHT_data VALUES(datetime('now'), 30.3, 50, 6)")