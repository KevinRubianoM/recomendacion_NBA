import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn import preprocessing

#ADVERTENCIA: BASADO EN OBJETOS CREADOS EN LOS OTROS SCRIPTS 

#IMPLEMENTACIÓN DEL MODELO

#BASADO EN EL CONTENIDO CENTRADO EN EL USUARIO CENTRADA EN EL USUARIO

#QUITAR VALORES INFINITOS

intMat22_23[np.isneginf(intMat22_23)] = np.min(np.min(intMat22_23[np.isfinite(intMat22_23)]))
intMat22_23[np.isposinf(intMat22_23)] = np.max(np.max(intMat22_23[np.isfinite(intMat22_23)]))


#ESTABLECER SIMILITUD ENTRE LOS JUGADORES CON SUS CARACTERÍSTICAS PARA REALIZAR UNA IMPUTACIÓN

raw_players22_23= raw_players[raw_players['PLAYER_ID'].isin(raw22_23['Player_ID'])].reset_index()

item_features= raw_players22_23.drop(columns=['PLAYER_ID','PLAYER_NAME','TEAM_ID','TEAM_ABBREVIATION','PLAYER_HEIGHT','COLLEGE','COUNTRY','DRAFT_YEAR','DRAFT_ROUND','DRAFT_NUMBER'])

#Ver variables con menos coeficiente de variación

CVs=np.sqrt(item_features.var())/item_features.mean()

item_features= item_features.drop(columns=['PLAYER_WEIGHT'])

items_similarity=cosine_similarity(item_features)


#RELLENAR VALORES FALTANTES

#Sacar indice de jugadores en item feature
jugadores=raw_players22_23.iloc[:,1:3]
player=jugadores['PLAYER_NAME'][0]

#Se rellenan los valores faltantes usando una ponderación basada
#en la silitud de los jugadores

for player in jugadores['PLAYER_NAME']:
    
    player_scores=intMat22_23.iloc[:,jugadores.iloc[:,1].to_list().index(player)]
    i=0
    for score in player_scores:
        if np.isnan(score):
            similarities=items_similarity[jugadores.iloc[:,1].to_list().index(player),:]
            mejores=sorted(enumerate(similarities), key=lambda x: x[1],reverse=True)[1:6]
            scores_mejores=intMat22_23.iloc[:,[mejores[0][0],mejores[1][0],mejores[2][0],mejores[3][0],mejores[4][0]]]
            scores_mejores=scores_mejores.fillna(0)
            
            intMat22_23.iloc[i,jugadores.iloc[:,1].to_list().index(player)]= ((mejores[0][1]*scores_mejores.iloc[i,0])+(mejores[1][1]*scores_mejores.iloc[i,1])+(mejores[2][1]*scores_mejores.iloc[i,2])+(mejores[3][1]*scores_mejores.iloc[i,3])+(mejores[4][1]*scores_mejores.iloc[i,4]))/(mejores[0][1]+mejores[1][1]+mejores[2][1]+mejores[3][1]+mejores[4][1])
        i+=1

#Vamos a realizar una recomendación de jugadores de los BOS para un partido contra ATL

BOS_players= raw_players.query("TEAM_ABBREVIATION=='BOS'")

ATL_scores= intMat22_23.iloc[0,:].reset_index()
ATL_counters_BOS = ATL_scores[ATL_scores['Player'].isin(BOS_players['PLAYER_NAME'])]

BKN_scores= intMat22_23.iloc[1,:].reset_index()
BKN_counters_BOS = BKN_scores[BKN_scores['Player'].isin(BOS_players['PLAYER_NAME'])]

CHA_scores= intMat22_23.iloc[2,:].reset_index()
CHA_counters_BOS = CHA_scores[CHA_scores['Player'].isin(BOS_players['PLAYER_NAME'])]

