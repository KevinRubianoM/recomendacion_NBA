import pandas as pd
from nba_api.stats.static import teams



#IMPLEMENTACIÓN DEL MODELO

# IDs de los equipos 

nba_teams = teams.get_teams()
team_ids = [team['id'] for team in nba_teams]
team_names = [team['abbreviation'] for team in nba_teams]


#Lectura de los conjuntos de datos 

raw19_20 = pd.read_table("0raw_stats_2019_20.csv",delimiter=",",header=0)

raw20_21 = pd.read_table("0raw_stats_2020_21.csv",delimiter=",",header=0)

raw21_22 = pd.read_table("0raw_stats_2021_22.csv",delimiter=",",header=0)

raw22_23 = pd.read_table("0raw_stats_2022_23.csv",delimiter=",",header=0)

raw_players = pd.read_table("raw_players_bios.csv",delimiter=",",header=0)

raw_teams = pd.read_table("raw_teams_stats.csv",delimiter=",",header=0)


#Nombres de las variables 

playerVSteamVARS = raw19_20.columns.to_list()

'''
VARIABLES JUGADORES CONTRA EQUIPOS

SEASON_ID: The identifier for the NBA season in which the game took place.
Player_ID: Unique identifier for the player.
Game_ID: Unique identifier for the game.
WL: Indicates whether the player's team won ('W') or lost ('L') the game.
MIN: The number of minutes the player was on the court during the game.
FGM: Field goals made by the player.
FGA: Field goals attempted by the player.
FG_PCT: Field goal percentage, calculated as FGM divided by FGA.
FG3M: Three-point field goals made by the player.
FG3A: Three-point field goals attempted by the player.
FG3_PCT: Three-point field goal percentage, calculated as FG3M divided by FG3A.
FTM: Free throws made by the player.
FTA: Free throws attempted by the player.
FT_PCT: Free throw percentage, calculated as FTM divided by FTA.
OREB: Offensive rebounds grabbed by the player.
DREB: Defensive rebounds grabbed by the player.
REB: Total rebounds grabbed by the player (OREB + DREB).
AST: Assists made by the player.
STL: Steals made by the player.
BLK: Blocks made by the player.
TOV: Turnovers committed by the player.
PF: Personal fouls committed by the player.
PTS: Total points scored by the player.
PLUS_MINUS: Plus-minus statistic, which represents the point differential when the player was on the court.
Player: Name of the player.
TeamID: Unique identifier for the player's team.
Opponent: Name of the opposing team.
Location: Indicates whether the game was played at home ('Home') or away ('Away') for the player's team.

'''

playersVARS = raw_players.columns.to_list()

'''
VARIABLES DE JUGADORES

1. PLAYER_ID: The unique identifier for the player.
2. PLAYER_NAME: The name of the player.
3. TEAM_ID: The unique identifier for the team the player belongs to.
4. TEAM_ABBREVIATION: The abbreviation or code for the team the player belongs to.
5. AGE: The age of the player.
6. PLAYER_HEIGHT: The height of the player (in feet).
7. PLAYER_HEIGHT_INCHES: The additional height of the player (in inches).
8. PLAYER_WEIGHT: The weight of the player (in pounds).
9. COLLEGE: The college the player attended.
10. COUNTRY: The country of origin of the player.
11. DRAFT_YEAR: The year in which the player was drafted.
12. DRAFT_ROUND: The round in which the player was drafted.
13. DRAFT_NUMBER: The draft position or number of the player.
14. GP: The number of games played by the player.
15. PTS: The average points scored per game by the player.
16. REB: The average rebounds grabbed per game by the player.
17. AST: The average assists made per game by the player.
18. NET_RATING: The net rating of the player, which measures the point differential per 100 possessions when the player is on the court.
19. OREB_PCT: The offensive rebound percentage of the player.
20. DREB_PCT: The defensive rebound percentage of the player.
21. USG_PCT: The usage percentage of the player, which measures the percentage of team plays used by the player while on the court.
22. TS_PCT: The true shooting percentage of the player, which takes into account field goals, three-pointers, and free throws.
23. AST_PCT: The assist percentage of the player, which measures the percentage of teammate field goals the player assisted on while on the court.

'''
teamsVARS = raw_teams.columns.to_list()

