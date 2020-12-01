import database as db
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mbx
import datetime

def validID(id,table):
    """
    This is a function to check if the id entered
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


def checkoutBook(isbn,id,member_id,member,display):
    
    """
    this is a function the check out books first by checking if the book
    is eligible to be checked out and thus updating the database accordingy
    """
    library_db=db.readDatabase("database.txt")
    valid_results=[]
    valid_id=validID(id,library_db)
    if not valid_id:
        mbx.showerror("Error","Invalid Book ID")
    else:

        for i in range(len(library_db)):#loops based on the how many records

            if library_db[i+1][isbn]==id and \
                library_db[i+1][member_id]=='0':
                #^^^checks if id exists and if book is not checked out

                library_db[i+1][member_id]=member#updates member id to checkout book
                valid_results.append(list(library_db[i+1].values()))#appends > list

        if valid_results==[]:
            mbx.showerror("Error","Book has already been checked out")
        else:
            mbx.showinfo("Success!","Book has been loaned to member:%s"%(member))
            display.delete(0,tk.END)#emptys out the display box
            for i in valid_results:
                display.insert(tk.END,i)# inserts search results on the display box
      
            log_db=db.checkout_Log(id)
            db.writeDatabase(log_db,"logfile.txt")
            db.writeDatabase(library_db,"database.txt")


 











    


