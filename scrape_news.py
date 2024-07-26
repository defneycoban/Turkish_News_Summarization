import requests
from bs4 import BeautifulSoup
import sqlite3
from datetime import datetime

def scrape_news():
    url = 'https://www.sozcu.com.tr/gundem'
    response = requests.get(url)
    if response.status_code == 200:
        print("Successfully fetched the webpage")
        soup = BeautifulSoup(response.content, 'html.parser')

        # Select headlines and summaries
        headlines = soup.select('a.news-card-footer')
        summaries = soup.select('a.post-summary')

        if headlines:
            print(f"Found {len(headlines)} headlines")
        else:
            print("No headlines found")

        if summaries:
            print(f"Found {len(summaries)} summaries")
        else:
            print("No summaries found")

        news_data = []
        for i in range(len(headlines)):
            title = headlines[i].get_text(strip=True)
            try:
                summary_text = summaries[i].get_text(strip=True)
            except IndexError:
                summary_text = "Summary not available"
            print(f"Title: {title}")  # Debug print
            print(f"Summary: {summary_text}")  # Debug print
            date = datetime.now().strftime('%Y-%m-%d')
            news_data.append((date, title, summary_text))

        save_to_db(news_data)
    else:
        print(f"Failed to fetch the webpage. Status code: {response.status_code}")

def save_to_db(news_data):
    if news_data:
        try:
            conn = sqlite3.connect('news.db')
            c = conn.cursor()
            for entry in news_data:
                # Check for duplicates before inserting
                c.execute('SELECT * FROM news WHERE headline = ? AND date = ?', (entry[1], entry[0]))
                result = c.fetchone()
                if result is None:
                    # Insert new entry
                    c.execute('INSERT INTO news (date, headline, summary) VALUES (?, ?, ?)', entry)
                else:
                    # Update the summary if it was "Summary not available"
                    if result[3] == 'Summary not available':
                        c.execute('UPDATE news SET summary = ? WHERE headline = ? AND date = ?', (entry[2], entry[1], entry[0]))
            conn.commit()
            conn.close()
            print("Successfully saved news to the database")
        except Exception as e:
            print(f"Error saving to database: {e}")
    else:
        print("No news data to save to the database")

if __name__ == '__main__':
    scrape_news()
