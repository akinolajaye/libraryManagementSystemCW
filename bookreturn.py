import database as db
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mbx
from bookcheckout import validID

def returnBook(isbn,id,member_id,member,display):
    
    """
    this is a function to return books first by checking 
    if the book id is valid then if it 
    is eligible to be returned and thus updating the database accordingy
    """
    library_db=db.readDatabase("database.txt")
    valid_results=[]
    valid_id=validID(id,library_db)
    if not valid_id:
        mbx.showerror("Error","Invalid Book ID")
    else:

        for i in range(len(library_db)):#loops based on the how many records

            if library_db[i+1][isbn]==id and \
                library_db[i+1][member_id]!='0':
                #^^^checks if id exists and if book is  checked out

                library_db[i+1][member_id]=member#updates member id to return book
                
                valid_results.append(list(library_db[i+1].values()))#appends > list

        if valid_results==[]:
            mbx.showerror("Error","Book is already available")
        else:
            mbx.showinfo("Success!","Book has been returned")
            display.delete(0,tk.END)#emptys out the display box
            for i in valid_results:
                display.insert(tk.END,i)# inserts search results on the display box

  
            
            log_db=db.returnLog(id)
            db.writeDatabase(log_db,"logfile.txt")
            db.writeDatabase(library_db,"database.txt")


 