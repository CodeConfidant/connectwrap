import sys, os

sys.path.append(os.path.abspath("connectwrap"))

from database import db; import utils

# Create demo.db database file.
utils.create_database("demo.db")

# Create object representing the demo.db file database.
demo_database = db("demo.db") 

# Create table Crew in the demo.db database file with the desired keys and types as kwargs. 
demo_database.create_table("Crew", crew_id = "int", first_name = "str", last_name = "str", age = "int", position = "str")
 
# Insert rows/tuples of records in the Crew table. 
demo_database.insert_row("Crew", 0, "Jean-Luc", "Picard", 59, "Captain")
demo_database.insert_row("Crew", 1, "William", "Riker", 29, "Commander")
demo_database.insert_row("Crew", 2, "Beverly", "Crusher", 40, "Commander Doctor")
demo_database.insert_row("Crew", 3, "Data", "Soong", 26, "Lieutenant Commander")
demo_database.insert_row("Crew", 4, "Deanna", "Troi", 28, "Lieutenant Commander Counselor")
demo_database.insert_row("Crew", 5, "Geordi", "LaForge", 29, "Lieutenant Junior Grade")
demo_database.insert_row("Crew", 6, "Worf", "Son of Mogh", 24, "Lieutenant Junior Grade")
demo_database.insert_row("Crew", 7, "Wesley", "Crusher", 16, "Ensign")

# Select table names from database and output them to terminal.
demo_database.select_tablenames()

# Select key values from Crew table and output them to terminal. 
demo_database.select_keys("Crew")

# Select row values in Crew table and output them to terminal. 
demo_database.select_table("Crew")

# Select column values by key first_name and output them to terminal. 
demo_database.select_column("Crew", "first_name")

# Select a specific row with the key/value args and output to terminal. 
demo_database.select_row("Crew", "position", "Captain")

input("Press enter to continue:")

# Delete the Crew table. 
demo_database.drop_table("Crew")

# Close the database.
demo_database.close_db()

# Delete demo.db database file.
utils.drop_database("demo.db")

# Delete object.
del(demo_database)