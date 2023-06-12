import pandas as pd
from string import ascii_uppercase as alphabet 
import pickle
from bs4 import BeautifulSoup
import requests

all_tables = pd.read_html('https://en.wikipedia.org/wiki/2022_FIFA_World_Cup')

# Each index below represents the group table with increments of 7
#all_tables[9]
# ...
#all_tables[58]
dict_table = {}
for letter, i in zip(alphabet, range(9, 65, 7)):
    df = all_tables[i]
    df.rename(columns={df.columns[1]: 'Team'}, inplace=True)
    df.pop('Qualification')
    dict_table[f'Group {letter}'] = df

# Export dictionary to external file
with open('dict_table', 'wb') as output:
    pickle.dump(dict_table, output)

def get_matches(year):
    web = f'https://en.wikipedia.org/wiki/{year}_FIFA_World_Cup'
    response = requests.get(web)
    content = response.text
    soup = BeautifulSoup(content, 'lxml')

    matches = soup.find_all('div', class_= 'footballbox')

    home = []
    away = []
    score = []

    for match in matches:
        home.append(match.find('th', class_ = 'fhome').get_text())
        score.append(match.find('th', class_ = 'fscore').get_text())
        away.append(match.find('th', class_ ='faway').get_text())

    dict_football = {'home': home, 'away': away, 'score': score}
    df_football = pd.DataFrame(dict_football)
    df_football['year'] = year

    return df_football

matchSummary = get_matches(2022)
matchSummary.to_csv('fifa_worldcup_2022.csv', index=False)