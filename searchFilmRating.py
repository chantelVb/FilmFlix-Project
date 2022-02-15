from ffdbConnection import * 

def searchRatings():
     rating = input("Enter film rating: ").strip()
     print(rating)

     cursor.execute('SELECT * FROM tblFilms WHERE rating='+ "'" + rating + "'")

     row = cursor.fetchall()
     for record in row:
        print(record) 

# searchRatings()