import psycopg2


# connect to "chinook" database
connection = psycopg2.connect(database="chinook")


# build a cursor object
cursor = connection.cursor()

# Query 1 - Select all records from the "Artist" table
# cursor.execute('SELECT * FROM "Artist"')


# Query 2 - Select all results from the "Name" column
# cursor.execute('SELECT "Name" FROM "Artist"')


# Query 3 - select only "Queen" from the "Artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])

# Query 4 - select only by "ArtistId" #51 from the "Artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" =%s', [51])


# cursor.execute('SELECT * FROM "Track" WHERE "Composer" =%s', ["Foo Fighters"])


# cursor.execute('SELECT * FROM "Track" WHERE "Composer" =%s', ["test"])


# fetch the results (multiple)
results = cursor.fetchall()


# fetch the result (single)
# results = cursor.fetchone()


# close the connection
connection.close()


# print results
for result in results:
    print(result)
