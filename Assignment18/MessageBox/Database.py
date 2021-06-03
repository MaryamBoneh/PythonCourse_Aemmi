from datetime import datetime
from sqlite3 import connect


class Database:

    @staticmethod
    def insert(name, text):
        try:
            my_con = connect('Assignment18/MessageBox/messages.db')
            my_cursor = my_con.cursor()
            time = datetime.now().strftime('%Y-%m-%d-%H:%M:%S')
            my_cursor.execute(f"INSERT INTO messages(NAME, TEXT, TIME) VALUES('{name}','{text}','{time}')")
            my_con.commit()
            my_con.close()
            return True
        except Exception as e:
            print("error:", e)
            return False

    @staticmethod
    def select():
        try:
            my_con = connect('Assignment18/MessageBox/messages.db')
            my_cursor = my_con.cursor()
            my_cursor.execute("SELECT * FROM messages")
            result = my_cursor.fetchall()
            my_con.close()
            return result
        except Exception as e:
            print("error:", e)
            return []

    @staticmethod
    def delete(id):
        try:
            my_con = connect('Assignment18/MessageBox/messages.db')
            my_cursor = my_con.cursor()
            my_cursor.execute(f"DELETE FROM messages WHERE ID = {id}")
            my_con.commit()
            my_con.close()
            return True
            
        except Exception as e:
            print("error:", e)
            return False
   
    @staticmethod
    def deleteAll():
        try:
            my_con = connect('Assignment18/MessageBox/messages.db')
            my_cursor = my_con.cursor()
            my_cursor.execute(f"DELETE FROM messages")
            my_con.commit()
            my_con.close()
            return True
            
        except Exception as e:
            print("error:", e)
            return False
