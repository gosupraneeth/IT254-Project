from users.models import Movies , Languages ,Genres, User,PriorityGenre,PriorityLanguage
import csv
import numpy as np
import pandas as pd
#def save_movies(data):
#    data_list = data.values.tolist()
#    details = list()
#    for movie in data_list:
#        Movie = Movies(mid=movie[1],title=movie[3],year=movie[4],duration=movie[6],director=movie[9],writer=movie[10],production=movie[11],actors=movie[12],description=movie[13],rating=movie[14])
#        Movie.save()

def save_movies(data):
    count =0
    for movie in data:
        print(movie)
        try:
            Movie = Movies(mid=movie[1],title=movie[3],year=movie[4],duration=movie[6],director=movie[9],writer=movie[10],production=movie[11],actors=movie[12],description=movie[13],rating=movie[14])
            Movie.save()
            count+=1
        except:
            pass
    
    print(count)

def save_genres(data):
    for movie in data:
        Movie = Movies.objects.get(mid=movie[1])
        for ge in movie[5].split(', '):
            if ge in ['Comedy','Family','War','Adventure','Music','Musical','Mystery','Thriller','Drama','Romance','Action','Crime','Horror','Film-Noir','Fantasy','Sci-Fi','History']:
                Genre = Genres.objects.get(g_name=ge)
                Genre.movies.add(Movie)


def save_languages(data):
    for movie in data:
        Movie = Movies.objects.get(mid=movie[1])
        for lan in movie[8].split(', '):
            if lan in ['Hindi','Marathi','English','French','German','Spanish','Russian','Italian','Japanese','Chinese']:
                Language = Languages.objects.get(l_name=lan)
                Language.movies.add(Movie)

def add_genres():
    for ge in ['Comedy','Family','War','Adventure','Music','Musical','Mystery','Thriller','Drama','Romance','Action','Crime','Horror','Film-Noir','Fantasy','Sci-Fi','History']:
        genre = Genres(g_name=ge)
        genre.save()

def add_languages():
    for lan in ['Hindi','Marathi','English','French','German','Spanish','Russian','Italian','Japanese','Chinese']:
        language = Languages(l_name=lan)
        language.save()

def add_prio_genres():
    for ge in ["action", "adventure", "darkmovies", "drama", "fantasy", "musical", "romance", "scifi", "thriller", "comedy", "history"]:
        genre = PriorityGenre(pgname=ge,pgval=0)
        genre.save()

def add_prio_languages():
    for lan in ["hindi", "marathi", "english", "french", "german", "spanish", "russian", "italian", "japanese", "chinese"]:
        language = PriorityLanguage(plname=lan,plval=0)
        language.save()

def run():
    #file_ = open('users/FinalMovies.csv')
    #data = csv.reader(file_)
    #next(data)
    data = pd.read_csv('users/FinalMovies.csv')
    data = data.values.tolist()

    Movies.objects.all().delete()
    Languages.objects.all().delete()
    Genres.objects.all().delete()
    PriorityGenre.objects.all().delete()
    PriorityLanguage.objects.all().delete()

    add_genres()
    add_languages()
    add_prio_genres()
    add_prio_languages()
    save_movies(data)
    save_genres(data)
    save_languages(data)
