
import pandas as pd

folder = 'data/'
raw = pd.read_csv(folder + 'dalenogare.csv', sep = '|')

# reviews
review = raw
excluido = raw
for idx, row in raw.iterrows():
    title = row['title']
    key = 'Crítica'
    if not key in title:
        review = review.drop(index = idx)

review.to_csv(folder + 'review.csv', index = False, sep = '|')
