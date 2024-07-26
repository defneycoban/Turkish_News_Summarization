from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_news():
    conn = sqlite3.connect('news.db')
    c = conn.cursor()
    c.execute('SELECT * FROM news ORDER BY date DESC')
    news = c.fetchall()
    conn.close()
    return news

@app.route('/')
def index():
    news = get_news()
    return render_template('index.html', news=news)

if __name__ == '__main__':
    app.run(debug=True)
