import pandas as pd
from nba_api.stats.static import teams
from nba_api.stats.endpoints import commonteamroster
from nba_api.stats.endpoints import playergamelog
from nba_api.stats.endpoints import leaguedashplayerbiostats
from nba_api.stats.endpoints import teaminfocommon
from nba_api.stats.endpoints import teamyearbyyearstats


import requests

#Extraer historial de enfrentamientos de cada jugador contra todos los quipos
#durante las últimas 4 temporadas regulares.


#Extraer hitorial de enfrentamientos (para construir matriz de interacciones)

def get_team_player_stats(team_id):
    # Set the timeout duration for the API request
    timeout_duration = 60
    
    try:
        # Get the roster of the team for the 2022-23 season
        roster = commonteamroster.CommonTeamRoster(team_id=team_id, season='2022-23',timeout=timeout_duration)
        team_roster = roster.get_data_frames()[0]

        # Retrieve the player IDs from the roster
        player_ids = team_roster['PLAYER_ID'].tolist()

    except requests.Timeout:
        print(f"Request for team {team_id} timed out.")

    # Create an empty dataframe to store the player stats
    all_players_stats = pd.DataFrame()

    # Iterate over each player ID
    for player_id in player_ids:
        player_info = team_roster.loc[team_roster['PLAYER_ID'] == player_id]
        player_name = player_info['PLAYER'].values[0]

        try:
            # Retrieve the player's game logs for the regular season
            player_log = playergamelog.PlayerGameLog(player_id=player_id, season='2022-23', season_type_all_star='Regular Season',timeout= timeout_duration)
            player_log_df = player_log.get_data_frames()[0]

            # Add player name and team ID as columns in the dataframe
            player_log_df['Player'] = player_name
            player_log_df['TeamID'] = team_id

            # Append player's game logs to the main dataframe
            all_players_stats = pd.concat([all_players_stats, player_log_df], ignore_index=True)

        except requests.Timeout:
            print(f"Request for player {player_name} timed out.")

    return all_players_stats


# Get all team IDs
nba_teams = teams.get_teams()
team_ids = [team['id'] for team in nba_teams]
team_names = [team['abbreviation'] for team in nba_teams]


atl = get_team_player_stats(team_ids[0]) #

bos = get_team_player_stats(team_ids[1]) #

cle = get_team_player_stats(team_ids[2]) #

nop = get_team_player_stats(team_ids[3]) #

chi = get_team_player_stats(team_ids[4]) #

dal = get_team_player_stats(team_ids[5]) #

den = get_team_player_stats(team_ids[6])  #

gsw = get_team_player_stats(team_ids[7]) #

hou = get_team_player_stats(team_ids[8]) #

lac = get_team_player_stats(team_ids[9]) #

lal = get_team_player_stats(team_ids[10]) #

mia = get_team_player_stats(team_ids[11]) #

mil = get_team_player_stats(team_ids[12]) #

minn = get_team_player_stats(team_ids[13]) #

bkn = get_team_player_stats(team_ids[14]) #

nyk = get_team_player_stats(team_ids[15]) #

orl = get_team_player_stats(team_ids[16]) #

ind = get_team_player_stats(team_ids[17]) #

phi = get_team_player_stats(team_ids[18]) #

phx = get_team_player_stats(team_ids[19]) #

por = get_team_player_stats(team_ids[20]) #

sac = get_team_player_stats(team_ids[21]) #

sas = get_team_player_stats(team_ids[22]) #

okc = get_team_player_stats(team_ids[23]) #

tor = get_team_player_stats(team_ids[24])#

uta = get_team_player_stats(team_ids[25]) #

mem = get_team_player_stats(team_ids[26]) #

was = get_team_player_stats(team_ids[27]) #

det = get_team_player_stats(team_ids[28]) #

cha = get_team_player_stats(team_ids[29]) #