'''
VARIABLES DE EQUIPOS

1. TEAM_ID: The unique identifier for the team.
2. TEAM_ABBREVIATION: The abbreviation or code for the team.
3. W: The number of wins by the team.
4. L: The number of losses by the team.
5. PCT: The winning percentage of the team.
6. CONF_RANK: The ranking of the team within its conference.
7. DIV_RANK: The ranking of the team within its division.
8. MIN_YEAR: The earliest season in which the team existed.
9. PTS_RANK: The ranking of the team in terms of points scored.
10. PTS_PG: The average points scored per game by the team.
11. REB_RANK: The ranking of the team in terms of rebounds.
12. REB_PG: The average rebounds grabbed per game by the team.
13. AST_RANK: The ranking of the team in terms of assists.
14. AST_PG: The average assists made per game by the team.
15. OPP_PTS_RANK: The ranking of the team in terms of points allowed to opponents.
16. OPP_PTS_PG: The average points allowed per game by the team.
17. WINS: The total number of wins by the team.
18. LOSSES: The total number of losses by the team.
19. WIN_PCT: The overall winning percentage of the team.
20. CONF_RANK.1: Another representation of the team's ranking within its conference.
21. DIV_RANK.1: Another representation of the team's ranking within its division.
22. PO_WINS: The number of playoff wins by the team.
23. PO_LOSSES: The number of playoff losses by the team.
24. FGM: The total field goals made by the team.
25. FGA: The total field goals attempted by the team.
26. FG_PCT: The field goal percentage of the team.
27. FG3M: The total three-point field goals made by the team.
28. FG3A: The total three-point field goals attempted by the team.
29. FG3_PCT: The three-point field goal percentage of the team.
30. FTM: The total free throws made by the team.
31. FTA: The total free throws attempted by the team.
32. FT_PCT: The free throw percentage of the team.
33. OREB: The total offensive rebounds grabbed by the team.
34. DREB: The total defensive rebounds grabbed by the team.
35. REB: The total rebounds grabbed by the team.
36. AST: The total assists made by the team.
37. PF: The total personal fouls committed by the team.
38. STL: The total steals made by the team.
39. TOV: The total turnovers committed by the team.
40. BLK: The total blocks made by the team.
41. PTS: The total points scored by the team.
42. PTS_RANK.1: Another representation of the team's ranking in terms of points scored.

'''


# ESTABLECER RATINGS DE UN JUGADOR CONTRA UN EQUIPO


'''
To create a measure of the overall performance of the NBA player during the game, 
we can consider multiple performance metrics and assign weights to each based on their importance. 
Here's one way to calculate an overall performance score:

Start with a base score of 0.
Add points for positive contributions:
Add 1 point for each made three-pointer (FG3M).
Add 1 points for each made free throw (FTM).
Add 0.5 points for each defensive rebound (DREB).
Add 1.5 points for each assist (AST).
Add 2 points for each steal (STL).
Add 2 points for each block (BLK).
Deduct points for negative contributions:
Deduct 0.5 points for each missed field goal (FGA) or missed three-pointer (FG3A).
Deduct 1.5 points for each missed free throw (FTA).
Deduct 1 point for each turnover (TOV).
Deduct 0.5 points for each personal foul (PF).

Add the plus-minus statistic (PLUS_MINUS) directly to the score.

Scale the score based on playing time:
Multiply the score by a factor of 48 (minutes in a full game) divided by the player's minutes played (MIN).

The resulting score represents the overall performance of the NBA player during the game, 
considering their contributions and various performance metrics.

'''
                
#Ver variables significativas
#Se escoge explicar la variable PLUS_MINUS

import statsmodels.api as sm

y = raw19_20['PLUS_MINUS']

#Con y sin FGM
X=raw19_20.loc[:,['FG3M','FTM','OREB','DREB','AST','STL','BLK','FGA','FG3A','FTA','TOV','PF','MIN']]

# Add a constant term to the independent variable
X = sm.add_constant(X)

# Create a model and fit it
model = sm.OLS(y, X)
results = model.fit()

# Print the model summary
print(results.summary())

# Se decide no incluir en la creación del SCORE las variables FGM ni OREB
#Esto por cuestiones de multicolinealidad

#En la temporada 2019-20 

#Crear los scores de todos los jugadores contra todos los enquipos en la temporada 

scores19_20 = pd.DataFrame()
teamVS=pd.DataFrame()

