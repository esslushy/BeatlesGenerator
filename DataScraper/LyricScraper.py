import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import pickle

# Construct user agent
ua = UserAgent()

def get_lyrics(link):
    """
      Gets all the lyrics on a webpage.

      Args:
        link: the link to the webpage with the lyrics
    """
    print(link)
    # Get data
    res = requests.get(link, headers={'User-Agent': ua.chrome})
    if res.status_code == 404:
        return
    soup = BeautifulSoup(res.text, 'html.parser')
    # Pull out lyrics
    lyric_tags = soup.body.find('td', {'width': 591, 'valign': 'top', 'rowspan': 2}).findAll('p')
    # Get only the text
    lyrics = [lyric.getText() for lyric in lyric_tags]
    # Make all values lowercase and split on new lines
    lyrics = [lyric.lower().split('\n') for lyric in lyrics]
    # Take it out of the double dimensioned array caused by the split
    lyrics = lyrics[0] 
    # Remove excess whitespace and split on word level
    lyrics = [lyric.strip().split(' ') for lyric in lyrics if lyric]
    return lyrics

# Get website data into a soup
res = requests.get('https://www.brianhartzog.com/beatles/beatles-alphabetical-list-of-all-lyrics.htm', headers={'User-Agent': ua.chrome})
soup = BeautifulSoup(res.text, 'html.parser')
# Find all A tags and store in a set to remove duplicates
song_tags = set(soup.body.find('td', {'width': 591, 'valign': 'top', 'rowspan': 2}).findAll('a', href=True))
# Pull out links. Add the start of the website to each.
song_links = ['https://www.brianhartzog.com/beatles/' + a['href'] for a in song_tags]
# Gather all the data
lyrics = []
for link in song_links:
    song = get_lyrics(link)
    if song is not None:
        lyrics.extend(song)
print(lyrics)
pickle.dump(lyrics, open('dataset/songs.pickle', 'wb'))