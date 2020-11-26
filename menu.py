import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext as st
from tkinter import messagebox as mbx
win=tk.Tk()#creates an instance of the tkinter module
title='LibraryManagementSystem'
book_title=tk.StringVar()#sets book title as a string variable

def createWindow(window,title):#function to setup the window
    window.title(title) #sets the window title
    window.geometry("500x500")#sets defualt window size

def createFrames(window): #function to create all the frames that will be used
    #creates a frame that will be used as a container for other frames
    main_frame=ttk.LabelFrame(window,text="LibrayManagmentSystem")
    main_frame.pack(fill="both") #organises the frame position on the window

    data_frame=ttk.Frame(main_frame) #creates a frame to hold entry and display
    data_frame.pack(side=tk.TOP,fill='x')

    entry_frame=ttk.Frame(data_frame) #creates a frame to hold entry widgets
    entry_frame.pack(side=tk.LEFT,anchor='nw')

    display_frame=ttk.Frame(data_frame) #creates a frame to hold display widget
    display_frame.pack(side=tk.RIGHT,anchor='w')

    button_frame=ttk.Frame(main_frame)#creates a frame to hold buttons
    button_frame.pack(side=tk.BOTTOM,fill='x')

    return entry_frame,display_frame,button_frame

def createLabels(frame): #function to create label for entry fields
    bk_title_lbl=ttk.Label(frame,text="Book Title:")
    bk_title_lbl.grid(row=0,column=0)#organises widget in grid form

def createEntrys(frame,var,w):#function to create entry field widgets
    bk_title_entry=ttk.Entry(frame,textvariable=var,width=w)
    bk_title_entry.grid(row=0,column=1)

def createListbox(frame,w,h):
    """
    creates a list box that will display data 
    x and y scrollbar creates horizontal and vertical scrollbars
    and binds them to the list box
    """

    display=tk.Listbox(frame,width=w,height=h)
    yscrollbar= st.Scrollbar(frame,orient=tk.VERTICAL,command=display.yview)
    xscrollbar= st.Scrollbar(frame,orient=tk.HORIZONTAL,command=display.xview)
    display.configure(yscrollcommand=yscrollbar.set)
    display.configure(yscrollcommand=yscrollbar.set)
    yscrollbar.pack(fill='y',side=tk.RIGHT)
    xscrollbar.pack(fill="x",side=tk.BOTTOM)

    display.pack(side=tk.TOP,fill='both',expand=1)


def createButtons(frame):
    """
    creates buttons that will perform functions
    for the program
    """
    search=ttk.Button(frame,text="Search")
    search.grid(row=0,column=0)

    exit=ttk.Button(frame,text="Exit")
    exit.grid(row=0,column=1)
    return search,exit

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
        



createWindow(win,title)
entry_frame, display_frame,button_frame=createFrames(win)
createLabels(entry_frame)
createEntrys(entry_frame,book_title,15)
createListbox(display_frame,20,10)
search,exit=createButtons(button_frame)

exit.configure(command=lambda:exitProgram(win,title))
#^^^binds the function 'exitProgram' to the button 'exit'

win.mainloop()