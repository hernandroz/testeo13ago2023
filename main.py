from fastapi import FastAPI
import pandas as pd
import pyarrow

app = FastAPI()


df_general = pd.read_parquet('asdf.parquet')
df_business = pd.read_parquet('business_google_yelp.parquet')


def get_business_user(user_id):
    # Se ingresa un 'User_ID' y retorna un DataFrame con los negocios que visitó que tengan mayor o igual a 4 estrellas

    s = df_general[df_general['User_ID']==user_id]
    e = s[s['Stars']>=4]

    return set(e['ID_Business'])

def get_top_business_state(state):
    top = df_general[df_general['State'] == state]
    top = top.groupby('ID_Business', as_index = False)['Stars'].mean()
    top = set(top[top['Stars']==5]['ID_Business'])
    
    return top 

def get_states(User_ID):
    return list(df_general[df_general['User_ID'] == User_ID]['State'].unique())




@app.get("/recomendacion/{user_id}")
def recomendacion(user_id):
    states = get_states(user_id)
    recomendacion_stateS = []
    for state in states:
        top_business = get_top_business_state(state)
        business_user = get_business_user(user_id)
        recomendacion_state = list(top_business.difference(business_user))[0:5]
        recomendacion_stateS.append(recomendacion_state)
    
    recomendacion_texto = []

    for cantidad in range(len(states)):
        recomendado = df_business[df_business['ID_Business'] == recomendacion_stateS[cantidad]]['Name'].to_list()[0]
        recomendacion_texto_base = "Para el estado de " + states[cantidad] + " te recomendamos los siguientes lugares: " + ", ".join(recomendado)
        recomendacion_texto.append(recomendacion_texto_base)
        
    return {"Recomendación": ". ".join(recomendacion_texto)}
