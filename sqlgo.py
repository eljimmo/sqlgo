import sqlite3
import csv
from prettytable import from_db_cursor
import os

table_name = ""
def database_info(tab_name):
    global table_name
    table_name = tab_name
  
conn = sqlite3.connect("cars.db")
c = conn.cursor()

#.display functions
def display_that(column_name, value):
    os.system("clear")
    c.execute(f"SELECT * FROM {table_name} WHERE {column_name} {value}")
    line = from_db_cursor(c)
    print(line)
    conn.commit()


def display_all():
    os.system("clear")
    c.execute(f"SELECT * FROM {table_name}")
    table = from_db_cursor(c)
    print(table)
    conn.commit()

#.insert function
def insert_csv(filename):
    test_file = open(filename)
    rows = csv.reader(test_file)
    c.executemany(f"INSERT INTO {table_name} VALUES (?, ?, ?, ?, ?, ?, ?)", rows)
    conn.commit()


def insert_standard(car_id1, speed1, brand1, model1, year1, mileage1, price1):
    c.execute(f"""INSERT INTO {table_name} (car_id, speed, brand, model, year, mileage, price) VALUES ({car_id1}, {speed1}, '{brand1}', '{model1}', {year1}, {mileage1}, {price1});""")
    conn.commit()

#.modify function
def modify(column_name, value, car_id):
    c.execute(f"UPDATE {table_name} SET {column_name} = {value} WHERE car_id = {car_id};")
    conn.commit()

#.delete function
def delete(car_id):
    c.execute(f"DELETE FROM {table_name} WHERE car_id = {car_id}")
    conn.commit()

#.end function
def end():
    conn.close()
