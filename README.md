# ***connectwrap***

    A Python package built on top of the sqlite3 module made specifically for SQLite database file management.

## ***Module database, Class db***

<table width="100%">
	<tr>
		<th align="left">
            Attribute/Exception/Method
        </th>
		<th align="left">
            Description
        </th>
	</tr>
	<tr>
		<td>
            <code>db_filepath</code>
        </td>
		<td>
            Attribute of the string type representing the database file path. <br/>
            The file must have a .db, .sqlite, or .sqlite3 extension. <br/>
            This is the only attribute needed for the object's argument. The other attributes are generated from this.
        </td>
	</tr>
    <tr>
		<td>
            <code>connection</code>
        </td>
		<td>
            Attribute of the Connection type from the sqlite3 module representing the database connection. Used to commit changes to database.
        </td>
	</tr>
    <tr>
		<td>
            <code>connection_cursor</code>
        </td>
		<td>
            Attribute of the Cursor type from the sqlite3 module representing the database connection cursor. Used to execute queries.
        </td>
	</tr>
    <tr>
		<td>
            <code>connection_status</code>
        </td>
		<td>
            Attribute of the bool type representing whether the Database connection is opened or closed. <br/>
            Set to True upon the creation of a new Database object. <br/>
            Opened = True <br/>
            Closed = False
        </td>
	</tr>
    <tr>
		<td>
            <code>TableNotFoundError</code>
        </td>
		<td>
            Custom exception to raise when an argument table doesn't exist in a database.
        </td>
	</tr>
    <tr>
		<td>
            <code>TableExistsError</code>
        </td>
		<td>
            Custom exception to raise when an argument table already exists in a database.
        </td>
	</tr>
    <tr>
		<td>
            <code>close_db()</code>
        </td>
		<td>
            Close database connection.
        </td>
	</tr>
    <tr>
		<td>
            <code>open_db()</code>
        </td>
		<td>
            Open database connection. Reset the cursor.
        </td>
	</tr>
    <tr>
		<td>
            <code>set_db_filepath(db_filepath)</code>
        </td>
		<td>
            Change the db_filepath attribute value. <br/>
            The file must have a .db, .sqlite, or .sqlite3 extension. <br/>
            This allows you to switch between file databases while only creating one object. <br/>
            Works on open or closed databases. The result of this method will be an open Database using the db_filepath argument as the new Database file path.
        </td>
	</tr>
    <tr>
		<td>
            <code>get_connection_status()</code>
        </td>
		<td>
            Return the connection_status attribute representing whether the Database connection is open or closed. <br/>
            Opened = True <br/>
            Closed = False
        </td>
	</tr>
    <tr>
		<td>
            <code>get_db_filepath()</code>
        </td>
		<td>
            Return the db_filepath attribute value representing the database file path.
        </td>
	</tr>
    <tr>
		<td>
            <code>get_table_name()</code>
        </td>
		<td>
            Select and return the table names within a database as strings in a list.
        </td>
	</tr>
    <tr>
		<td>
            <code>get_keys(db_table)</code>
        </td>
		<td>
            Select and return the key names within a table as strings in a list.
        </td>
	</tr>
    <tr>
		<td>
            <code>get_column(db_table, key)</code>
        </td>
		<td>
            Select and return a list of the values in a column based on the key from that column.
        </td>
	</tr>
    <tr>
		<td>
            <code>get_row(db_table, key, value)</code>
        </td>
		<td>
            Select and return a dictionary representing a row in the database table where the key and value arguments match a row column key and value pair. <br/>
            Only returns the first row with the occurance of the key/value argument pair. <br/>
            Returns None if there's no occurance of the key/value argument in any row in the table. <br/>
            The key argument must be a string and a key within the table. <br/>
            The value argument must be one of the following types - int, float, str, bytes, None. <br/>
            Use a key with a unique value for best results.
        </td>
	</tr>
    <tr>
		<td>
            <code>get_table(db_table)</code>
        </td>
		<td>
            Select and return a list of dictionaries with each dictionary representing a row in a table.
        </td>
	</tr>
    <tr>
		<td>
            <code>drop_table(db_table)</code>
        </td>
		<td>
            Drop/delete table in the file database.
        </td>
	</tr>
    <tr>
		<td>
            <code>create_table(db_table, **kwargs)</code>
        </td>
		<td>
            Create table within the file database. <br/>
            The key in each kwargs entry denotes the key name of a column. <br/>
            The value in each kwargs entry denotes the data type of a column. <br/> 
            The value in each kwargs entry must be one of the following strings - 'int', 'float', 'str', 'bytes', 'None'.
        </td>
	</tr>
    <tr>
		<td>
            <code>select_table_name()</code>
        </td>
		<td>
            Select and output to terminal the table names within a database.
        </td>
	</tr>
    <tr>
		<td>
            <code>select_table(db_table)</code>
        </td>
		<td>
            Select and output to terminal the rows as dictionaries from a table.
        </td>
	</tr>
    <tr>
		<td>
            <code>select_column(db_table, *args)</code>
        </td>
		<td>
             Select and output to terminal the values from keys within a table. <br/> Each arg in *args arguments must be strings containing key names within the table.
        </td>
	</tr>
    <tr>
		<td>
            <code>select_keys(db_table)</code>
        </td>
		<td>
            Select and output to terminal the key names within a table.
        </td>
	</tr>
    <tr>
		<td>
            <code>select_row(db_table, key, value)</code>
        </td>
		<td>
            Select and output to terminal a row of a table in a database. <br/>  
            Only outputs the first row with the occurance of the key/value argument pair. <br/>
            Outputs None if there's no occurance of the key/value argument in any row in the table. <br/>
            The key argument must be a string and a key within the table. <br/>
            The value argument must be one of the following types - int, float, str, bytes, None. <br/>
            Use a key with a unique value for best results.
        </td>
	</tr>
    <tr>
		<td>
            <code>insert_row(db_table, *args)</code>
        </td>
		<td>
            Insert row of data into table. <br/>
            Each arg in *args must be one of the following types - int, float, str, bytes, None.
        </td>
	</tr>
    <tr>
		<td>
            <code>key_exists(db_table, key)</code>
        </td>
		<td>
            Return True if the key argument exists in a table.
        </td>
	</tr>
    <tr>
		<td>
            <code>table_exists(db_table)</code>
        </td>
		<td>
            Return True if the db_table argument is a table name within the database.
        </td>
	</tr>