stats_2022_23 = pd.concat([atl,bos,cle,nop,chi,dal,den,gsw,hou,lac,lal,mia,mil,minn,bkn,nyk,orl,ind,phi,phx,por,sac,sas,okc,tor,uta,mem,was,det,cha], axis=0)
stats_2022_23.to_csv('raw_stats_2022_23.csv', index=False)


#PARA LA TEMPORADA 2021-2022

def get_team_player_stats(team_id):
    # Set the timeout duration for the API request
    timeout_duration = 60
    
    try:
        # Get the roster of the team for the 2021-22 season
        roster = commonteamroster.CommonTeamRoster(team_id=team_id, season='2021-22',timeout=timeout_duration)
        team_roster = roster.get_data_frames()[0]

        # Retrieve the player IDs from the roster
        player_ids = team_roster['PLAYER_ID'].tolist()

    except requests.Timeout:
        print(f"Request for team {team_id} timed out.")

    # Create an empty dataframe to store the player stats
    all_players_stats = pd.DataFrame()

    # Iterate over each player ID
    for player_id in player_ids:
        player_info = team_roster.loc[team_roster['PLAYER_ID'] == player_id]
        player_name = player_info['PLAYER'].values[0]

        try:
            # Retrieve the player's game logs for the regular season
            player_log = playergamelog.PlayerGameLog(player_id=player_id, season='2021-22', season_type_all_star='Regular Season',timeout= timeout_duration)
            player_log_df = player_log.get_data_frames()[0]

            # Add player name and team ID as columns in the dataframe
            player_log_df['Player'] = player_name
            player_log_df['TeamID'] = team_id

            # Append player's game logs to the main dataframe
            all_players_stats = pd.concat([all_players_stats, player_log_df], ignore_index=True)

        except requests.Timeout:
            print(f"Request for player {player_name} timed out.")

    return all_players_stats

atl21 = get_team_player_stats(team_ids[0]) #

bos21 = get_team_player_stats(team_ids[1]) #

cle21 = get_team_player_stats(team_ids[2]) #

nop21 = get_team_player_stats(team_ids[3]) #

chi21 = get_team_player_stats(team_ids[4]) #

dal21 = get_team_player_stats(team_ids[5]) #

den21 = get_team_player_stats(team_ids[6]) #

gsw21 = get_team_player_stats(team_ids[7]) #

hou21 = get_team_player_stats(team_ids[8]) #

lac21 = get_team_player_stats(team_ids[9]) #

lal21 = get_team_player_stats(team_ids[10]) #

mia21 = get_team_player_stats(team_ids[11]) #

mil21 = get_team_player_stats(team_ids[12]) #

minn21 = get_team_player_stats(team_ids[13]) #

bkn21 = get_team_player_stats(team_ids[14]) #

nyk21 = get_team_player_stats(team_ids[15]) #

orl21 = get_team_player_stats(team_ids[16]) #

ind21 = get_team_player_stats(team_ids[17]) #

phi21 = get_team_player_stats(team_ids[18]) #

phx21 = get_team_player_stats(team_ids[19]) #

por21 = get_team_player_stats(team_ids[20]) #

sac21 = get_team_player_stats(team_ids[21]) #

sas21 = get_team_player_stats(team_ids[22]) #

okc21 = get_team_player_stats(team_ids[23]) #

tor21 = get_team_player_stats(team_ids[24])#

uta21 = get_team_player_stats(team_ids[25]) #

mem21 = get_team_player_stats(team_ids[26]) #

was21 = get_team_player_stats(team_ids[27]) #

det21 = get_team_player_stats(team_ids[28]) #

cha21 = get_team_player_stats(team_ids[29]) #


stats_2021_22 = pd.concat([atl21,bos21,cle21,nop21,chi21,dal21,den21,gsw21,hou21,lac21,lal21,mia21,mil21,minn21,bkn21,nyk21,orl21,ind21,phi21,phx21,por21,sac21,sas21,okc21,tor21,uta21,mem21,was21,det21,cha21], axis=0)
stats_2021_22.to_csv('raw_stats_2021_22.csv', index=False)


