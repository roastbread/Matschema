import pandas as pd
import sqlite3 as sl

sqliteConnection = sl.connect('matschema.db')
cursor = sqliteConnection.cursor()
print('DB Init')

meal_table = """CREATE TABLE MEALTABLE (
    ID INTEGER NOT NULL,
    NAME TEXT NOT NULL,
    CUISINE TEXT,
    PRIMARY KEY (ID,NAME)
);
"""

ingredient_table = """CREATE TABLE INGREDIENTS (
    ID INTEGER NOT NULL,
    NAME TEXT NOT NULL,
    CLASS TEXT NOT NULL,
    CALORIES REAL,
    PRICE REAL,
    PRIMARY KEY (ID,NAME)
);
"""

junc_table = """CREATE TABLE MEAL_INGREDIENT_JUNCTION(
    MealID INTEGER,
    IngredientID INTEGER,
    MealNAME TEXT,
    IngredientNAME TEXT,
    PRIMARY KEY (MealID, IngredientID, MealNAME, IngredientNAME)
    FOREIGN KEY (MealID)
        REFERENCES MEALTABLE (ID),
    FOREIGN KEY (IngredientID)
        REFERENCES INGREDIENTS (ID),
    FOREIGN KEY (MealNAME)
        REFERENCES MEALTABLE (NAME),
    FOREIGN KEY (IngredientNAME)
        REFERENCES INGREDIENTS (NAME)
);
"""

cursor.execute(meal_table)
cursor.execute(ingredient_table)
cursor.execute(junc_table)
pizza = {'name': 'Pizza', 'ingredients': ['mjöl', 'jäst', 'krossade tomater', 'mozzarella', 'salami', 'svamp']}


#new_meal = input('Skriv in måltid:')
#print(new_meal)
#ingredients = [input('Skriv in ingredienser:')]
#print(ingredients)
