# Fandom Wiki Scraping 

## Terms of Service and robots.txt
Before starting this project, I checked both the website’s Terms of Service and its robots.txt file.

Fandom Terms of Use:  
https://www.fandom.com/terms-of-use  

Ariana Grande Wiki robots.txt:  
https://arianagrande.fandom.com/robots.txt  

The robots.txt file allows access to most public-facing wiki pages, including the songs category page that I used. It mainly blocks certain internal or administrative pages, which I avoided.

However, the Terms of Use are stricter and state that automated scraping is not allowed without permission. Because of this, I treated this project as a small, educational exercise using only a limited amount of publicly available data. I did not attempt large-scale scraping or anything that would negatively affect the website. If this were a real research project, I would look for permission or use an official API.

## Choice of Wiki and Data Collected
I chose the Ariana Grande Wiki because I have been a huge Ariana Grande fan for the past 8 years and already have a lot of prior knowledge about her. Because of that, I was interested in seeing how her music and career are represented as data on a fan-created website.

For this project, I scraped song titles and their corresponding links from the songs category page. I focused on songs because they are clearly organized and easy to collect in a structured way.

This type of data could be useful to researchers studying digital fandom, since it shows how fans organize and present information about an artist’s work. It also reflects how online communities create their own structured archives, which can sometimes differ from official sources.

## Code Used
I used the `cloudscraper` library to request the webpage and handle bot protection, and the `BeautifulSoup` library to parse the HTML and extract the data.

## Data Output
The scraped data was saved as a CSV file (`ariana_grande_songs.csv`) in the web_scraping_assignments directory. This format makes the data easy to read, share, and analyze.
