import database as db
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mbx
library_db=db.readDatabase("database.txt")

def checkoutBook(isbn,id,member_id,member,display):
    """
    this is a function the check out books first by checking if the book
    is eligible to be checked out and thus updating the database accordingy
    """

    valid_results=[]
    for i in range(len(library_db)):#loops based on the how many records
        if library_db[i+1][isbn]==id and \
            library_db[i+1][member_id]=='0':
            #^^^checks if id exists and if book is not checked out

            library_db[i+1][member_id]=member#updates member id to checkout book
            valid_results.append(list(library_db[i+1].values()))#appends > list

    if valid_results==[]:
        mbx.showerror("Error","Book has already been checked out by...")
    else:

        display.delete(0,tk.END)#emptys out the display box
        for i in valid_results:
            display.insert(tk.END,i)# inserts search results on the display box







    


