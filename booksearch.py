import database as db
import tkinter as tk
from tkinter import ttk


def searchBook(title,book,display):
    
    """
    this is a function that uses the element name and field value
    to search for an item in the database in this case searching for
    book based on title
    """
    library_db=db.readDatabase("database.txt")

    search_result=[]
    for i in range(len(library_db)):#loops based on the how many records
        if library_db[i+1][title]==book:#checks if search criteria exists
            search_result.append(list(library_db[i+1].values()))#appends > list
    
    display.delete(0,tk.END)#emptys out the display box
    for i in search_result:
        display.insert(tk.END,i)# inserts search results on the display box


            
        
