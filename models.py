import sqlite3


class Todos:
    def __init__(self, database):
        self.conn = None
        try:
            self.conn = sqlite3.connect(database, check_same_thread=False)
            self.cur = self.conn.cursor()
        except sqlite3.Error as e:
            print(e)


    def all(self):
        return self.todos


    def show_all(self):
        self.cur.execute("SELECT * FROM CDs")
        self.conn.commit()
        rows = self.cur.fetchall()
        return rows

    def show_one(self, id):
        self.cur.execute(f"SELECT * FROM CDs WHERE id ={id}")
        row = self.cur.fetchone()
        return row

    def insert(self, values):
        self.cur.execute('''INSERT INTO CDs(artist, year_of_publication, CD_name, my_favourite)
                         VALUES (?,?,?,?)''', values)
        self.conn.commit()
        self.conn.close()

    def update(self, id, values):
        sql = f''' UPDATE CDs
                    SET id ={id},
                    artist =?,
                    year_of_publication=?,
                    CD_name=?,
                    my_favourite=?
                    WHERE id = {id}'''
        self.cur.execute(sql, values)
        self.conn.commit()
        self.conn.close()

    def delete(self, id):
        self.cur.execute(f"DELETE FROM CDs where id={id}")
        self.conn.commit()
        self.conn.close()



database = "database.db"
todos = Todos(database)

