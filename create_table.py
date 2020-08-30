import sqlite3

conn = sqlite3.connect("database.db")
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS CDs(
                    id integer PRIMARY KEY,
                    artist TEXT,
                    year_of_publication INTEGER,
                    CD_name TEXT,
                    my_favourite TEXT);
        """)
cur.execute("""INSERT INTO CDs (artist, year_of_publication, CD_name, my_favourite) VALUES(
                    'Beyonce',
                    2003,
                    'Dangerously in love',
                    'yes');
        """)
conn.commit()
cur.execute("SELECT * FROM CDs")
conn.commit()
rows = cur.fetchall()
values = ["Beyonce", 2003, "Dangerously in love", "no"]
sql = ''' UPDATE CDs
                   SET artist =?,
                   year_of_publication=?,
                   CD_name=?,
                   my_favourite=?
                   WHERE id = 1'''
cur.execute(sql, values)
conn.commit()

conn.close()