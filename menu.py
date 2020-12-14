import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext as st
from tkinter import messagebox as mbx
import booksearch as bsrch
import bookcheckout as bcheck
import bookreturn as breturn
import bookweed as bweed
import database as db
win=tk.Tk()#creates an instance of the tkinter module
win_title='LibraryManagementSystem'
isbn=tk.StringVar()#sets isbn as a string variable
title=tk.StringVar()
author=tk.StringVar()
purchase_date=tk.StringVar()
member_id=tk.StringVar()


 
def createWindow(window,title):#function to setup the window
    window.title(title) #sets the window title
    window.geometry("700x280")#sets defualt window size
    window.resizable(0,0)

def createFrames(window): #function to create all the frames that will be used
    #creates a frame that will be used as a container for other frames
    main_frame=ttk.LabelFrame(window,text="LibrayManagmentSystem")
    main_frame.pack(fill="both") #organises the frame position on the window

    data_frame=ttk.Frame(main_frame) #creates a frame to hold entry and display_box
    data_frame.pack(side=tk.TOP,fill='x')

    entry_frame=ttk.Frame(data_frame) #creates a frame to hold entry widgets
    entry_frame.pack(side=tk.LEFT,anchor='nw')

    display_frame=ttk.Frame(data_frame) #creates a frame to hold display_box widget
    display_frame.pack(side=tk.RIGHT,anchor='w')

    button_frame=ttk.Frame(main_frame)#creates a frame to hold buttons
    button_frame.pack(side=tk.BOTTOM,fill='x')

    return entry_frame,display_frame,button_frame

def createLabels(frame): #function to create label for entry fields
    isbn_lbl=ttk.Label(frame,text="ISBN:")
    isbn_lbl.grid(row=0,column=0)#organises widget in grid form

    title_lbl=ttk.Label(frame,text="Book Title:")
    title_lbl.grid(row=1,column=0)

    author_lbl=ttk.Label(frame,text="Author:")
    author_lbl.grid(row=2,column=0)

    purchase_date_lbl=ttk.Label(frame,text="Purchase Date:")
    purchase_date_lbl.grid(row=3,column=0)

    member_id_lbl=ttk.Label(frame,text="Member ID:")
    member_id_lbl.grid(row=4,column=0)

def createEntrys(frame,w):#function to create entry field widgets
    
    isbn_entry=ttk.Entry(frame,textvariable=isbn,width=w)
    isbn_entry.grid(row=0,column=1)

    title_entry=ttk.Entry(frame,textvariable=title,width=w)
    title_entry.grid(row=1,column=1)

    search=ttk.Button(frame,text="Search",command=lambda:bsrch.searchBook\
        ("Title",title_entry.get(),display_box,"database.txt"))
    #^^^ binds the function 'searchbook' to the button 'search')
    search.grid(row=1,column=2)

    author_entry=ttk.Entry(frame,textvariable=author,width=w)
    author_entry.grid(row=2,column=1)

    purchase_date_entry=ttk.Entry(frame,textvariable=purchase_date,width=w)
    purchase_date_entry.grid(row=3,column=1)

    member_id_entry=ttk.Entry(frame,textvariable=member_id,width=w)
    member_id_entry.grid(row=4,column=1)

    return isbn_entry,title_entry,author_entry,\
        purchase_date_entry,member_id_entry 

def createListbox(frame,w,h):
    """
    creates a list box that will display_box data 
    x and y scrollbar creates horizontal and vertical scrollbars
    and binds them to the list box
    """

    display_box=tk.Listbox(frame,width=w,height=h)
    yscrollbar= st.Scrollbar(frame,orient=tk.VERTICAL,command=display_box.yview)
    xscrollbar= st.Scrollbar(frame,orient=tk.HORIZONTAL,command=display_box.xview)
    display_box.configure(yscrollcommand=yscrollbar.set)
    display_box.configure(yscrollcommand=yscrollbar.set)
    yscrollbar.pack(fill='y',side=tk.RIGHT)
    xscrollbar.pack(fill="x",side=tk.BOTTOM)

    display_box.pack(side=tk.TOP,fill='both',expand=1)

    return display_box

def insertFromDisplay(event,widget,frame):
    """
    this is a function to insert data into the entry
    fields when selected from the display_box box
    """
    try:
        j=0
        search=widget.curselection()[0] # gets the line index of the data selected
        data=widget.get(search) #uses the index returns tuples which hold selected data

        for i in frame.winfo_children():# loops through widgets in frame "entry in this case"

            if isinstance(i,ttk.Entry): #checks if the widget is an entry widget
                i.delete(0,tk.END) #empties the entry field
                i.insert(tk.END,data[j]) #inserts given data into the entry fields
                j+=1

                


    except:
        pass


def createButtons(frame,display_box):
    """
    creates buttons that will perform functions
    for the program
    """
    add=ttk.Button(frame,text="Add Book",command=lambda:db.addBook\
    ("database.txt",display_box,entry_array))
    add.grid(row=0,column=1)

    checkout=ttk.Button(frame,text="Checkout",command=lambda:bcheck.checkoutBook\
    ('ISBN',isbn_entry.get(),"Member ID",member_id_entry.get()\
        ,display_box,entry_array))
    checkout.grid(row=0,column=2)


    return_bk=ttk.Button(frame,text="Return",command=lambda:breturn.returnBook\
    ('ISBN',isbn_entry.get(),"Member ID",member_id_entry.get()\
        ,display_box,entry_array))
    return_bk.grid(row=0,column=3)

    weed=ttk.Button(frame,text="Weed",command=lambda:bweed.bookweed())

    weed.grid(row=0,column=4)

    display_data=ttk.Button(frame,text="Display",command=lambda:bsrch.displayBooks\
    ("database.txt",display_box))
    display_data.grid(row=0,column=5)

    exit=ttk.Button(frame,text="Exit",command=lambda:exitProgram(win,win_title))
    #^^^binds the function 'exitProgram' to the button 'exit')
    exit.grid(row=0,column=6)

 
def exitProgram(window,title):
    """
    function to exit the program
    using a ask yes or no confirmation for exit
    this function will be binded to the button 'exit'
    """
    close=mbx.askyesno(title,"Confirm if you want to exit")
    if close >0: #Checks if close is yes or no, yes being 1
        window.quit()
        window.destroy()





    


createWindow(win,win_title)#creates window

entry_frame, display_frame,button_frame=createFrames(win)#creates frames
    
createLabels(entry_frame)#creates labels

isbn_entry,title_entry,author_entry,purchase_date_entry,\
    member_id_entry =createEntrys(entry_frame,15)#creates entry fields

entry_array=[i for i in entry_frame.winfo_children() if isinstance(i,ttk.Entry)]


display_box=createListbox(display_frame,50,12)#creates listbox
display_box.bind('<<ListboxSelect>>',\
     lambda event:insertFromDisplay(event,display_box,entry_frame))  
#^^^binds a function to the event when data in the list box gets selected
#^^after data is selected on the list box it is inserted into entry fields

createButtons(button_frame,display_box)#creates buttons



win.mainloop()