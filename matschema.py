import pandas as pd
import sqlite3 as sl

sqliteConnection = sl.connect('matschema.db')
cursor = sqliteConnection.cursor()
print('DB Init')

meal_table = """CREATE TABLE MEALTABLE (
    ID INTEGER NOT NULL,
    NAME TEXT NOT NULL,
    PRIMARY KEY (ID,NAME),
    


"""


pizza = {'name': 'Pizza', 'ingredients': ['mjöl', 'jäst', 'krossade tomater', 'mozzarella', 'salami', 'svamp']}


#new_meal = input('Skriv in måltid:')
#print(new_meal)
#ingredients = [input('Skriv in ingredienser:')]
#print(ingredients)