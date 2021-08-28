
# https://github.com/shantnu/PyEng

import pandas as pd
import cv2

folder = 'data/'
data = pd.read_csv(folder + 'review.csv', sep = '|')

repo = 'cv2/'
cascPath = repo + 'haarcascade_frontalface_default.xml'
faceCascade = cv2.CascadeClassifier(cascPath)

thumb = 'crop/'
target = 'faces/'

for idx, row in data.iterrows():
    url = row['url']
    image = cv2.imread(thumb + url + '.jpg')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    faces = faceCascade.detectMultiScale(gray, scaleFactor = 1.2, 
                                         flags = cv2.CASCADE_SCALE_IMAGE)
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
        faces = image[y : y + h, x : x + w]
        cv2.imwrite(target + url + '.jpg', faces)
