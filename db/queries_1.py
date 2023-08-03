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
    CREATE TABLE IF NOT EXISTS product(
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
    INSERT INTO product(name, title, price)
    VALUES ("JBL", "Колонки", "1200"),
           ("Samsung Buds", "Наушники", "850"),
           ("Logitech", "Клавиатура", "2600")
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
    DROP TABLE IF EXISTS product
    """)
    db.commit()


def get_product():
    product = cursor.execute("""
    SELECT name, title, price FROM product;
    """)
    products = product.fetchall()
    product1 = products[0]
    product2 = products[1]
    product3 = products[2]
    return f'{product1[0]}{product1[1]} Цена: {product1[2]}\n'\
           f'{product2[0]}{product2[1]} Цена: {product2[2]}\n'\
           f'{product3[0]}{product3[1]} Цена: {product3[2]}\n'

if __name__ == "__main__":
    init_db()
    drop_tables()
    create_table()
    populate_tables()