CHI_scores= intMat22_23.iloc[3,:].reset_index()
CHI_counters_BOS = CHI_scores[CHI_scores['Player'].isin(BOS_players['PLAYER_NAME'])]

CLE_scores= intMat22_23.iloc[4,:].reset_index()
CLE_counters_BOS = CLE_scores[CLE_scores['Player'].isin(BOS_players['PLAYER_NAME'])]

DAL_scores= intMat22_23.iloc[5,:].reset_index()
DAL_counters_BOS = DAL_scores[DAL_scores['Player'].isin(BOS_players['PLAYER_NAME'])]

DAL_scores= intMat22_23.iloc[5,:].reset_index()
DAL_counters_BOS = DAL_scores[DAL_scores['Player'].isin(BOS_players['PLAYER_NAME'])]

MIA_scores= intMat22_23.iloc[15,:].reset_index()
MIA_counters_BOS = MIA_scores[MIA_scores['Player'].isin(BOS_players['PLAYER_NAME'])]



#BASADO EN EL CONTENIDO CENTRADO EN EL USUARIO CENTRADA EN EL USUARIO

#QUITAR VALORES INFINITOS

intMat22_23[np.isneginf(intMat22_23)] = np.min(np.min(intMat22_23[np.isfinite(intMat22_23)]))
intMat22_23[np.isposinf(intMat22_23)] = np.max(np.max(intMat22_23[np.isfinite(intMat22_23)]))


#ESTABLECER SIMILITUD ENTRE LOS JUGADORES CON SUS CARACTERÍSTICAS PARA REALIZAR UNA IMPUTACIÓN

raw_players22_23= raw_players[raw_players['PLAYER_ID'].isin(raw22_23['Player_ID'])].reset_index()

item_features= raw_players22_23.drop(columns=['PLAYER_ID','PLAYER_NAME','TEAM_ID','TEAM_ABBREVIATION','PLAYER_HEIGHT','COLLEGE','COUNTRY','DRAFT_YEAR','DRAFT_ROUND','DRAFT_NUMBER'])

#Ver variables con menos coeficiente de variación

CVs=np.sqrt(item_features.var())/item_features.mean()

item_features= item_features.drop(columns=['PLAYER_WEIGHT'])

items_similarity=cosine_similarity(item_features)


#RELLENAR VALORES FALTANTES

#Sacar indice de jugadores en item feature
jugadores=raw_players22_23.iloc[:,1:3]
player=jugadores['PLAYER_NAME'][0]

#Se rellenan los valores faltantes usando una ponderación basada
#en la silitud de los jugadores

for player in jugadores['PLAYER_NAME']:
    
    player_scores=intMat22_23.iloc[:,jugadores.iloc[:,1].to_list().index(player)]
    i=0
    for score in player_scores:
        if np.isnan(score):
            similarities=items_similarity[jugadores.iloc[:,1].to_list().index(player),:]
            mejores=sorted(enumerate(similarities), key=lambda x: x[1],reverse=True)[1:6]
            scores_mejores=intMat22_23.iloc[:,[mejores[0][0],mejores[1][0],mejores[2][0],mejores[3][0],mejores[4][0]]]
            scores_mejores=scores_mejores.fillna(0)
            
            intMat22_23.iloc[i,jugadores.iloc[:,1].to_list().index(player)]= ((mejores[0][1]*scores_mejores.iloc[i,0])+(mejores[1][1]*scores_mejores.iloc[i,1])+(mejores[2][1]*scores_mejores.iloc[i,2])+(mejores[3][1]*scores_mejores.iloc[i,3])+(mejores[4][1]*scores_mejores.iloc[i,4]))/(mejores[0][1]+mejores[1][1]+mejores[2][1]+mejores[3][1]+mejores[4][1])
        i+=1
        
        

#CON LA OTRA MATRIZ DE INTERACCIONES 

#RELLENAR VALORES FALTANTES

#Sacar indice de jugadores en item feature
jugadores=raw_players22_23.iloc[:,1:3]

