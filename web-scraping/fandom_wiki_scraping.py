import cloudscraper
import csv
from bs4 import BeautifulSoup

scraper = cloudscraper.create_scraper()

def get_song_data(url):
    try:
        response = scraper.get(url, timeout=10)
        if response.status_code != 200:
            return []

        soup = BeautifulSoup(response.text, "html.parser")
        songs = soup.find_all('a', class_='category-page__member-link')

        songs_data = []

        for song in songs:
            song_data = {
                "song_title": song.get_text(),
                "song_link": "https://arianagrande.fandom.com" + song.get('href')
            }
            songs_data.append(song_data)

        return songs_data

    except Exception as e:
        print(f"Error getting song data from {url}: {e}")
        return []

songs_data = get_song_data("https://arianagrande.fandom.com/wiki/Category:Songs")

with open('ariana_grande_songs.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['song_title', 'song_link'])

    for song in songs_data:
        writer.writerow([song['song_title'], song['song_link']])

print("Done scraping Ariana Grande songs")
