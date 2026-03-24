import cloudscraper
import csv
from bs4 import BeautifulSoup

scraper = cloudscraper.create_scraper()

response = scraper.get("https://arianagrande.fandom.com/wiki/Category:Songs", timeout=10)
print("Status code:", response.status_code)

soup = BeautifulSoup(response.text, "html.parser")

# fallback: search entire page but filter properly
songs = soup.find_all("a", href=True)

songs_data = []

for song in songs:
    title = song.get_text(strip=True)
    href = song.get("href")

    if href.startswith("/wiki/") and "Category:" not in href and title:
        songs_data.append({
            "song_title": title,
            "song_link": "https://arianagrande.fandom.com" + href
        })

# remove duplicates
unique = []
seen = set()

for song in songs_data:
    if song["song_link"] not in seen:
        seen.add(song["song_link"])
        unique.append(song)

print("Number of songs found:", len(unique))

with open("ariana_grande_songs.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["song_title", "song_link"])

    for song in unique:
        writer.writerow([song["song_title"], song["song_link"]])

print("Done scraping Ariana Grande songs")
