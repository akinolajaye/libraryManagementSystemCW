#This Programme was written by Jayeola Akinola on 1st December 2020 - 7th December 2020

import datetime
import tkinter as tk
from tkinter import messagebox as mbx
import re

def readDatabase(filename):
    """
    converts data from the text database file 
    into a dictionary that can be interpreted
    byt the python program
    """
    database={}
    file=open(filename,"r+") #Opens the text file in python
    line_length=len(file.readlines())#count the num of lines in the txt file
    file.seek(0)

    data_str=file.readline() # reads the first line of the txt file
    data_str=data_str.strip("\n") #removes leading and trailing white space
    data_elements=data_str.split(",") # converts the text into a list 

    
    
    """
    this for loop  goes through the text file and puts
    each line of text from the txt file(data record) into a 
    dictionary where element is the key and field is the value
    eg: data record={date element: data field} = {Title : Book 1}
    this is then put into another dictionary where the key is the id
    and the value is the data record eg: {1 : {Title: Book1}...}
    """

    if line_length-1 !=0:
        for i in range(line_length-1):#loop on the amount of records in txt
            data_record={} #empty dict to store current data record
            data_str=file.readline()#retrieves the data field from txt file

            data_str=data_str.strip("\n")
            data_field=data_str.split(",")

            for j in range(len(data_elements)):#loop on num of data elements
                data_record[data_elements[j]]= data_field[j] 

            database[(i+1)]=data_record

        file.close()

    else:
            file.close()
    
    if __name__ == "__main__":
        for i in range(len(database)):
            print(database[i+1])
            
    
    return database



def writeDatabase(database,filename):
    """
    this is a function the write all data from the
    dictionary to the txt file. this is used for updating
    the database regularly
    """

    file=open(filename,"r+") #Opens the text file in python

    data_str=file.readline() # reads the first line of the txt file
    data_str=data_str.strip("\n") #removes leading and trailing white space
    data_elements=data_str.split(",") # converts the text into a list 
    data_elements=",".join(data_elements)#formats the data to a string
    file.close()

    file=open(filename,"w+")
    file.write(data_elements+"\n")#writes the data to the file

    for i in range(len(database)):#loops through all records
        data_str=list(database[i+1].values())
        data_str=",".join(data_str)

        file.write(data_str+"\n")
    file.close()

def getDate():
    """
    gets the current date
    """
    date=str(datetime.date.today())

    if __name__ == "__main__":
        print(date)

    return date

def IdExists(id,table):
    """
    This is a function to check if the isbn entered
    exists within the database, return true if 
    it does and false if it doesnt
    """
    count =1#count starts as 1 as 1st key in dict is 1
    end=len(table)#gets the length of the dict thus num of records
    
    while count<=end:

        if id in table[count].values():
            return True
        count+=1

    return False


def validMemberID(id):
    if not re.match(r"^[0-9]{4}$",id):
        return False

    else:
        return True


def validISBN(id):
    if not re.match(r"^[0-9]{13}$",id):
        return False

    else:
        return True
  


def addBook(filename,display,arg):
    """
    this is a function that allows the librarian
    to add books to the data base
    """
    library_db=readDatabase(filename)
    isbn=arg[0].get()#arg stores the variables for the entry widget
    new_data={"ISBN":isbn,"Title":arg[1].get(),"Author":arg[2].get(),\
        "Purchase Date":arg[3].get(),"Member ID":"0"}

    if __name__ != "__main__":

        if not validISBN(isbn):
            mbx.showerror("Error","Invalid ISBN") 

        elif IdExists(isbn,library_db):
            mbx.showerror("Error","Book ISBN already exists") 
        else:


            library_db[(len(library_db)+1)]=new_data

            writeDatabase(library_db,filename)

            display.delete(0,tk.END)#emptys out the display box
            
            display.insert(tk.END,\
                list(new_data.values()))# inserts search results on the display box

            for i in range(len(arg)):
                arg[i].delete(0,tk.END)






if __name__ == "__main__": 
    """
    Tests all functions
    """
    print("Test that databse is read and converted to dict:")
    print()
    readDatabase("database.txt")
    
    print()
    print("Test getDate:")
    getDate()

    print()
    print("Test ID Exists:")
    print()
    print("Exists 9783161484100:")
    print(IdExists("9783161484100",readDatabase("database.txt")))
    print()
    print("Doesnt exist 978316100:")
    print(IdExists("978316100",readDatabase("database.txt")))

    print()
    print("Test validMemberID:")
    print()
    print("Valid ID 3234")
    print(validMemberID("3234"))

    print()
    print("Invalid ID - 32")
    print(validMemberID("32"))


    print()
    print("Test valid ISBN:")
    print()
    print("Valid ISBN 9783161484100")
    print(validISBN("9783161484100"))

    print()
    print("Invalid ISBN 9783161400")
    print(validISBN("9783161400"))