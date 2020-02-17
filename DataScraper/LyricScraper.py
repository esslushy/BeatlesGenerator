import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

# Construct user agent
ua = UserAgent()

# Get website data into a soup
res = requests.get('https://www.brianhartzog.com/beatles/beatles-alphabetical-list-of-all-lyrics.htm', headers={'User-Agent': ua.chrome})
soup = BeautifulSoup(res.text, 'html.parser')
# Find all A tags
song_tags = soup.body.find('td', {'width': 591, 'valign': 'top', 'rowspan': 2}).findAll('a', href=True)
# Pull out links
song_links = [a['href'] for a in song_tags]
print(song_links)