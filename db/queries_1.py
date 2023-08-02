import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent.parent
DB_NAME = 'db.sqlite'
db = sqlite3.connect(DB_PATH / DB_NAME)
cursor = db.cursor()
def init_db():
    global db, cursor
def create_table():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tovar(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    title TEXT,
    price INTEGER
    )
    ''')
    db.commit()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS user_resaults(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    gender TEXT
    )
    ''')
    db.commit()


def populate_tables():
    cursor.execute("""
    INSERT INTO tovar(name, title, price)
    VALUES ("Стразы", "камня свароского", "500"),
           ("Стразы", "Пластикого", " 250"),
           ("Стразы", "Стекло", "350")
    """)
    db.commit()


def save_user_results(data):
    cursor.execute("""
    INSERT INTO user_resaults(name, age, gender)
    VALUES (:name, :age, :gender)
    """,
                   {'name': data['name'],
                    'age': data['age'],
                    'gender': data['gender']}
                   )
    db.commit()




def drop_tables():
    cursor.execute("""
    DROP TABLE IF EXISTS tovar
    """)
    db.commit()


def get_tovar():
    tovar = cursor.execute("""
    SELECT name , title , price FROM tovar;
    """)
    return tovar.fetchall()


if __name__ == "__main__":
    init_db()
    drop_tables()
    create_table()
    populate_tables()
