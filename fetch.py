import sqlite3
import pandas as pd

conn = sqlite3.connect('playoffs.db')
cursor = conn.cursor()

query = """
    SELECT *
    FROM teams
"""
cursor.execute(query)
records = cursor.fetchall()
conn.close()

#Printing all the records
#print(records)

#printing all the records in a list
#records_df = pd.DataFrame(records,columns = ["id", "City", "Name"])
#print(records_df)

#cities = []
#for record in records:
  #cities.append(record[1])
#print(cities)


#length_cities = []
#for record in records:
   #length_cities.append(len(record[1]))
#print(length_cities)


length_cityName = []
for record in records:
    length_cityName.append(len(record[1]))
    length_cityName.append(len(record[2]))
print(length_cityName)