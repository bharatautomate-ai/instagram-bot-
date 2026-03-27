import sqlite3

conn = sqlite3.connect("store.db", check_same_thread=False)
cursor = conn.cursor()

# CLIENT TABLE
cursor.execute("""
CREATE TABLE IF NOT EXISTS clients (
    id TEXT PRIMARY KEY,
    page_id TEXT
)
""")

# PRODUCTS TABLE
cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id TEXT,
    name TEXT,
    keywords TEXT,
    price INTEGER,
    sizes TEXT,
    stock INTEGER,
    location TEXT,
    description TEXT,
    link TEXT
    White Shoes TEXT,
shoes,white shoes,shoe,sneakers,white sneaker,
     cost and location TEXT,
     Rate and addrase TEXT,
     قیمت  TEXT,
    قیمت کیا ہے  TEXT,
                
    Great lcation,            
                            
                                              
)
""")

conn.commit()