for player in jugadores['PLAYER_NAME']:
    
    player_scores=intMat_0_22_23.iloc[:,jugadores.iloc[:,1].to_list().index(player)]
    i=0
    for score in player_scores:
        if np.isnan(score):
            similarities=items_similarity[jugadores.iloc[:,1].to_list().index(player),:]
            mejores=sorted(enumerate(similarities), key=lambda x: x[1],reverse=True)[1:6]
            scores_mejores=intMat_0_22_23.iloc[:,[mejores[0][0],mejores[1][0],mejores[2][0],mejores[3][0],mejores[4][0]]]
            scores_mejores=scores_mejores.fillna(0)
            
            intMat_0_22_23.iloc[i,jugadores.iloc[:,1].to_list().index(player)]= ((mejores[0][1]*scores_mejores.iloc[i,0])+(mejores[1][1]*scores_mejores.iloc[i,1])+(mejores[2][1]*scores_mejores.iloc[i,2])+(mejores[3][1]*scores_mejores.iloc[i,3])+(mejores[4][1]*scores_mejores.iloc[i,4]))/(mejores[0][1]+mejores[1][1]+mejores[2][1]+mejores[3][1]+mejores[4][1])
        i+=1

#Vamos a realizar una recomendación de jugadores de los BOS para un partido contra ATL

BOS_players= raw_players.query("TEAM_ABBREVIATION=='BOS'")

ATL_scores= intMat_0_22_23.iloc[0,:].reset_index()
ATL_counters_BOS_0_ = ATL_scores[ATL_scores['Player'].isin(BOS_players['PLAYER_NAME'])]

BKN_scores= intMat_0_22_23.iloc[1,:].reset_index()
BKN_counters_BOS_0_  = BKN_scores[BKN_scores['Player'].isin(BOS_players['PLAYER_NAME'])]

CHA_scores= intMat_0_22_23.iloc[2,:].reset_index()
CHA_counters_BOS_0_  = CHA_scores[CHA_scores['Player'].isin(BOS_players['PLAYER_NAME'])]

CHI_scores= intMat_0_22_23.iloc[3,:].reset_index()
CHI_counters_BOS_0_  = CHI_scores[CHI_scores['Player'].isin(BOS_players['PLAYER_NAME'])]

CLE_scores= intMat_0_22_23.iloc[4,:].reset_index()
CLE_counters_BOS_0_  = CLE_scores[CLE_scores['Player'].isin(BOS_players['PLAYER_NAME'])]

DAL_scores= intMat_0_22_23.iloc[5,:].reset_index()
DAL_counters_BOS_0_  = DAL_scores[DAL_scores['Player'].isin(BOS_players['PLAYER_NAME'])]

DAL_scores= intMat_0_22_23.iloc[5,:].reset_index()
DAL_counters_BOS_0_  = DAL_scores[DAL_scores['Player'].isin(BOS_players['PLAYER_NAME'])]

MIA_scores= intMat_0_22_23.iloc[15,:].reset_index()
MIA_counters_BOS_0_  = MIA_scores[MIA_scores['Player'].isin(BOS_players['PLAYER_NAME'])]



# FILTRADO COLABORATIVO ITEM-ITEM

#SIMILITUD SOLO BASADA EN LAS INTERACCONES

intMat22_23_00_[np.isneginf(intMat22_23_00_)] = np.min(np.min(intMat22_23_00_[np.isfinite(intMat22_23_00_)]))
intMat22_23_00_[np.isposinf(intMat22_23_00_)] = np.max(np.max(intMat22_23_00_[np.isfinite(intMat22_23_00_)]))

intMat22_23_00_nan[np.isneginf(intMat22_23_00_nan)] = np.min(np.min(intMat22_23_00_nan[np.isfinite(intMat22_23_00_nan)]))
intMat22_23_00_nan[np.isposinf(intMat22_23_00_nan)] = np.max(np.max(intMat22_23_00_nan[np.isfinite(intMat22_23_00_nan)]))


