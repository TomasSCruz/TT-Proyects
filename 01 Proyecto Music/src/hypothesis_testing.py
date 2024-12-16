import pandas as pd
from tabulate import tabulate

### Hipótesis 1: comparar el comportamiento del usuario en las dos ciudades 
### De acuerdo con la primera hipótesis, los usuarios de Springfield y Shelbyville escuchan  
### música de forma distinta. Comprueba esto utilizando los datos de tres días de la semana: 
### lunes, miércoles y viernes.

# <creando la función number_tracks()>
# declararemos la función con dos parámetros: day=, city=
def number_tracks(df: pandas.core.frame.DataFrame,day: str,city: str) -> int:
    track_list = df[df['day'] == day]
    track_list = track_list[track_list['city'] == city]
    track_list_count = track_list['user_id'].count()
    return track_list_count

# Creamos una función para comparar la actividad de cada ciudad en los Lunes, Miercoles y Viernes
def hip_1(df: pandas.core.frame.DataFrame) -> None:
    # Primero obtenemos los day_counts para Springfield
    mon_spr = number_tracks('Monday','Springfield')
    wed_spr = number_tracks('Wednesday','Springfield')
    fri_spr = number_tracks('Friday','Springfield')

    # Y despues para Shelbyville
    mon_she = number_tracks('Monday','Shelbyville')
    wed_she = number_tracks('Wednesday','Shelbyville')
    fri_she = number_tracks('Friday','Shelbyville')

    # Finalmente creamos una tabla para comparar lado a lado los números
    cities_days = ['city','monday','wednesday','friday']
    day_num = [
        ['Springfield', mon_spr, wed_spr, fri_spr],
        ['Shelbyville', mon_she, wed_she, fri_she]
            ]
    day_city_comparison = pd.DataFrame(columns=cities_days, data=day_num)

    # Finalmente mostramos la tabla
    print('Comparación de comportamiento entre Springfield y Shelbyville','\n',tabulate(day_city_comparison, headers=head, tablefmt="grid"))

    return

### Hipótesis 2: música al principio y al final de la semana
### De acuerdo con la segunda hipótesis, los lunes por la mañana y los viernes por la noche 
### los ciudadanos de Springfield escuchan géneros que difieren de aquellos que los usuarios
### de Shelbyville disfrutan.

# Primero creamos una función para devolver los 15 géneros más populares en un periodo dentro de un día
def genre_weekday(df,day,time1,time2) -> pandas.core.series.Series:
    genre_df = df[df['day'] == day]
    genre_df = genre_df[genre_df['time'] >= time1]
    genre_df = genre_df[genre_df['time'] <= time2]
    genre_df_count = genre_df.groupby('genre')['genre'].count()
    genre_df_sorted = genre_df_count.sort_values(ascending = False)
    return genre_df_sorted[:15]

def hip_2(df: pandas.core.frame.DataFrame) -> None:

    # Obtenemos los DataFrames separados por ciudad
    spr_general = df[df['city'] == 'Springfield']
    she_general = df[df['city'] == 'Shelbyville']

    # Ahora recopilaamos los datos del lunes
    spr_monday = genre_weekday(spr_general,'Monday','08:00:00','12:00:00').rename('Springfield')
    she_monday = genre_weekday(she_general,'Monday','08:00:00','12:00:00').rename('Shelbyville')

    # Y los datos del viernes
    spr_friday = genre_weekday(spr_general,'Friday','17:00:00','21:00:00').rename('Springfield')
    she_friday = genre_weekday(she_general,'Friday','08:00:00','12:00:00').rename('Shelbyville')

    # Ahora si mostramos lado a lado los datos de los respectivos días
    print('Lunes \n', pd.merge(spr_monday, she_monday, right_index = True,
               left_index = True))

    print('Viernes \n', pd.merge(spr_friday, she_friday, right_index = True,
               left_index = True))
    
    return

### Hipótesis 3: preferencias de género en Springfield y Shelbyville
### Hipótesis: Shelbyville ama la música rap. A los ciudadanos de Springfield les gusta más el pop.

def hip_3(df: pandas.core.frame.DataFrame) -> None:

    # Obtenemos los DataFrames separados por ciudad
    spr_general = df[df['city'] == 'Springfield']
    she_general = df[df['city'] == 'Shelbyville']

    # Agrupamos para obtener el nro de canciones por género, lo ordenamos en descendente y obtenemos el top 10
    spr_top = spr_general.groupby('genre')['genre'].count().sort_values(ascending = False).head(10).rename('Springfield')
    she_top = she_general.groupby('genre')['genre'].count().sort_values(ascending = False).head(10).rename('Shelbyville')

    print('Top 10', pd.merge(spr_top, she_top, right_index = True,
               left_index = True))
    
    return
