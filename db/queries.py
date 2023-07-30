import sqlite3
from pathlib import Path


def init_db():
    global db, cursor
    DB_PATH = Path(__file__).parent.parent
    DB_NAME = 'parser_db.sqlite'
    db = sqlite3.connect(DB_PATH/DB_NAME)
    cursor = db.cursor()


def create_tables():
    cursor.execute( """
        CREATE TABLE IF NOT EXISTS cars(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            year INTEGER,
            price INTEGER,
            url TEXT
        )
        """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cars_results(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            year INTEGER,
            price_usd INTEGER,
            url TEXT
        )
    """)
    db.commit()


def populate_tables():
    cursor.execute("""
        INSERT INTO cars (title, year, price_usd, url) 
        VALUES  ('Toyota Highlander', 2016, 31800),
                ('Kia Sportage', 2011, 12900)
    """)
    db.commit()


def cars(data):
    cursor.execute(
        """
        INSERT INTO cars_results (title, year, price) 
        VALUES (:name, :age, :gender)
        """,
        {'title': data['title'], 
        'year': data['year'], 
        'price_usd': data['price_usd']}
    )
    db.commit()


def drop_tables():
    cursor.execute("""
        DROP TABLE IF EXISTS cars
    """)
    db.commit()


def get_cars():
    cars = cursor.execute("""
        SELECT * FROM cars;
    """)
    return cars.fetchall()


if __name__ == '__main__':
    init_db()
    drop_tables()
    create_tables()
    populate_tables()