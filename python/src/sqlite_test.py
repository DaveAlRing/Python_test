import sqlite3

# .connect() creates database object and assigns to variable
connection = sqlite3.connect("gta.db")
# .cursor() creates cursor object for connection database and assings to variable
cursor = connection.cursor()

# .execute() executes commands within db. Tables require data type after name
cursor.execute("create table gta (release_year integer, release_name text, city text)")

release_list = [
    (1997, "Grand Theft Auto", "state of New Guernsey"),
    (1999, "Grand Theft Auto 2", "Anywhere, USA"),
    (2001, "Grand Theft Auto III", "Liberty City"),
    (2002, "Grand Theft Auto: Vice City", "Vice City"),
    (2004, "Grand Theft Auto: San Andreas", "state of San Andreas"),
    (2008, "Grand Theft Auto IV", "Liberty City"),
    (2013, "Grand Theft Auto V", "Los Santos")
]

# inserts values into db. "?" are places holders, release_list is data
cursor.executemany("insert into gta values (?,?,?)", release_list)

# print db rows
for row in cursor.execute("select * from gta"):
    print(row)

# assign city column to c. Search c for Liberty City and print those entries
print("****************")
cursor.execute("select * from gta where city = :c", {"c" : "Liberty City"})
gta_search = cursor.fetchall()
print(gta_search)

#create new table comparing cities
cursor.execute("create table cities (gta_city text, real_city text)")
cursor.execute("insert into cities values (?,?)", ("Liberty City", "New York"))
cursor.execute("select * from cities where gta_city = :c", {"c" : "Liberty City"})
cities_search = cursor.fetchall()
print(cities_search)

# manipulate database data
print("*******************")
for i in gta_search:
    adjusted = [cities_search[0][1] if value == cities_search[0][0] else value for value in i]
    print(adjusted)
    
connection.close()