# File Database

This script allows saving files to a SQLite database table and retrieving them. Useful for storing binary file content in a structured queryable database.

## Usage

The main.py script has the overall workflow. Key functions:

- `create_connection()`: Connect to the SQLite database file
- `create_table()`: Create the table to hold file data
- `insert_file()`: Add a new file record to the database  
- `retrieve_file()`: Fetch file from database and save to output

The table stores these fields for each file:

- id - primary key 
- filename - original file name
- filehash - md5 hash of file contents  
- file - the binary file data as a BLOB

## Running 

To save and retrieve a file:

```
python main.py
```

This will:

1. Connect to the database file (myfiledb.db)
2. Create the files table if not exists
3. Insert the sample file into table 
4. Retrieve file from table and save to output folder

The output folder will hold the exported file.

## Configuration

The DB_FILE constant defines the database filename. New files to add are specified in the insert_file() function.

## Dependencies

- sqlite3
- os
- hashlib

Happy Coding! 🕶️