intMat22_23_00_[np.isnan(intMat22_23_00_)] = 0

item_similarity_INT=cosine_similarity(intMat22_23_00_.T)

#Sacar indice de jugadores en item feature
jugadores=raw_players22_23.iloc[:,1:3]

for player in jugadores['PLAYER_NAME']:
    
    player_scores=intMat22_23_00_nan.iloc[:,jugadores.iloc[:,1].to_list().index(player)]
    i=0
    for score in player_scores:
        if np.isnan(score):
            similarities=item_similarity_INT[jugadores.iloc[:,1].to_list().index(player),:]
            mejores=sorted(enumerate(similarities), key=lambda x: x[1],reverse=True)[1:6]
            scores_mejores=intMat22_23_00_nan.iloc[:,[mejores[0][0],mejores[1][0],mejores[2][0],mejores[3][0],mejores[4][0]]]
            scores_mejores=scores_mejores.fillna(0)
            
            intMat22_23_00_nan.iloc[i,jugadores.iloc[:,1].to_list().index(player)]= ((mejores[0][1]*scores_mejores.iloc[i,0])+(mejores[1][1]*scores_mejores.iloc[i,1])+(mejores[2][1]*scores_mejores.iloc[i,2])+(mejores[3][1]*scores_mejores.iloc[i,3])+(mejores[4][1]*scores_mejores.iloc[i,4]))/(mejores[0][1]+mejores[1][1]+mejores[2][1]+mejores[3][1]+mejores[4][1])
        i+=1

#Vamos a realizar una recomendación de jugadores de los BOS para un partido contra ATL

BOS_players= raw_players.query("TEAM_ABBREVIATION=='BOS'")

ATL_scores= intMat22_23_00_nan.iloc[0,:].reset_index()
ATL_counters_BOS_1_ = ATL_scores[ATL_scores['Player'].isin(BOS_players['PLAYER_NAME'])]

BKN_scores= intMat22_23_00_nan.iloc[1,:].reset_index()
BKN_counters_BOS_1_ = BKN_scores[BKN_scores['Player'].isin(BOS_players['PLAYER_NAME'])]

CHA_scores= intMat22_23_00_nan.iloc[2,:].reset_index()
CHA_counters_BOS_1_ = CHA_scores[CHA_scores['Player'].isin(BOS_players['PLAYER_NAME'])]

CHI_scores= intMat22_23_00_nan.iloc[3,:].reset_index()
CHI_counters_BOS_1_ = CHI_scores[CHI_scores['Player'].isin(BOS_players['PLAYER_NAME'])]

CLE_scores= intMat22_23_00_nan.iloc[4,:].reset_index()
CLE_counters_BOS_1_ = CLE_scores[CLE_scores['Player'].isin(BOS_players['PLAYER_NAME'])]

DAL_scores= intMat22_23_00_nan.iloc[5,:].reset_index()
DAL_counters_BOS_1_ = DAL_scores[DAL_scores['Player'].isin(BOS_players['PLAYER_NAME'])]

DAL_scores= intMat22_23_00_nan.iloc[5,:].reset_index()
DAL_counters_BOS_1_ = DAL_scores[DAL_scores['Player'].isin(BOS_players['PLAYER_NAME'])]

MIA_scores= intMat22_23_00_nan.iloc[15,:].reset_index()
MIA_counters_BOS_1_ = MIA_scores[MIA_scores['Player'].isin(BOS_players['PLAYER_NAME'])]


#MODELO 2.0

#PERFIL DE USUARIO 

perfil_LAL= intMat22_23.iloc[13,:].reset_index()

####

X=intMat22_23.values
Y=item_features.values

pesos=X@Y
pesos=Y.T@X.T

pesosnorm=preprocessing.scale(pesos, axis=0)