for team_name in team_names:
    
    score=0
    
    teamVS=raw19_20.loc[raw19_20['Opponent'] == team_name]
    
    teamVS['SCORE']=score+((1*teamVS['FG3M'])+(1*teamVS['FTM'])+(0.5*teamVS['DREB'])+(1.5*teamVS['AST'])+(2*teamVS['STL'])+(2*teamVS['BLK'])-(0.5*teamVS['FG3A'])-(1.5*teamVS['FTA'])-(1*teamVS['TOV'])-(0.5*teamVS['PF'])+teamVS['PLUS_MINUS'])*(48/teamVS['MIN'])
    
    teamVS =  (teamVS
              .groupby(["Player_ID","Player","TeamID","Opponent"])
              .agg(score=("SCORE","sum")).reset_index())
    
    scores19_20=pd.concat([scores19_20,teamVS],axis=0)

#En la temporada 2020-21 

#Crear los scores de todos los jugadores contra todos los enquipos en la temporada 

scores20_21 = pd.DataFrame()
teamVS=pd.DataFrame()

for team_name in team_names:
    
    score=0
    
    teamVS=raw20_21.loc[raw20_21['Opponent'] == team_name]
    
    teamVS['SCORE']=score+((1*teamVS['FG3M'])+(1*teamVS['FTM'])+(0.5*teamVS['DREB'])+(1.5*teamVS['AST'])+(2*teamVS['STL'])+(2*teamVS['BLK'])-(0.5*teamVS['FG3A'])-(1.5*teamVS['FTA'])-(1*teamVS['TOV'])-(0.5*teamVS['PF'])+teamVS['PLUS_MINUS'])*(48/teamVS['MIN'])
    
    teamVS =  (teamVS
              .groupby(["Player_ID","Player","TeamID","Opponent"])
              .agg(score=("SCORE","sum")).reset_index())
    
    scores20_21=pd.concat([scores20_21,teamVS],axis=0)

#En la temporada 2021_22 

#Crear los scores de todos los jugadores contra todos los enquipos en la temporada 

scores21_22 = pd.DataFrame()
teamVS=pd.DataFrame()

for team_name in team_names:
    
    score=0
    
    teamVS=raw21_22.loc[raw21_22['Opponent'] == team_name]
    
    teamVS['SCORE']=score+((1*teamVS['FG3M'])+(1*teamVS['FTM'])+(0.5*teamVS['DREB'])+(1.5*teamVS['AST'])+(2*teamVS['STL'])+(2*teamVS['BLK'])-(0.5*teamVS['FG3A'])-(1.5*teamVS['FTA'])-(1*teamVS['TOV'])-(0.5*teamVS['PF'])+teamVS['PLUS_MINUS'])*(48/teamVS['MIN'])
    
    teamVS =  (teamVS
              .groupby(["Player_ID","Player","TeamID","Opponent"])
              .agg(score=("SCORE","sum")).reset_index())
    
    scores21_22=pd.concat([scores21_22,teamVS],axis=0)

#En la temporada 2022_23 

#Crear los scores de todos los jugadores contra todos los enquipos en la temporada 

scores22_23 = pd.DataFrame()
teamVS=pd.DataFrame()

for team_name in team_names:
    
    score=0
    
    teamVS=raw22_23.loc[raw22_23['Opponent'] == team_name]
    
    teamVS['SCORE']=score+((1*teamVS['FG3M'])+(1*teamVS['FTM'])+(0.5*teamVS['DREB'])+(1.5*teamVS['AST'])+(2*teamVS['STL'])+(2*teamVS['BLK'])-(0.5*teamVS['FG3A'])-(1.5*teamVS['FTA'])-(1*teamVS['TOV'])-(0.5*teamVS['PF'])+teamVS['PLUS_MINUS'])*(48/teamVS['MIN'])
    
    teamVS =  (teamVS
              .groupby(["Player_ID","Player","TeamID","Opponent"])
              .agg(score=("SCORE","sum")).reset_index())
    
    scores22_23=pd.concat([scores22_23,teamVS],axis=0)

#MATRICES DE INTERACCIONES 

intMat19_20 = pd.pivot_table(scores19_20, values='score', index='Opponent', columns='Player')

intMat20_21 = pd.pivot_table(scores20_21, values='score', index='Opponent', columns='Player')

intMat21_22 = pd.pivot_table(scores21_22, values='score', index='Opponent', columns='Player')

intMat22_23 = pd.pivot_table(scores22_23, values='score', index='Opponent', columns='Player')

intMat22_23_00_ = pd.pivot_table(scores22_23, values='score', index='Opponent', columns='Player')

intMat22_23_00_nan= pd.pivot_table(scores22_23, values='score', index='Opponent', columns='Player')

