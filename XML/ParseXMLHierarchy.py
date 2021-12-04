"""
@author: Ashish Singh
Created on: 2021-07-24

This script helps parse the hierarchy in an XML file. 
"""

# Library Info:
# https://docs.python.org/3/library/xml.etree.elementtree.html#module-xml.etree.ElementTree

import xml.etree.ElementTree as et
import xml.etree.ElementPath as ep
from inspect import getmembers, isclass, isfunction


# ------------------------------------------------------------------ #
# Reads the file path and checks for input error.                    #
# ------------------------------------------------------------------ #

def readfile() -> str:
    """
    Reads the file and checks if the file location has error.
    """
    abs_path = input("Enter the filepath here: ")

    filereaderror = file_error(abs_path)

    while filereaderror == True:
        abs_path = input("Enter the filepath here: ")
        filereaderror = file_error(abs_path)

    return abs_path

def file_error(abs_path: str) -> bool:
    """
    Returns true if the file path has error, else, returns false.
    """
    try:
        open(abs_path, 'r')
        return False
    except FileNotFoundError:
        return True

# ------------------------------------------------------------------ #
# Reads elements of the XML file.                                    #
# ------------------------------------------------------------------ #
def main():
    abs_path = readfile()
    # ElementTree class represents the whole XML document as a tree.
    tree = et.parse(abs_path)
    root = tree.getroot()

    for elem in root.findall('.//Period'):
        print(elem.tag)



# Executes main method.
if __name__ == '__main__':
    main()