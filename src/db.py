import sqlite3
import pandas as pd

DB_PATH = "expenses.db"


# -----------------------------
# INIT DATABASE
# -----------------------------
def init_db():

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        category TEXT,
        amount REAL,
        note TEXT
    )
    """)

    conn.commit()
    conn.close()


# -----------------------------
# INSERT DATA (MISSING FUNCTION FIX)
# -----------------------------
def insert_data(df):

    conn = sqlite3.connect(DB_PATH)

    df.to_sql("expenses", conn, if_exists="append", index=False)

    conn.close()


# -----------------------------
# FETCH DATA
# -----------------------------
def fetch_data():

    conn = sqlite3.connect(DB_PATH)

    df = pd.read_sql("SELECT * FROM expenses", conn)

    conn.close()

    return df