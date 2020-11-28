import database as db
library_db=db.dataToDict("database.txt")
def searchBook(element,field):
    search_result=[]
    for i in range(len(library_db)):
        if library_db[i+1][element]==field:
            search_result.append(list(library_db[i+1].values()))

    print(search_result)
    return search_result
            
        
