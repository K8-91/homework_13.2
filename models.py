import sqlite3


class Todos:
    def __init__(self, database):
        self.conn = None
        try:
            self.conn = sqlite3.connect(database, check_same_thread=False)
            self.cur = self.conn.cursor()
        except sqlite3.Error as e:
            print(e)

    #def all(self):
        #return self.todos

    def show_all(self):
        self.cur.execute("SELECT * FROM CDs")
        self.conn.commit()
        rows = self.cur.fetchall()
        return rows

    def show_one(self, todo_id):
        self.cur.execute(f"SELECT * FROM CDs WHERE id ={todo_id+1}")
        columns = ["id", "artist", "year_of publication", "CD_name", "my_favourite"]
        row = self.cur.fetchone()
        CD_dict = dict(zip(columns, row))
        return CD_dict

    def insert(self, values):
        self.cur.execute('''INSERT INTO CDs(artist, year_of_publication, CD_name, my_favourite)
                         VALUES (?,?,?,?)''', values)
        self.conn.commit()

    def update(self, todo_id, values):
        sql = f''' UPDATE CDs
                    SET id ={todo_id},
                    artist =?,
                    year_of_publication=?,
                    CD_name=?,
                    my_favourite=?
                    WHERE id = {todo_id}'''
        self.cur.execute(sql, values)
        self.conn.commit()

    def delete(self, todo_id):
        self.cur.execute(f"DELETE FROM CDs where id={todo_id}")
        self.conn.commit()



database = "database.db"
todos = Todos(database)