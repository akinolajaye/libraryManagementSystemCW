import database as db
import tkinter as tk
from tkinter import ttk
library_db=db.dataToDict("database.txt")
def searchBook(element,field,display):
    """
    this is a function that uses the element name and field value
    to search for an item in the database in this case searching for
    book based on title
    """
    search_result=[]
    for i in range(len(library_db)):#loops based on the how many records
        if library_db[i+1][element]==field:#checks if search criteria exists
            search_result.append(list(library_db[i+1].values()))#appends > list
    
    display.delete(0,tk.END)#emptys out the display box
    for i in search_result:
        display.insert(tk.END,i)# inserts search results on the display box

    return search_result
            
        
