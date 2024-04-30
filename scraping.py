# import the requests, BeautifulSoup
import requests
from bs4 import BeautifulSoup
# define the url to the station
url = 'https://trends.google.com/trends/explore?date=today%205-y&q=youtube'

# use the response module to get the data from the url
response = requests.get(url)

# use BeautifulSoup to parse the html data
soup = BeautifulSoup(response.content, "html.parser")

# search for the division with the id "stn_metadata"
# store it as a variable called stn_metadata
stn_metadata = soup.find("span", class_ = "font-bold")

# convert the stn_metadata to a string
stn_metadata = str(stn_metadata)
print(stn_metadata)

# split the stn_metadata
stn_metadata = stn_metadata.split('\n')

# search for the "Water depth" in the stn_metadata
for line in stn_metadata:
    if 'Water depth' in line:
        print(line)