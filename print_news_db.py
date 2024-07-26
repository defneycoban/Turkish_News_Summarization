import sqlite3

def print_news_db():
    conn = sqlite3.connect('news.db')
    c = conn.cursor()
    c.execute('SELECT * FROM news')
    rows = c.fetchall()
    for row in rows:
        print(row)
    conn.close()

if __name__ == '__main__':
    print_news_db()
