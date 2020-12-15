#This Programme was written by Jayeola Akinola on 1st December 2020 - 7th December 2020

import database as db
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mbx


import datetime

def returnBook(isbn,id,member_id,member,database_file,logfile,display,arg):
    
    """
    this is a function to return books first by checking 
    if the book id is valid then if it 
    is eligible to be returned and thus updating the database accordingy
    """
    library_db=db.readDatabase(database_file)
    valid_results=[]
    isbn_exists=db.IdExists(id,library_db)

    if not isbn_exists:
        mbx.showerror("Error","Book ID does not exist")

    elif not db.validISBN(id):
        mbx.showerror("Error","Invalid Book ID")   

    else:

        for i in range(len(library_db)):#loops based on the how many records

            if library_db[i+1][isbn]==id and library_db[i+1][member_id]!='0':
                #^^^checks if id exists and if book is  checked out

                library_db[i+1][member_id]="0"#updates member id to return book
                
                valid_results.append(list(library_db[i+1].values()))#appends > list

        if __name__ != "__main__":#only runs if the main program is running
            if valid_results==[]:
                mbx.showerror("Error","Book is already available")
            else:
                mbx.showinfo("Success!","Book has been returned")

                display.delete(0,tk.END)#emptys out the display box
                for i in valid_results:
                    display.insert(tk.END,i)# inserts search results on the display box

                for i in range(len(arg)):
                    arg[i].delete(0,tk.END)



                log_db=returnLog(id,logfile)
                db.writeDatabase(log_db,logfile)
                db.writeDatabase(library_db,database_file)
        else:
            print(valid_results)

 
def returnLog(id,logfile):

    """
    this is a function to write data to a log dictionary 
    once a book is returned out
    """

    log_db=db.readDatabase(logfile)

    for i in range(len(log_db)):
        if log_db[i+1]["ISBN"]==id and \
            log_db[i+1]["Return Date"]=="0":#checks if books isnt returned
            log_db[i+1]["Return Date"]=str(db.getDate())
            break


    if __name__ == "__main__":
        print(log_db[len(log_db)])#use for testing the return log 
                                  # thats returned  
    return log_db


if __name__ == "__main__":
    """
    tests all the functions 
    """

    print("return Book (ISBN: 9783161484103 Member ID: 4933) <-Book that can be returned")
    print()
    returnBook("ISBN","9783161484103","Member ID","4933","database.txt","logfile.txt",None,None)

    print()
    print("return Log (ISBN: 9783161484103)")
    print()
    returnLog("9783161484103","logfile.txt")
