import pandas as pd
import numpy as np

# import country table, convert to a pandas dataframe and update indices
country = pd.DataFrame(pd.read_csv("C://Users/TimothyBarczak/Documents/Visual Studio Code/Tim's project/European Soccer Database/country.csv"))
country.index = ['BEL', 'ENG', 'FRA', 'GER', 'ITA', 'NET', 'POL', 'POR', 'SCO', 'ESP', 'SWI']

print(country)
print(country.loc["ITA"])
print(country.loc[["ITA", "BEL", "GER"]])

# import League table, convert to a pandas dataframe and update indices
league = pd.DataFrame(pd.read_csv("C://Users/TimothyBarczak/Documents/Visual Studio Code/Tim's project/European Soccer Database/league.csv"))
league.index = ['BJL', 'EPL', 'Lig1', 'Bund', 'SerA', 'Erie', 'Eks', 'Liga', 'SPL', 'LaLiga', 'SSL']

print(league)
print(league.loc["EPL"])
print(league.loc[["EPL", "Lig1", "Erie"]])

# import Match table, convert to a pandas dataframe
player = pd.DataFrame(pd.read_csv("C://Users/TimothyBarczak/Documents/Visual Studio Code/Tim's project/European Soccer Database/player.csv"))

print(player)
print(player.iloc[2])

# import Match table, convert to a pandas dataframe
player_attributes = pd.DataFrame(pd.read_csv("C://Users/TimothyBarczak/Documents/Visual Studio Code/Tim's project/European Soccer Database/player_attributes.csv"))

print(player_attributes.iloc[2:5,:])

# import Match table, convert to a pandas dataframe
team = pd.DataFrame(pd.read_csv("C://Users/TimothyBarczak/Documents/Visual Studio Code/Tim's project/European Soccer Database/team.csv"))

print(team.iloc[2:5,:])

# import Match table, convert to a pandas dataframe
team_attributes = pd.DataFrame(pd.read_csv("C://Users/TimothyBarczak/Documents/Visual Studio Code/Tim's project/European Soccer Database/team_attributes.csv"))

print(team_attributes.iloc[2:5,:])