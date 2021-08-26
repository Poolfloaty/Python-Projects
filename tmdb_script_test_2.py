import psycopg2
import json, sys
import requests
import os
from psycopg2.extras import Json
from psycopg2.extensions import adapt

session = requests.Session()
  
tmdb_api_key = os.environ.get('TMDB_API_KEY')
response = session.get('https://api.themoviedb.org/3/movie/popular?api_key=' + tmdb_api_key)   
response.raise_for_status()

json_data = response.json()
movies_list = json_data['results']

genre_response = session.get('https://api.themoviedb.org/3/genre/movie/list?api_key=' + tmdb_api_key)   
genre_response.raise_for_status()

genre_json_data = genre_response.json()
genre_list = genre_json_data['genres']

#get the clomun names
columns = list()
for movie in movies_list:
    for key in movie:
        columns.append(key)
columns = list(dict.fromkeys(columns))

# get the column values
values = list()
for index in range(len(movies_list)):
    for value in movies_list[index]:
        values.append(str(movies_list[index][value]))
        
genre_columns = list()
for genre_id in genre_list:
    for key in genre_id:
        genre_columns.append(key)
genre_columns = list(dict.fromkeys(genre_columns))
        
genre_values = list()
for index in range(len(genre_list)):
    for value in genre_list[index]:
        genre_values.append(str(genre_list[index][value]))
        
try:
    dbconn = psycopg2.connect(
        dbname = "tmdb",
        user = "tmdbuser",
        host = "34.207.155.134",
        password = os.environ.get("TMDB_PASSWORD"),
        # attempt to connect for 3 seconds then raise exception
        connect_timeout = 3,
    )
    
    cur = dbconn.cursor()
    print ("\ncreated cursor object:", cur)

except psycopg2.Error as err:
    print ("\npsycopg2 connect error:", err)
    dbconn = None
    cur = None

if cur != None:
        
    try:
        for column, value in zip(columns, values):
        #cur.execute("SET CLIENT_ENCODING TO 'iso-8859-1';")
            #print("INSERT INTO popular_movies (%s)\nVALUES (%s);" % (
            #column,
            #value
            #))
            cur.execute("INSERT INTO popular_movies (%s)\nVALUES (%s);" % (
            column,
            value
            ))
        for genre_column, genre_value in zip(genre_columns, genre_values):
            #print("INSERT INTO movie_genres (%s)\nVALUES (%s);" % (
            #genre_column,
            #genre_value
            #))
            cur.execute("INSERT INTO movie_genre (%s)\nVALUES (%s);" % (
            genre_column,
            genre_value
            ))
        dbconn.commit()
        print ('finished INSERT INTO execution')

    except (Exception, psycopg2.Error) as error:
        print("\nexecute_sql() error:", error)
        dbconn.rollback()