#Se computan otros posibles scores

'''
AJUSTE DE OTRO SCORE
Overall Performance Score = w1 * Points + w2 * Rebounds + w3 * Assists + w4 * Steals + w5 * Blocks - w6 * Turnovers

w1 = 1.0
w2 = 0.9
w3 = 0.8
w4 = 0.5
w5 = 0.5
w6 = 0.7
'''

#En la temporada 2022_23 

#Crear los scores de todos los jugadores contra todos los enquipos en la temporada 

scores_0_22_23 = pd.DataFrame()
teamVS=pd.DataFrame()

for team_name in team_names:
    
    score=0
    
    teamVS=raw22_23.loc[raw22_23['Opponent'] == team_name]
    
    teamVS['SCORE']=score+((1*teamVS['PTS'])+(0.9*teamVS['REB'])+(0.8*teamVS['AST'])+(0.5*teamVS['STL'])+(0.5*teamVS['BLK'])+(0.7*teamVS['TOV']))*(48/teamVS['MIN'])
    
    teamVS =  (teamVS
              .groupby(["Player_ID","Player","TeamID","Opponent"])
              .agg(score=("SCORE","sum")).reset_index())
    
    scores_0_22_23=pd.concat([scores_0_22_23,teamVS],axis=0)

#En la temporada 2022_23 

#Crear los scores de todos los jugadores contra todos los enquipos en la temporada 

scores_0_21_22 = pd.DataFrame()
teamVS=pd.DataFrame()

for team_name in team_names:
    
    score=0
    
    teamVS=raw21_22.loc[raw21_22['Opponent'] == team_name]
    
    teamVS['SCORE']=score+((1*teamVS['PTS'])+(0.9*teamVS['REB'])+(0.8*teamVS['AST'])+(0.5*teamVS['STL'])+(0.5*teamVS['BLK'])+(0.7*teamVS['TOV']))*(48/teamVS['MIN'])
    
    teamVS =  (teamVS
              .groupby(["Player_ID","Player","TeamID","Opponent"])
              .agg(score=("SCORE","sum")).reset_index())
    
    scores_0_21_22=pd.concat([scores_0_21_22,teamVS],axis=0)

#En la temporada 2020_21 

#Crear los scores de todos los jugadores contra todos los enquipos en la temporada 

scores_0_20_21 = pd.DataFrame()
teamVS=pd.DataFrame()

for team_name in team_names:
    
    score=0
    
    teamVS=raw20_21.loc[raw20_21['Opponent'] == team_name]
    
    teamVS['SCORE']=score+((1*teamVS['PTS'])+(0.9*teamVS['REB'])+(0.8*teamVS['AST'])+(0.5*teamVS['STL'])+(0.5*teamVS['BLK'])+(0.7*teamVS['TOV']))*(48/teamVS['MIN'])
    
    teamVS =  (teamVS
              .groupby(["Player_ID","Player","TeamID","Opponent"])
              .agg(score=("SCORE","sum")).reset_index())
    
    scores_0_20_21=pd.concat([scores_0_20_21,teamVS],axis=0)

#En la temporada 2019_20 

#Crear los scores de todos los jugadores contra todos los enquipos en la temporada 

scores_0_19_20 = pd.DataFrame()
teamVS=pd.DataFrame()

for team_name in team_names:
    
    score=0
    
    teamVS=raw19_20.loc[raw19_20['Opponent'] == team_name]
    
    teamVS['SCORE']=score+((1*teamVS['PTS'])+(0.9*teamVS['REB'])+(0.8*teamVS['AST'])+(0.5*teamVS['STL'])+(0.5*teamVS['BLK'])+(0.7*teamVS['TOV']))*(48/teamVS['MIN'])
    
    teamVS =  (teamVS
              .groupby(["Player_ID","Player","TeamID","Opponent"])
              .agg(score=("SCORE","sum")).reset_index())
    
    scores_0_19_20=pd.concat([scores_0_19_20,teamVS],axis=0)


#MATRICES DE INTERACCIONES 

intMat_0_19_20 = pd.pivot_table(scores_0_19_20, values='score', index='Opponent', columns='Player')

intMat_0_20_21 = pd.pivot_table(scores_0_20_21, values='score', index='Opponent', columns='Player')

intMat_0_21_22 = pd.pivot_table(scores_0_21_22, values='score', index='Opponent', columns='Player')

intMat_0_22_23 = pd.pivot_table(scores_0_22_23, values='score', index='Opponent', columns='Player')




