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
    
    display.delete(0,tk.END)#emptys out the display box
    for i in search_result:
        display.insert(tk.END,i)# inserts search results on the display box


            
        
def displayBooks(filename,display):
    """
    this is a function to display all library books
    from the data base onto the list box
    """
    display_all=[]
    library_db=db.readDatabase(filename)
    for i in range (len(library_db)):
        display_all.append((list(library_db[i+1].values())))

    display.delete(0,tk.END)
    for i in display_all :
        display.insert(tk.END,i)
    
    

