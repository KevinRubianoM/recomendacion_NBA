import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error


#EVALUACIÓN DEL MODELO

#BASADO EN EL CONTENIDO CENTRADO EN EL USUARIO CENTRADA EN EL USUARIO

#CALCULAR SCORES PARA TODOS LOS EQUIPOS SUPONIENDO QUE TODOS LOS VALORES SON FALTANTES PARA CADA JUGADOR

#Sacar indice de jugadores en item feature
jugadores=raw_players22_23.iloc[:,1:3]

#Se rellenan los valores faltantes usando una ponderación basada
#en la similitud de los jugadores

#Se toma la matriz original sin la imputación anterior

intMat22_23 = pd.pivot_table(scores22_23, values='score', index='Opponent', columns='Player')


#Quitar valores infinitos

intMat22_23[np.isneginf(intMat22_23)] = np.min(np.min(intMat22_23[np.isfinite(intMat22_23)]))
intMat22_23[np.isposinf(intMat22_23)] = np.max(np.max(intMat22_23[np.isfinite(intMat22_23)]))

Predict_Mat=pd.DataFrame(0, index=intMat22_23.index, columns=intMat22_23.columns)

for player in jugadores['PLAYER_NAME']:
    
    player_scores=intMat22_23.iloc[:,jugadores.iloc[:,1].to_list().index(player)]
    i=0
    for score in player_scores:
            similarities=items_similarity[jugadores.iloc[:,1].to_list().index(player),:]
            mejores=sorted(enumerate(similarities), key=lambda x: x[1],reverse=True)[1:6]
            scores_mejores=intMat22_23.iloc[:,[mejores[0][0],mejores[1][0],mejores[2][0],mejores[3][0],mejores[4][0]]]
            scores_mejores=scores_mejores.fillna(0)
            
            Predict_Mat.iloc[i,jugadores.iloc[:,1].to_list().index(player)]= ((mejores[0][1]*scores_mejores.iloc[i,0])+(mejores[1][1]*scores_mejores.iloc[i,1])+(mejores[2][1]*scores_mejores.iloc[i,2])+(mejores[3][1]*scores_mejores.iloc[i,3])+(mejores[4][1]*scores_mejores.iloc[i,4]))/(mejores[0][1]+mejores[1][1]+mejores[2][1]+mejores[3][1]+mejores[4][1])
            i+=1

intMat22_23=preprocessing.scale(intMat22_23)
Predict_Mat=preprocessing.scale(Predict_Mat)

MSE = mean_squared_error(intMat22_23, Predict_Mat)

#Realizar recomendación

BOS_players= raw_players.query("TEAM_ABBREVIATION=='BOS'")

ATL_scores= Predict_Mat.iloc[0,:].reset_index()
ATL_counters_BOS_pred = ATL_scores[ATL_scores['Player'].isin(BOS_players['PLAYER_NAME'])]

BKN_scores= Predict_Mat.iloc[1,:].reset_index()
BKN_counters_BOS_pred = BKN_scores[BKN_scores['Player'].isin(BOS_players['PLAYER_NAME'])]

CHA_scores= Predict_Mat.iloc[2,:].reset_index()
CHA_counters_BOS_pred = CHA_scores[CHA_scores['Player'].isin(BOS_players['PLAYER_NAME'])]

CHI_scores= Predict_Mat.iloc[3,:].reset_index()
CHI_counters_BOS_pred = CHI_scores[CHI_scores['Player'].isin(BOS_players['PLAYER_NAME'])]

CLE_scores= Predict_Mat.iloc[4,:].reset_index()
CLE_counters_BOS_pred = CLE_scores[CLE_scores['Player'].isin(BOS_players['PLAYER_NAME'])]

DAL_scores= Predict_Mat.iloc[5,:].reset_index()
DAL_counters_BOS_pred = DAL_scores[DAL_scores['Player'].isin(BOS_players['PLAYER_NAME'])]

DAL_scores= Predict_Mat.iloc[5,:].reset_index()
DAL_counters_BOS_pred = DAL_scores[DAL_scores['Player'].isin(BOS_players['PLAYER_NAME'])]

MIA_scores= Predict_Mat.iloc[15,:].reset_index()
MIA_counters_BOS_pred = MIA_scores[MIA_scores['Player'].isin(BOS_players['PLAYER_NAME'])]