#PARA LA TEMPORADA 2020-2021

def get_team_player_stats(team_id):
    # Set the timeout duration for the API request
    timeout_duration = 60
    
    try:
        # Get the roster of the team for the 2020-21 season
        roster = commonteamroster.CommonTeamRoster(team_id=team_id, season='2020-21',timeout=timeout_duration)
        team_roster = roster.get_data_frames()[0]

        # Retrieve the player IDs from the roster
        player_ids = team_roster['PLAYER_ID'].tolist()

    except requests.Timeout:
        print(f"Request for team {team_id} timed out.")

    # Create an empty dataframe to store the player stats
    all_players_stats = pd.DataFrame()

    # Iterate over each player ID
    for player_id in player_ids:
        player_info = team_roster.loc[team_roster['PLAYER_ID'] == player_id]
        player_name = player_info['PLAYER'].values[0]

        try:
            # Retrieve the player's game logs for the regular season
            player_log = playergamelog.PlayerGameLog(player_id=player_id, season='2020-21', season_type_all_star='Regular Season',timeout= timeout_duration)
            player_log_df = player_log.get_data_frames()[0]

            # Add player name and team ID as columns in the dataframe
            player_log_df['Player'] = player_name
            player_log_df['TeamID'] = team_id

            # Append player's game logs to the main dataframe
            all_players_stats = pd.concat([all_players_stats, player_log_df], ignore_index=True)

        except requests.Timeout:
            print(f"Request for player {player_name} timed out.")

    return all_players_stats


atl20 = get_team_player_stats(team_ids[0]) #

bos20 = get_team_player_stats(team_ids[1]) #

cle20 = get_team_player_stats(team_ids[2]) #

nop20 = get_team_player_stats(team_ids[3]) #

chi20 = get_team_player_stats(team_ids[4]) #

dal20 = get_team_player_stats(team_ids[5]) #

den20 = get_team_player_stats(team_ids[6]) #

gsw20 = get_team_player_stats(team_ids[7]) #

hou20 = get_team_player_stats(team_ids[8]) #

lac20 = get_team_player_stats(team_ids[9]) #

lal20 = get_team_player_stats(team_ids[10]) #

mia20 = get_team_player_stats(team_ids[11]) #

mil20 = get_team_player_stats(team_ids[12]) #

minn20 = get_team_player_stats(team_ids[13]) #

bkn20 = get_team_player_stats(team_ids[14]) #

nyk20 = get_team_player_stats(team_ids[15]) #

orl20 = get_team_player_stats(team_ids[16]) #

ind20 = get_team_player_stats(team_ids[17]) #

phi20 = get_team_player_stats(team_ids[18]) #

phx20 = get_team_player_stats(team_ids[19]) #

por20 = get_team_player_stats(team_ids[20]) #

sac20 = get_team_player_stats(team_ids[21]) #

sas20 = get_team_player_stats(team_ids[22]) #

okc20 = get_team_player_stats(team_ids[23]) #

tor20 = get_team_player_stats(team_ids[24])#

uta20 = get_team_player_stats(team_ids[25]) #

mem20 = get_team_player_stats(team_ids[26]) #

was20 = get_team_player_stats(team_ids[27]) #

det20 = get_team_player_stats(team_ids[28]) #

cha20 = get_team_player_stats(team_ids[29]) #


stats_2020_21 = pd.concat([atl20,bos20,cle20,nop20,chi20,dal20,den20,gsw20,hou20,lac20,lal20,mia20,mil20,minn20,bkn20,nyk20,orl20,ind20,phi20,phx20,por20,sac20,sas20,okc20,tor20,uta20,mem20,was20,det20,cha20], axis=0)
stats_2020_21.to_csv('raw_stats_2020_21.csv', index=False)


#PARA LA TEMPORADA 2019-2020

