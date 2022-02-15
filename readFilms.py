from ffdbConnection import *

def displayFilms():
    cursor.execute('SELECT * FROM tblFilms')
    row = cursor.fetchall()
    for record in row:
        print(record)
# displayFilms()