</table>

## ***Module utils***

<table width="100%">
	<tr>
		<th align="left">
            Method
        </th>
		<th align="left">
            Description
        </th>
	</tr>
    <tr>
		<td>
            <code>drop_database(db_filepath)</code>
        </td>
		<td>
            Drop/delete .db, .sqlite, or .sqlite3 file database.
        </td>
	</tr>
    <tr>
		<td>
            <code>create_database(db_filepath)</code>
        </td>
		<td>
            Create .db, .sqlite, or .sqlite3 file database.
        </td>
	</tr>
    <tr>
		<td>
            <code>ishex(arg)</code>
        </td>
		<td>
            Return True if all characters in arg string are hexadecimal.
        </td>
	</tr>
    <tr>
		<td>
            <code>isfloat(arg)</code>
        </td>
		<td>
            Return True if arg string characters constitute a float.
        </td>
	</tr>
    <tr>
		<td>
            <code>isdb(db_filepath)</code>
        </td>
		<td>
            Return True if db_filepath argument has one of the follow extensions: .db, .sqlite, or .sqlite3
        </td>
	</tr>
</table>

## ***Data Types Comparison***

<table width="100%">
	<tr>
		<th align="left">
            Python
        </th>
		<th align="left">
            SQLite
        </th>
	</tr>
	<tr>
		<td>
            None
        </td>
		<td>
            NULL
        </td>
	</tr>
    <tr>
		<td>
            int
        </td>
		<td>
            INTEGER
        </td>
	</tr>
    <tr>
		<td>
            float
        </td>
		<td>
            REAL
        </td>
	</tr>
    <tr>
		<td>
            str
        </td>
		<td>
            TEXT
        </td>
	</tr>
    <tr>
		<td>
            bytes
        </td>
		<td>
            BLOB
        </td>
	</tr>
</table>

[Back to Top](#connectwrap)

---