def get_team_player_stats(team_id):
    # Set the timeout duration for the API request
    timeout_duration = 60
    
    try:
        # Get the roster of the team for the 2019-20 season
        roster = commonteamroster.CommonTeamRoster(team_id=team_id, season='2019-20',timeout=timeout_duration)
        team_roster = roster.get_data_frames()[0]

        # Retrieve the player IDs from the roster
        player_ids = team_roster['PLAYER_ID'].tolist()

    except requests.Timeout:
        print(f"Request for team {team_id} timed out.")

    # Create an empty dataframe to store the player stats
    all_players_stats = pd.DataFrame()

    # Iterate over each player ID
    for player_id in player_ids:
        player_info = team_roster.loc[team_roster['PLAYER_ID'] == player_id]
        player_name = player_info['PLAYER'].values[0]

        try:
            # Retrieve the player's game logs for the regular season
            player_log = playergamelog.PlayerGameLog(player_id=player_id, season='2019-20', season_type_all_star='Regular Season',timeout= timeout_duration)
            player_log_df = player_log.get_data_frames()[0]

            # Add player name and team ID as columns in the dataframe
            player_log_df['Player'] = player_name
            player_log_df['TeamID'] = team_id

            # Append player's game logs to the main dataframe
            all_players_stats = pd.concat([all_players_stats, player_log_df], ignore_index=True)

        except requests.Timeout:
            print(f"Request for player {player_name} timed out.")

    return all_players_stats


atl19 = get_team_player_stats(team_ids[0])  #

bos19 = get_team_player_stats(team_ids[1]) #

cle19 = get_team_player_stats(team_ids[2]) #

nop19 = get_team_player_stats(team_ids[3]) #

chi19 = get_team_player_stats(team_ids[4]) #

dal19 = get_team_player_stats(team_ids[5]) #

den19 = get_team_player_stats(team_ids[6])  #

gsw19 = get_team_player_stats(team_ids[7]) #

hou19 = get_team_player_stats(team_ids[8]) #

lac19 = get_team_player_stats(team_ids[9]) #

lal19 = get_team_player_stats(team_ids[10]) #

mia19 = get_team_player_stats(team_ids[11]) #

mil19 = get_team_player_stats(team_ids[12]) #

minn19 = get_team_player_stats(team_ids[13]) #

bkn19 = get_team_player_stats(team_ids[14]) #

nyk19 = get_team_player_stats(team_ids[15]) #

orl19 = get_team_player_stats(team_ids[16]) #

ind19 = get_team_player_stats(team_ids[17]) #

phi19 = get_team_player_stats(team_ids[18]) #

phx19 = get_team_player_stats(team_ids[19]) #

por19 = get_team_player_stats(team_ids[20]) # 

sac19 = get_team_player_stats(team_ids[21]) #

sas19 = get_team_player_stats(team_ids[22]) #

okc19 = get_team_player_stats(team_ids[23]) #

tor19 = get_team_player_stats(team_ids[24]) #

uta19 = get_team_player_stats(team_ids[25]) #

mem19 = get_team_player_stats(team_ids[26]) #

was19 = get_team_player_stats(team_ids[27]) #

det19 = get_team_player_stats(team_ids[28]) #

cha19 = get_team_player_stats(team_ids[29]) #


stats_2019_20 = pd.concat([atl19,bos19,cle19,nop19,chi19,dal19,den19,gsw19,hou19,lac19,lal19,mia19,mil19,minn19,bkn19,nyk19,orl19,ind19,phi19,phx19,por19,sac19,sas19,okc19,tor19,uta19,mem19,was19,det19,cha19], axis=0)

stats_2019_20.to_csv('raw_stats_2019_20.csv', index=False)


#Pre- procesamiento de los datos por temporada

#Crear la variable oponente 
stats_2022_23['Opponent'] = stats_2022_23['MATCHUP'].str.split().str[-1]
stats_2021_22['Opponent'] = stats_2021_22['MATCHUP'].str.split().str[-1]
stats_2020_21['Opponent'] = stats_2020_21['MATCHUP'].str.split().str[-1]
stats_2019_20['Opponent'] = stats_2019_20['MATCHUP'].str.split().str[-1]

