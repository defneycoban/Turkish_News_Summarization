# Turkish News Summarizer

## Project Overview
Turkish News Summarizer is a web application designed to scrape, summarize, and display news articles from various Turkish news sources. The goal of this project is to provide concise and relevant news summaries, free from biases and excessive advertisements, making it easier for users to stay informed about current events in Turkey.

## Features
- **Web Scraping:** Automatically fetches the latest news articles from specified Turkish news websites.
- **Text Summarization:** Utilizes a pre-trained transformer model to generate concise summaries of the news articles.
- **Database Storage:** Stores news articles and their summaries in an SQLite database to ensure persistence and easy retrieval.
- **Web Interface:** Provides a simple, user-friendly interface to display the latest news summaries.

## Components
- **Web Scraper (`scrape_news.py`):**
  - Fetches the latest news articles from https://www.sozcu.com.tr/gundem.
  - Extracts headlines and their summaries.
  - Stores the articles and summaries in an SQLite database.

- **Summarizer (`summarizer.py`):**
  - Uses the `transformers` library to summarize the text of the news articles.
  - Utilizes the `dbmdz/bert-base-turkish-cased` model for text summarization.

- **Database Setup (`setup_db.py`):**
  - Sets up the SQLite database and creates the necessary tables to store news articles and summaries.

- **Web Application (`app.py`):**
  - Fetches news articles from the SQLite database.
  - Renders the articles and summaries in a web interface using Flask.

- **HTML Template (`templates/index.html`):**
  - Provides a clean and simple interface to display the news articles and their summaries.
