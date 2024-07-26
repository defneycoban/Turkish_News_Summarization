import sqlite3

def setup_db():
    conn = sqlite3.connect('news.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS news (
            id INTEGER PRIMARY KEY,
            date TEXT,
            headline TEXT,
            summary TEXT
        )
    ''')
    conn.commit()
    conn.close()

if __name__ == '__main__':
    setup_db()
