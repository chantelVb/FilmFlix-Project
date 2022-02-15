from ffdbConnection import * 

def searchTitle():
     title = input("Enter film title to search for: ").strip()
     print(title)

     cursor.execute('SELECT * FROM tblFilms WHERE title='+ "'" + title + "'")

     row = cursor.fetchall()
     for record in row:
        print(record) 

# searchTitle()