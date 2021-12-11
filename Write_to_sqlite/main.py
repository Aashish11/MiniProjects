'''
@author: Ashish Singh
Modified Date: 2021-11-20
'''

from sqlite3.dbapi2 import Error
import db_utils as db
import os 
    
# ------------------------------------------------------------------------------------------
# The main method executes the following actions:
# 1) Checks the CSV directory for error.
# 2) Reads all the csv files from the selected directory and stores them in a list.
# 3) Calls the create_connection function from the db_utils module to create a sqlite 
#    connection object.
# 4) Iterates a loop to delete all records from existing table structures by calling the 
#    the del_records function. If the table doesn't exist, prints the error message on the screen.
# 5) Iterates a loop to populate records in the sqlite tables by calling the exec_func function.
#    If there are any issues with the operation, prints the error message on the screen.
# ------------------------------------------------------------------------------------------
def main():    
    try:
        csv_dir = "../CSV_data"   
    except FileNotFoundError as e:
        print(e)
        print("Please check the directory path.")
        
    # Creates a list of files in the csv directory.
    csv_files_list = os.listdir(csv_dir) 
    # Calls the function from db_utils to establish a connection with the database
    # (create a new connection object).
    db_dir = "../Database/ibotta.db"  
    conn = db.create_connection(db_dir)
    
    # Iterates through the files in the csv file list.
    # And deletes records form the existing tables.
    for file_name in csv_files_list:
        try:
            db.del_records(conn, file_name)
        except Error as e:
            print(e)
    print() 
        
    # Iterates through the files in the csv file list.  
    # And populates records in the database tables.  
    for file_name in csv_files_list:   
        try:
            db.exe_func(conn, file_name)
        except Error as e:
            print(e)               
    

# ------------------------------------------------------------------------------------------
# Main executable code.
# ------------------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
