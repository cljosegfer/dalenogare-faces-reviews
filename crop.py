
import pandas as pd
from PIL import Image

folder = 'data/'
data = pd.read_csv(folder + 'review.csv', sep = '|')

thumb = 'thumbnails/'
target = 'crop/'

for idx, row in data.iterrows():
    url = row['url']
    im = Image.open(thumb + url + '.jpg')
    
    width, height = im.size
    
    left = 0
    top = 0
    bottom = height
    right = width / 4

    crop = im.crop((left, top, right, bottom))
    crop.save(target + url + '.jpg')
