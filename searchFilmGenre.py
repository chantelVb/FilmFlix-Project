from ffdbConnection import * 

def searchGenre():
     genre = input("Enter film genre: ").strip()
     print(genre)

     cursor.execute('SELECT * FROM tblFilms WHERE genre='+ "'" + genre + "'")

     row = cursor.fetchall()
     for record in row:
        print(record) 

# searchGenre()