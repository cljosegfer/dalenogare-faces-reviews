
import pandas as pd

folder = 'data/'
raw = pd.read_csv(folder + 'review.csv', sep = '|')
clean = pd.read_csv(folder + 'clean.csv', header = None)
clean['title'] = ''
clean.columns = raw.columns

# reviews
for idx, row in clean.iterrows():
    url = row['url'][:-4]
    line = raw[raw['url'] == url]
    clean.loc[idx] = [line.iloc[0, 0], line.iloc[0, 1]]

clean.to_csv(folder + 'clean.csv', index = False, sep = '|')
    