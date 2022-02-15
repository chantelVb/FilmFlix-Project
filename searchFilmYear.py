from ffdbConnection import * 

def searchYear():
     year = input("Enter year of film: ").strip()
     print(year)

     cursor.execute('SELECT * FROM tblFilms WHERE yearReleased='+ "'" + year + "'")

     row = cursor.fetchall()
     for record in row:
        print(record) 

# searchYear()