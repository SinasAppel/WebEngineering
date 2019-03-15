import json
import sqlite3
conn = sqlite3.connect('/home/jur/Documents/WebEngineering/airapi/db.sqlite3')
c = conn.cursor()
id_number = 0
json_data = open('airlines.json')
data = json.load(json_data)
table_name = 'airports_airport'

for d in data:
    id_number = id_number + 1
    airport_name = d['airport']['name']
    airport_code = d['airport']['code']
    c.execute("INSERT INTO airports_airport "
              "VALUES (?, ?, ?)", (id_number, airport_name, airport_code))

conn.commit()
conn.close()
