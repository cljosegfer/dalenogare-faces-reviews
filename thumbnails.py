# https://github.com/RGGH/rng

from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser

import requests
import pandas as pd

DEVELOPER_KEY = "yourkeyhere"
channel = 'dalenogarecriticas'
folder = 'thumbnails/'

youtube = build('youtube', 'v3', developerKey=DEVELOPER_KEY)

request = youtube.channels().list(
    part = 'contentDetails', 
    forUsername = channel)
response = request.execute()

videos = []
playlist = response['items'][0]['contentDetails']['relatedPlaylists']['uploads']

token = None
while True:
    request = youtube.playlistItems().list(playlistId = playlist, 
                                           part = 'snippet', 
                                           maxResults = 50, 
                                           pageToken = token)
    response = request.execute()
    
    videos += response['items']
    token = response.get('nextPageToken')
    
    if token is None:
        break

df = pd.DataFrame(columns = ['url', 'title'])
for idx, video in enumerate(videos):
    url = (video['snippet']['thumbnails']['high']['url'])    
    name = s_name = url.split('/')[-2]
    
    r = requests.get(url, allow_redirects = True)
    open(folder + name + '.jpg', 'wb').write(r.content)
    
    title = video['snippet']['title'] 
    df = df.append({'url': name, 'title': title}, ignore_index = True)

df.to_csv('data/dalenogare.csv', index = False, sep = '|')
