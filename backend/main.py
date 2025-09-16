from fastapi import FastAPI, requests
from fastapi.staticfiles import StaticFiles
import sqlite3

from routes import notes

app = FastAPI(title='ToDo List server')

app.include_router(notes.router)


# def create_db():
#     con = sqlite3.connect('users.db')
#     cur = con.cursor()
#     cur.execute(''' CREATE TABLE IF NOT EXISTS users ( user_id INTEGER PRIMARY KEY,
#                                                            username TEXT,
#                                                            first_name TEXT,
#                                                            score INTEGER DEFAULT 0 ) ''')
#
#     con.commit()
#     con.close()


def setup_db():
    conn = sqlite3.connect('notes.db')
    cur = conn.cursor()
    cur.execute(''' CREATE TABLE IF NOT EXISTS notes ( user_id INTEGER,
                                                        note TEXT ) ''')

    conn.commit()
    conn.close()

def get_db():
    conn = sqlite3.connect('notes.db', check_same_thread=False)
    try:
        yield conn
    finally:
        conn.close()


def main():
    setup_db()

if __name__ == '__main__':
    main()
