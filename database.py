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
    for i in range(line_length-1):#loop on the amount of records in txt
        data_record={} #empty dict to store current data record
        data_str=file.readline()#retrieves the data field from txt file

        data_str=data_str.strip("\n")
        data_field=data_str.split(",")

        for j in range(len(data_elements)):#loop on num of data elements
            data_record[data_elements[j]]= data_field[j] 

        database[(i+1)]=data_record

    file.close()

    return database

def writeDatabase(database,filename):
    """
    this is a function the write all data from the
    dictionary to the txt file. this is used for updating
    the database regularly
    """
    file=open(filename,"w+")
    data_elements=list(database[1].keys())#gets the elements
    data_elements= ",".join(data_elements)#formats the data
    file.write(data_elements+"\n")#writes the data to the file

    for i in range(len(database)):#loops through all records
        data_str=list(database[i+1].values())
        data_str=",".join(data_str)
        file.write(data_str+"\n")


    file.close()

