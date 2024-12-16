import pandas as pd

def load_data(file_path) -> pandas.core.frame.DataFrame:
    # Primero leemos el CSV
    return pd.read_csv(file_path)

# Funcion para corregir valores
def replace_wrong_values(wrong_values, correct_value) -> None: 
    for wrong_value in wrong_values: 
        df['genre'] = df['genre'].replace(wrong_value, correct_value)
    return

# Funcion para englobar subgeneros
def englobe(genres, genre: str) -> list[str]: # genres: lista completa a filtrar / genre: genero que se desea filtrar
    genres = list(genres)
    subgens = []
    for gen in genres:
        #bucle para revisar subgeneros basados en la inclusion de la palabra
        if genre in gen:
            subgens.append(gen)
    return subgens

def clean_data(df) -> pandas.core.frame.DataFrame:
    # Renombramos las columnas para estandarizar todo
    df = df.rename(columns = {'  userID':'user_id','Track':'track','  City  ':'city','Day':'day'})
    
    # Ahora reemplazamos los nulos dentro de las columans por el string "unknown"
    columns_to_replace = ['track','artist','genre']
    for column in columns_to_replace:
        df[column] = df[column].fillna('unknown')

    # Eliminamos duplicados explícitos reiniciando el índice
    df = df.drop_duplicates().reset_index(drop=True)

    # Primero creamos los géneros principales
    metal = englobe(all_genres, 'metal')
    rock = englobe(all_genres, 'rock')
    pop = englobe(all_genres, 'pop')
    folk = englobe(all_genres, 'folk')
    hiphop = englobe(all_genres, 'hop')
    latin = englobe(all_genres, 'latin')
    
    # Correciones particulares por la forma de funcionamiento de englobe: 
    hiphop.pop() 
    hiphop.append('hip') 

    # Eliminamos los duplicados implícitos
    replace_wrong_values(metal,'metal')
    replace_wrong_values(rock,'rock')
    replace_wrong_values(pop,'pop')
    replace_wrong_values(folk,'folk')
    replace_wrong_values(hiphop,'hiphop')
    replace_wrong_values(latin,'latin')
    
    return df
