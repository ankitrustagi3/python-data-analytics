import pandas as pd
from string import ascii_uppercase as alphabet 
import pickle

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


