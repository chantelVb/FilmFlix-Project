from ffdbConnection import *
import time

def update():
    filmID = input("Enter ID of record to be updated: ")

    fieldName = input("Which field fo you want to update: (title, yearReleased, rating, duration, genre) ")

    newFieldValue = input("Enter the new value for the field you are updating: ")
    print("User input: ",newFieldValue)

    newFieldValue = "'" + newFieldValue + "'"
    print("Amended input",newFieldValue)

    try:
        cursor.execute("UPDATE tblFilms SET " + fieldName + "=" + newFieldValue + "WHERE filmID=" + filmID)
        conn.commit()
        print("Record " + filmID + " updated")

        time.sleep(2) 
        cursor.execute('SELECT * FROM tblFilms') 
        row = cursor.fetchall()
        for record in row:
            print(record) 
    except:
        print("Record " + filmID + " has not been updated")
# update()