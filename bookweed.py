import numpy as np
import matplotlib.pyplot as plt
import database as db
import datetime

def bookweed():
    """
    This is a function to suggest which books should be removed
    it does this by calculating the amount of borrows per year
    from a books first checkout to the current date
    """
    lib=db.readDatabase("logfile.txt")
    book_titles=[]
    book_borrows=[]
    for i in range(len(lib)):
        if lib[i+1]["Title"] not in book_titles:#creates a list of book titles
            book_titles.append(lib[i+1]["Title"])

  
    

    for i in book_titles:
        borrows=([int(lib[j+1]["Borrows"]) for j in range(len(lib)) \
            if lib[j+1]["Title"]==i])#creates list of borrows for each book

        book_borrows.append(max(borrows))

        
    """
    This for statement gets the first checkout date for 
    each book
    """

    dates=[]  
    for i in book_titles:
        for j in range(len(lib)):
            if lib[j+1]["Title"]==i:#gets the first checkout date
                dates.append(lib[j+1]["Checkout Date"])
                break

    years_since_first_checkout=[]
    today=datetime.datetime.now()
    for i in dates:
        date=datetime.datetime.strptime(i,"%Y-%m-%d")

        time_span= today -date
        days_in_years=time_span.days//365

        

        years_since_first_checkout.append(days_in_years)

    



    borrows_per_year=[]    
    for i in range(len(book_borrows)):

        if years_since_first_checkout[i]!=0:
            bpy=book_borrows[i]//years_since_first_checkout[i]
            borrows_per_year.append(bpy)
        else:
            borrows_per_year.append(0)

    

    weeded_books=[]
    weed_values=[]

    books=[]
    book_values=[]

    book_count=[]
    data=db.readDatabase("database.txt")

    """
    The criteria for a book to get weeded is
    if the borrows per year for each 
    book is less than 12 then that book will
    be signalled for removal.
    
    for loop creates an array of books to be 
    weeded and books not to be weeded
    """
    for i in book_titles:
        count=0
        for j in range(len(data)):
            if data[j+1]["Title"]==i:
                count+=1

        book_count.append(count)

    for i in range(len(book_count)):

        if borrows_per_year[i]!=0:        
            if borrows_per_year[i]<12:

                
                weeded_books.append(book_titles[i])
                weed_values.append(borrows_per_year[i])


            else:
                books.append(book_titles[i])
                book_values.append(borrows_per_year[i])

        else:
            weeded_books.append(book_titles[i])
            weed_values.append(borrows_per_year[i])


            

    
    plt.bar(weeded_books,weed_values,color="red",label="Books to be removed")
    plt.bar(books,book_values,color="blue",label="Normal Books")
    plt.legend(loc="upper left")
    plt.xlabel("Book Title")
    plt.ylabel("Borrows per Year")
    plt.title("Weeding")
    plt.show()

