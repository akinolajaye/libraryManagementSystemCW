import datetime


def readDatabase(filename):
    """
    converts data from the text database file 
    into a dictionary that can be interpreted
    byt the python program
    """
    database={}
    file=open(filename,"r+") #Opens the text file in python
    line_length=len(file.readlines())#count the num of lines in the txt file
    file.seek(0)

    data_str=file.readline() # reads the first line of the txt file
    data_str=data_str.strip("\n") #removes leading and trailing white space
    data_elements=data_str.split(",") # converts the text into a list 

    
    
    """
    this for loop  goes through the text file and puts
    each line of text from the txt file(data record) into a 
    dictionary where element is the key and field is the value
    eg: data record={date element: data field} = {Title : Book 1}
    this is then put into another dictionary where the key is the id
    and the value is the data record eg: {1 : {Title: Book1}...}
    """

    if line_length-1 !=0:
        for i in range(line_length-1):#loop on the amount of records in txt
            data_record={} #empty dict to store current data record
            data_str=file.readline()#retrieves the data field from txt file

            data_str=data_str.strip("\n")
            data_field=data_str.split(",")

            for j in range(len(data_elements)):#loop on num of data elements
                data_record[data_elements[j]]= data_field[j] 

            database[(i+1)]=data_record

        file.close()

    else:
            file.close()
    return database



def writeDatabase(database,filename):
    """
    this is a function the write all data from the
    dictionary to the txt file. this is used for updating
    the database regularly
    """

    file=open(filename,"r+") #Opens the text file in python

    data_str=file.readline() # reads the first line of the txt file
    data_str=data_str.strip("\n") #removes leading and trailing white space
    data_elements=data_str.split(",") # converts the text into a list 
    data_elements=",".join(data_elements)#formats the data to a string
    file.close()

    file=open(filename,"w+")
    file.write(data_elements+"\n")#writes the data to the file

    for i in range(len(database)):#loops through all records
        data_str=list(database[i+1].values())
        data_str=",".join(data_str)

        file.write(data_str+"\n")
    file.close()

def getDate():
    """
    gets the current date
    """
    date=str(datetime.date.today())

    return date

def checkoutLog(id,lib):
    """
    this is a function to write data to a log dictionary 
    once a book is checked out
    """
    log_db=readDatabase("logfile.txt")


    for i in range(len(lib)):
        if lib[i+1]["ISBN"]==id:
            member_id=lib[i+1]["Member ID"]# gets the current member id
            bk_title=lib[i+1]["Title"]#gets the book title based on id
            break

        

    log_data={"ISBN":id,"Member ID":member_id,"Title":bk_title,\
        "Checkout Date":str(getDate()),"Return Date":"0","Borrows":"0"}

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

        
    return log_db
            

def returnLog(id):
    """
    this is a function to write data to a log dictionary 
    once a book is returned out
    """

    log_db=readDatabase("logfile.txt")

    for i in range(len(log_db)):
        if log_db[i+1]["ISBN"]==id and \
            log_db[i+1]["Return Date"]=="0":#checks if books isnt returned
            log_db[i+1]["Return Date"]=str(getDate())
            break


    return log_db








    