#Crear la variable location

def get_location(game_desc):
    if '@' in game_desc:
        return 'Away'
    elif 'vs' in game_desc:
        return 'Home'
    else:
        return 'Unknown'

stats_2022_23['Location'] = stats_2022_23['MATCHUP'].apply(get_location)
stats_2021_22['Location'] = stats_2021_22['MATCHUP'].apply(get_location)
stats_2020_21['Location'] = stats_2020_21['MATCHUP'].apply(get_location)
stats_2019_20['Location'] = stats_2019_20['MATCHUP'].apply(get_location)

#Borrar 3 variables innecesarias

stats_2022_23 = stats_2022_23.drop(['GAME_DATE','MATCHUP','VIDEO_AVAILABLE'], axis=1)
stats_2021_22 = stats_2021_22.drop(['GAME_DATE','MATCHUP','VIDEO_AVAILABLE'], axis=1)
stats_2020_21 = stats_2020_21.drop(['GAME_DATE','MATCHUP','VIDEO_AVAILABLE'], axis=1)
stats_2019_20 = stats_2019_20.drop(['GAME_DATE','MATCHUP','VIDEO_AVAILABLE'], axis=1)

#Guardar

stats_2022_23.to_csv('0raw_stats_2022_23.csv', index=False)
stats_2021_22.to_csv('0raw_stats_2021_22.csv', index=False)
stats_2020_21.to_csv('0raw_stats_2020_21.csv', index=False)
stats_2019_20.to_csv('0raw_stats_2019_20.csv', index=False)



#Extraer información general de los jugadores (Item Features)

# Request player biostats for all teams
player_bio_stats = leaguedashplayerbiostats.LeagueDashPlayerBioStats()

# Retrieve data from the API
players_bios = player_bio_stats.get_data_frames()[0]

players_bios.info()

players_bios.to_csv('raw_players_bios.csv', index=False)


# Request stats for all teams

# Set the timeout duration for the API request
timeout_duration = 60

team_id=team_ids[0]

teams_stats=pd.DataFrame()

for team_id in team_ids:
    try:
        team_stats1=teamyearbyyearstats.TeamYearByYearStats(team_id,timeout=timeout_duration)
        team_stats2=teaminfocommon.TeamInfoCommon(team_id,timeout=timeout_duration)

        # Retrieve data from the API
        team_stats1=team_stats1.get_data_frames()[0].tail(1)
        team_stats1=team_stats1.drop(['TEAM_CITY','TEAM_NAME','TEAM_ID','YEAR','NBA_FINALS_APPEARANCE'],axis=1)
        
        team_stats2_1=team_stats2.get_data_frames()[0]
        team_stats2_1=team_stats2_1.drop(['TEAM_CITY','TEAM_NAME','TEAM_CONFERENCE','TEAM_DIVISION','TEAM_CODE','TEAM_SLUG'],axis=1)

        team_stats2_2=team_stats2.get_data_frames()[1]
        team_stats2_2=team_stats2_2.drop(['TEAM_ID','LEAGUE_ID','SEASON_ID'],axis=1)
        
        team_stats= pd.concat([team_stats2_1.reset_index(drop=True),team_stats2_2.reset_index(drop=True),team_stats1.reset_index(drop=True)],axis=1)
         
        teams_stats=pd.concat([teams_stats,team_stats],axis=0)
        
    except requests.Timeout:
        print(f"Request for player {team_id} timed out.")
        

teams_stats=teams_stats.drop(['NBA_FINALS_APPEARANCE'],axis=1)
teams_stats=teams_stats.drop(['CONF_COUNT','DIV_COUNT'],axis=1)
teams_stats=teams_stats.drop(['SEASON_YEAR','GP'],axis=1)
teams_stats=teams_stats.drop(['MAX_YEAR'],axis=1)

teams_stats.to_csv('raw_teams_stats.csv', index=False)





