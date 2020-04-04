import os

# Drop/delete .db file database.
def drop_database(db_filepath):
    if (type(db_filepath) is not str):
        raise TypeError("The db_filepath argument isn't a string!")

    if (os.path.exists(db_filepath) == False):
        raise FileNotFoundError("The file that the db_filepath argument represents doesn't exist!")

    if (db_filepath.endswith(".db") == False):
        raise ValueError("The db_filepath argument doesn't have extension .db!")
        
    print("Deleting Database:", db_filepath)
    os.remove(db_filepath)
    print("Deletion Success:", db_filepath, "Deleted!")

# Create .db file database. 
def create_database(db_filepath):
    if (type(db_filepath) is not str):
        raise TypeError("The db_filepath argument isn't a string!")

    if (os.path.exists(db_filepath) == True):
        raise FileExistsError("A file with that name already exists!")
        
    if (db_filepath.endswith(".db") == False):
        raise ValueError("The db_filepath argument doesn't have extension .db!")
        
    print("Creating Database:", db_filepath)
    new_db = open(db_filepath, "xb"); new_db.close()
    print("Creation Success:", db_filepath, "Created!")

# Return true if all characters in arg string are hexadecimal.
def ishex(arg):
    if (type(arg) is not str):
        raise TypeError("The arg argument isn't a string!")
        
    hex_digits = str("0123456789abcdef")

    for digit in arg.replace(' ', '').lower():
        if not (digit in hex_digits):
            return False

    return True

# Return true if arg string characters constitute a float. 
def isfloat(arg):
    if (type(arg) is not str):
        raise TypeError("The arg argument isn't a string!")

    if (arg.replace('.', '', 1).isdigit() == True):
        return True
    else:
        return False