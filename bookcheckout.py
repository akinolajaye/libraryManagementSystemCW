#This Programme was written by Jayeola Akinola on 1st December 2020 - 7th December 2020

import database as db
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mbx
import re




def checkoutBook(isbn,id,member_id,member,database_file,logfile,display,arg):
    
    """
    this is a function the check out books first by checking if the book
    is eligible to be checked out and thus updating the database accordingy
    """
    library_db=db.readDatabase(database_file)
    valid_results=[]
    isbn_exists=db.IdExists(id,library_db)

    if not isbn_exists:
        mbx.showerror("Error","Book ID does not exist")

    elif not db.validISBN(id):
        mbx.showerror("Error","Invalid Book ID")   

    elif not db.validMemberID(member):
        mbx.showerror("Error","Invalid Member ID")
    else:

        for i in range(len(library_db)):#loops based on the how many records

            if library_db[i+1][isbn]==id and \
                library_db[i+1][member_id]=='0':
                #^^^checks if id exists and if book is not checked out

                library_db[i+1][member_id]=member#updates member id to checkout book
                valid_results.append(list(library_db[i+1].values()))#appends > list

        if __name__ != "__main__":#only runs if the main program is running
             

            if valid_results==[]:
                mbx.showerror("Error","Book has already been checked out")
            else:
                mbx.showinfo("Success!","Book has been loaned to member:%s"%(member))
                display.delete(0,tk.END)#emptys out the display box
                for i in valid_results:
                    display.insert(tk.END,i)# inserts search results on the display box

                for i in range(len(arg)):
                    arg[i].delete(0,tk.END)

        
                log_db=checkoutLog(id,library_db,logfile)
                db.writeDatabase(log_db,logfile)
                db.writeDatabase(library_db,database_file)

        else:
            print(valid_results)
            
                


def checkoutLog(id,lib,logfile):
    """
    this is a function to write data to a log dictionary 
    once a book is checked out
    """
    log_db=db.readDatabase(logfile)


    for i in range(len(lib)):
        if lib[i+1]["ISBN"]==id:
            member_id=lib[i+1]["Member ID"]# gets the current member id
            bk_title=lib[i+1]["Title"]#gets the book title based on id
            break

        

    log_data={"ISBN":id,"Member ID":member_id,"Title":bk_title,\
        "Checkout Date":str(db.getDate()),"Return Date":"0","Borrows":"0"}

    log_db[(len(log_db)+1)]=log_data#adds the log data to dictionary

    """
    the statement below is a list comprehension that returns a list of 
    the amount of borrows that has occured for a book title 
    the maximum value in the list being the current number of times
    the book has been borrowed
    when the book is borrowed again then the statement will add 1 to the max
    The amount of borrowers is based on the title
    """

    borrows=([int(log_db[i+1]["Borrows"]) for i in range(len(log_db)) \
        if log_db[i+1]["Title"]==bk_title])#gets a list of the number of
                                     #borrows for the given book title
    log_db[len(log_db)]["Borrows"]=str(max(borrows)+1)#

    if __name__ == "__main__":
        print(log_db[len(log_db)])#use for testing the check out log 
                                  # thats returned

        
    return log_db
            



if __name__ == "__main__":
    """
    tests all the functions 
    """

    print("checkout Book (ISBN: 9783161484100 Member ID: 5432)")
    print()
    checkoutBook("ISBN","9783161484100","Member ID","5432","database.txt","logfile.txt",None,None)

    print()
    print("checkout Book (ISBN: 9783161484103 Member ID: 4933) <-Book that is checked out")
    print()
    checkoutBook("ISBN","9783161484103","Member ID","4933","database.txt","logfile.txt",None,None)


    print()
    print("checkout Log (ISBN: 9783161484103)")
    checkoutLog("9783161484103",db.readDatabase("database.txt"),"logfile.txt")










    


