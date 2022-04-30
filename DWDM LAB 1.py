
import pandas as pd
data = pd.read_csv('C:/results.csv', header=None)

data.columns = ['Date of match', 'HOME-TEAM', 'AWAY-TEAM', ' ', ' ', ' ', 'Host City','Host Country', 'Neutral ground']

k = data.head()
print(k)

