#!/usr/bin/env python3

import sys, os

sys.path.append(os.path.abspath("connectwrap"))

from connectwrap import db; import utils

# Create demo.db database file.
utils.create_database("demo.db")

# Create object representing the demo.db file database and Crew table.
demo_database = db("demo.db", "Crew") 

# Create table Crew in the demo.db database file with the desired keys and types as kwargs. 
demo_database.create_table("Crew", crew_id = "int", first_name = "str", last_name = "str", age = "int", position = "str")
 
# Insert rows/tuples of records in the Crew table. 
demo_database.insert_row(0, "Jean-Luc", "Picard", 59, "Captain")
demo_database.insert_row(1, "William", "Riker", 29, "Commander")
demo_database.insert_row(2, "Beverly", "Crusher", 40, "Commander Doctor")
demo_database.insert_row(3, "Data", "Soong", 26, "Lieutenant Commander")
demo_database.insert_row(4, "Deanna", "Troi", 28, "Lieutenant Commander Counselor")
demo_database.insert_row(5, "Geordi", "LaForge", 29, "Lieutenant Junior Grade")
demo_database.insert_row(6, "Worf", "Son of Mogh", 24, "Lieutenant Junior Grade")
demo_database.insert_row(7, "Wesley", "Crusher", 16, "Ensign")

# Select table names from database and output them to terminal.
demo_database.select_tablenames()

# Select key values from Crew table and output them to terminal. 
demo_database.select_keys()

# Update columns from rows based on desired criteria. 
demo_database.update_row("position", "Lieutenant", "crew_id", 5)

# Select a specific row with key/value args and delete.
demo_database.drop_row("first_name", "Wesley")

# Select row values in Crew table and output them to terminal. 
demo_database.select_table()

# Select column values by key first_name and output them to terminal. 
demo_database.select_column("first_name")

# Select a specific row with the key/value args and output to terminal. 
demo_database.select_row("position", "Captain")

input("Press enter to continue:")

# Delete the Crew table. 
demo_database.drop_table("Crew")

# Close the database.
demo_database.close_db()

# Delete demo.db database file.
utils.drop_database("demo.db")