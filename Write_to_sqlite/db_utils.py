'''
@author: Ashish Singh
Modified Date: 2021-11-20
'''

# ------------------------------------------------------------------------------------------
# sqlite3: A lightweight library that provides a SQL interface compliant with the DB API 2.0
# specification described by PEP 249 (Python Enhancement Proposals).
#
# csv: The csv module implements classes to read and write tabular data in CSV format.
# ------------------------------------------------------------------------------------------
import sqlite3
from sqlite3 import Error
from sqlite3 import dbapi2 as sqlite
import csv

# ------------------------------------------------------------------------------------------
# To do anything we need to first, establish a connection with the database.
# 
# The create_connection function/method uses the sqlite3 library to create a sqlite 
# connection object (connection class) that represents the database.
#
# The try except block checks if the database file can be opened, otherwise, returns an error
# that the file cannot be opened.
# ------------------------------------------------------------------------------------------
def create_connection(db_file: str) -> object:
    '''
    @param db_file
    A variable of string type/object that holds the file name. 
    
    @return conn
    Returns the sqlite connection object.
    '''
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite.OperationalError as oe:
        print(oe)
        print("Please check the directory path.")
    except Error as e:
        print(e)

    return conn


# ------------------------------------------------------------------------------------------
# The db_get_row_counts function fetches all the rows in a given table and prints only the number of
# rows in the queried table.
# 
# cursor: A cursor object is created to help carry out SQL commands. 
#
# execute: The execute method performs a single SQL statement and throws/raises an error 
# when multiple SQL statements are passed.
#
# fetchall: Fetches all (remaining) rows of a query result, returning a list. 
# An empty list is returned when no rows are available
# ------------------------------------------------------------------------------------------
def db_get_row_counts(conn: object, query: str) -> int:
    '''
    @param conn
    A sqlite connection object.
    
    @param query
    A string variable that holds the query to be executed.
    
    @return len(rows)
    Returns the number of rows available in the given table.
    '''
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()

    # Commenting out the code below. The row length is a good indication
    # of records populated in the table.
    '''
    for row in rows:
        print(row)
    '''
    
    return len(rows)


# ------------------------------------------------------------------------------------------
# The db_get_columnlist function returns a list of columns of the given table.
# 
# cursor: A cursor object is created to help carry out SQL commands. 
#
# execute: The execute method performs a single SQL statement and throws/raises an error 
# when multiple SQL statements are passed.
#
# description: A read-only attribute that provides column names of the query. It returns 
# 7-tuple for each column where the last six items of each tuple are None.
# ------------------------------------------------------------------------------------------
def db_get_columnlist(conn: object, query: str) -> list:
    '''
    @param conn
    A sqlite connection object.
    
    @param query
    A string variable that holds the query to be executed.
    
    @return column_name_list
    Returns a list of the table column/field names.
    '''
    cur = conn.cursor()
    cur.execute(query)
    column_name_list = [tuple[0] for tuple in cur.description]

    return column_name_list


# ------------------------------------------------------------------------------------------
# The db_loadcsv function reads the contents of the csv file and inserts the records in its
# respective database table in sqlite. Once the commands are successfully executed,
# a statement is printed out to show the number of rows inserted in the table.
# The print statement is included in the exec_func function.
#
# open: Function is called to open a csv file for reading. The file will be decoded into 
# unicode using the system default encoding. Three common unicode character encodings are:
# UTF-8, UTF-16, UTF-32.
#
# DictReader: Creates an object that operates like a regular reader but maps the information 
# in each row to a dictionary whose keys are fieldnames.
# 
# fieldnames: Returns a list of fieldnames/columns from the csv file.
#
# executemany: Executes a parameterized SQL command against all parameter sequences or 
# mappings found in the sequence.
#
# commit: Saves the changes made by the executemany function.
# ------------------------------------------------------------------------------------------
def db_loadcsv(conn: object, file_path: str, tbl_name: str):
    '''
    @param conn
    A sqlite connection object.
    
    @param file_path
    A string variable that holds the path of the csv files.
    
    @param tbl_name
    A string variable that holds the name of the table containing particular transactions/activity.
    '''
    # The csv file is opened and the its contents are read and poplated in a dictionary (data type),
    # where the field header (column names) are the dictionary keys.
    csv_file = open(file_path)
    csv_reader = csv.DictReader(csv_file)
    
    # Creates a SQL command based on the acceptable tokens and lexical values in the cursor object.
    insert_sql = 'INSERT INTO ' + tbl_name + ' (' + ','.join(csv_reader.fieldnames) + ') VALUES (' + ','.join(['?'] * len(csv_reader.fieldnames))+ ')'
    
    # The outermost loop of the quadratic loop iterates and reads the contents of 
    # the dictionary (csv_reader) one row at a time.
    #
    # The inner loop iterates through the list of fieldnames/columns and passes
    # the dictionary key (field) to return the dictionary values from csv_reader 
    # and appends the results to row_values; an empty list.
    #
    # Once the inner loop completes one full iteration, the values from the row_values
    # list are added/appended to the "values" list of lists, which is then passed to the 
    # executemany function to insert rows/records in the database table.
    #
    # The commit function executes the SQL command to populate the database table.
    values = []
    for datarow in csv_reader:
        row_values = []
        for field in csv_reader.fieldnames:
            row_values.append(datarow[field])
        values.append(row_values)

    conn.executemany(insert_sql, values)
    
    # Saves/commits the changes.
    conn.commit()
    
    
# ------------------------------------------------------------------------------------------
# Organizes the print statements and function calls involved in loading data into one method. 
# ------------------------------------------------------------------------------------------       
def exe_func(conn: object, file_name: str):
    '''    
    @param conn
    The sqlite connection object.
    
    @param file_name
    A string variable that contains the name of the csv file.
    '''
    # A string variable that holds the name of the table containing particular transactions/activity.
    tbl_name = file_name[0: (file_name[::-1].find("_") + 1) * -1]
    # A string variable that holds the query to be executed.
    query = "Select * From " + tbl_name
    # A string variable that holds the path of the csv files.
    file_path = "../CSV_data/" + file_name 
    
    print("CSV File Name: " + file_name)
    print("SQLite Table Name: " + tbl_name)
    print("List of columns in " + tbl_name + ": " + str(db_get_columnlist(conn, query)))
    db_loadcsv(conn, file_path, tbl_name)
    print("Number of rows inserted in " + tbl_name + ": " + str(db_get_row_counts(conn, query)))
    print()
    

# ------------------------------------------------------------------------------------------
# Deletes records from existing tables and prints the row count of the table.
# ------------------------------------------------------------------------------------------    
def del_records(conn: object, file_name: str):
    '''
    @param conn
    A sqlite connection object.
    
    @param file_name
    A string variable that contains the name of the csv file.
    '''
    # A string variable that holds the name of the table containing particular transactions/activity.
    tbl_name = file_name[0: (file_name[::-1].find("_") + 1) * -1]
    # A string variable that holds the query to be executed.
    query = "Delete From " + tbl_name
    
    conn.execute(query)
    print("Current row counts in " + tbl_name + ": " + str(db_get_row_counts(conn, query)))
