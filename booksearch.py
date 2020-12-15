#This Programme was written by Jayeola Akinola on 1st December 2020 - 7th December 2020

import database as db
import tkinter as tk
from tkinter import ttk


def searchBook(title,book,display,filename):
    
    """
    this is a function that uses the element name and field value
    to search for an item in the database in this case searching for
    book based on title
    """
    library_db=db.readDatabase(filename)

    search_result=[]
    for i in range(len(library_db)):#loops based on the how many records
        if library_db[i+1][title].upper()==book.upper():#checks if search criteria exists
            search_result.append(list(library_db[i+1].values()))#appends > list
    
    """
    this if statement is so that display into tkinter window
    is only run when running from menu thus allowing for testing
    without error
    """
    if __name__ != "__main__":
        
        display.delete(0,tk.END)#emptys out the display box
        for i in search_result:
            display.insert(tk.END,i)# inserts search results on the display box

    else:

        for i in search_result:
            print(i)
        print()


            
        
def displayBooks(filename,display):
    """
    this is a function to display all library books
    from the data base onto the list box
    """
    display_all=[]
    library_db=db.readDatabase(filename)
    for i in range (len(library_db)):
        display_all.append((list(library_db[i+1].values())))

    if __name__ != "__main__":#only displays on tkinter if main program
        
        display.delete(0,tk.END)
        for i in display_all :
            display.insert(tk.END,i)

    else:
        for i in display_all:
            print(i)
        print()
    
    

if __name__ == "__main__":
    """
    tests all the functions 
    """

    print("searchBook (Book_1):")
    print()
    searchBook("Title","book_1",None,"database.txt")

    print("displayBooks :")
    print()
    displayBooks("database.txt",None)

   