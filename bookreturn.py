import database as db
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mbx
from bookcheckout import IdExists,validISBN,validMemberID

import datetime

def returnBook(isbn,id,member_id,member,display,arg):
    
    """
    this is a function to return books first by checking 
    if the book id is valid then if it 
    is eligible to be returned and thus updating the database accordingy
    """
    library_db=db.readDatabase("database.txt")
    valid_results=[]
    isbn_exists=IdExists(id,library_db)
    member_exists=IdExists(member,library_db)

    if not isbn_exists:
        mbx.showerror("Error","Book ID does not exist")

    elif not validISBN(id):
        mbx.showerror("Error","Invalid Book ID")   

    elif not member_exists:
        mbx.showerror("Error","Member does not exist") 

    elif not validMemberID(member):
        mbx.showerror("Error","Invalid Member ID")


    else:

        for i in range(len(library_db)):#loops based on the how many records

            if library_db[i+1][isbn]==id and \
                library_db[i+1][member_id]!='0':
                #^^^checks if id exists and if book is  checked out

                library_db[i+1][member_id]="0"#updates member id to return book
                
                valid_results.append(list(library_db[i+1].values()))#appends > list

        if valid_results==[]:
            mbx.showerror("Error","Book is already available")
        else:
            mbx.showinfo("Success!","Book has been returned")

            display.delete(0,tk.END)#emptys out the display box
            for i in valid_results:
                display.insert(tk.END,i)# inserts search results on the display box

            for i in range(len(arg)):
                arg[i].delete(0,tk.END)



            log_db=returnLog(id)
            db.writeDatabase(log_db,"logfile.txt")
            db.writeDatabase(library_db,"database.txt")


 
def returnLog(id):

    """
    this is a function to write data to a log dictionary 
    once a book is returned out
    """

    log_db=db.readDatabase("logfile.txt")

    for i in range(len(log_db)):
        if log_db[i+1]["ISBN"]==id and \
            log_db[i+1]["Return Date"]=="0":#checks if books isnt returned
            log_db[i+1]["Return Date"]=str(db.getDate())
            break


    return log_db


