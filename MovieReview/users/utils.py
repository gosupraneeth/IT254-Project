import random as rd
from users.models import Movies , Languages ,Genres

GENRE = ["Action","Adventure","Crime","Drama","Fantasy","Musical","Romance","Thriller","Comedy","History"]

def make_card_dict(card,obj):
    lang = ''
    for l_obj in obj.language.all():
        lang +=f'{l_obj.l_name},'
    lang = lang[:-1]
    card['language'] = lang
    ge = ''
    for g_obj in obj.genre.all():
        ge +=f'{g_obj.g_name},'
    ge = ge[:-1]
    card['genre'] = ge
    card['mid'] = obj.mid
    card['title'] = obj.title
    card['year'] = obj.year
    card['duration'] = obj.duration
    card['director'] = obj.director
    card['writer'] = obj.writer
    card['production']= obj.production
    card['actors'] = obj.actors
    card['description'] = obj.description
    card['rating'] = obj.rating

def sort_cards(cards,s_cards):
    for s in sorted(cards, key=lambda y: y['rating'],reverse=True):
        s_cards.append(s)


def movies_data_load(start,end):
    return s_cards[start:end]

def movies_data_load_mood(mood,lang):
    mood_cards = list()  
    mood_s_cards = list()
    if(mood=="sad"):
        for obj in Genres.objects.get(g_name='Comedy').movies.all() & Languages.objects.get(l_name=lang).movies.all():
            mood_card = dict()
            make_card_dict(mood_card,obj)
            mood_cards.append(mood_card)
    if mood=='frustrated':
        for obj in Genres.objects.get(g_name='Musical').movies.all() & Languages.objects.get(l_name=lang).movies.all():
            mood_card = dict()
            make_card_dict(mood_card,obj)
            mood_cards.append(mood_card)
    if mood=='angry':
        for obj in Genres.objects.get(g_name='Drama').movies.all() & Languages.objects.get(l_name=lang).movies.all():
            mood_card = dict()
            make_card_dict(mood_card,obj)
            mood_cards.append(mood_card)
    if mood == 'scared':
        for obj in Genres.objects.get(g_name='Adventure').movies.all() & Languages.objects.get(l_name=lang).movies.all():
            mood_card = dict()
            make_card_dict(mood_card,obj)
            mood_cards.append(mood_card)
        for obj in Genres.objects.get(g_name='Fantasy').movies.all() & Languages.objects.get(l_name=lang).movies.all():
            mood_card = dict()
            make_card_dict(mood_card,obj)
            mood_cards.append(mood_card)
    if mood == 'happy':
        for ge in GENRE:
            if ge !='Comedy':
                for obj in Genres.objects.get(g_name=ge).movies.all() & Languages.objects.get(l_name=lang).movies.all():
                    mood_card = dict()
                    make_card_dict(mood_card,obj)
                    mood_cards.append(mood_card)
    
    mood_cards = [dict(t) for t in {tuple(d.items()) for d in mood_cards}]
    sort_cards(mood_cards,mood_s_cards)
    return mood_s_cards[:7]


def movies_data_load_genre(genre,lang,num):
    genre_cards = list()  
    genre_s_cards = list()
    if(genre=='sci-fi' or genre == 'Sci-Fi'):
        genre='SciFi'
    if(genre=='film-noir'):
        genre='Film-Noir'
    genre = genre.capitalize()
    if(genre=='Comedy'):
        for obj in Genres.objects.get(g_name='Family').movies.all() & Languages.objects.get(l_name=lang).movies.all():
            genre_card = dict()
            make_card_dict(genre_card,obj)
            genre_cards.append(genre_card)
    
    if genre=='Adventure':
        for obj in Genres.objects.get(g_name='War').movies.all() & Languages.objects.get(l_name=lang).movies.all():
            genre_card = dict()
            make_card_dict(genre_card,obj)
            genre_cards.append(genre_card)
    if genre == 'Musical':
        for obj in Genres.objects.get(g_name='Music').movies.all() & Languages.objects.get(l_name=lang).movies.all():
            genre_card = dict()
            make_card_dict(genre_card,obj)
            genre_cards.append(genre_card)
    if genre == 'Thriller':
        for obj in Genres.objects.get(g_name='Mystery').movies.all() & Languages.objects.get(l_name=lang).movies.all():
            genre_card = dict()
            make_card_dict(genre_card,obj)
            genre_cards.append(genre_card)
    if genre == 'Darkmovies':
        for obj in Genres.objects.get(g_name='Crime').movies.all() & Languages.objects.get(l_name=lang).movies.all():
            genre_card = dict()
            make_card_dict(genre_card,obj)
            genre_cards.append(genre_card)
        for obj in Genres.objects.get(g_name='Horror').movies.all() & Languages.objects.get(l_name=lang).movies.all():
            genre_card = dict()
            make_card_dict(genre_card,obj)
            genre_cards.append(genre_card)
        genre = 'FilmNoir'
    for obj in Genres.objects.get(g_name=genre).movies.all() & Languages.objects.get(l_name=lang).movies.all():
        genre_card = dict()
        make_card_dict(genre_card,obj)
        genre_cards.append(genre_card)
    
    genre_cards = [dict(t) for t in {tuple(d.items()) for d in genre_cards}]
    sort_cards(genre_cards,genre_s_cards)
    return genre_s_cards[:num]

def  movies_data_genre(genre,start,end) : 
    genre_cards = list()  
    genre_s_cards = list()
    if(genre=='Comedy'):
        for obj in Genres.objects.get(g_name='Family').movies.all() :
            genre_card = dict()
            make_card_dict(genre_card,obj)
            genre_cards.append(genre_card)
    if genre=='Adventure':
        for obj in Genres.objects.get(g_name='War').movies.all() :
            genre_card = dict()
            make_card_dict(genre_card,obj)
            genre_cards.append(genre_card)
    if genre == 'Musical':
        for obj in Genres.objects.get(g_name='Music').movies.all() :
            genre_card = dict()
            make_card_dict(genre_card,obj)
            genre_cards.append(genre_card)
    if genre == 'Thriller':
        for obj in Genres.objects.get(g_name='Mystery').movies.all() :
            genre_card = dict()
            make_card_dict(genre_card,obj)
            genre_cards.append(genre_card)
    if genre == 'Darkmovies':
        for obj in Genres.objects.get(g_name='Crime').movies.all() :
            genre_card = dict()
            make_card_dict(genre_card,obj)
            genre_cards.append(genre_card)
        for obj in Genres.objects.get(g_name='Horror').movies.all() :
            genre_card = dict()
            make_card_dict(genre_card,obj)
            genre_cards.append(genre_card)
        genre = 'FilmNoir'
    for obj in Genres.objects.get(g_name=genre).movies.all() :
        genre_card = dict()
        make_card_dict(genre_card,obj)
        genre_cards.append(genre_card)
    
    genre_cards = [dict(t) for t in {tuple(d.items()) for d in genre_cards}]
    sort_cards(genre_cards,genre_s_cards)
    return genre_s_cards[start:end]


def movies_data_language(language,start,end) : 
    language_cards = list()
    language_s_cards = list()
    for obj in Languages.objects.get(l_name=language).movies.all() :
        language_card = dict()
        make_card_dict(language_card,obj)
        language_cards.append(language_card)   
   
    language_cards = [dict(t) for t in {tuple(d.items()) for d in language_cards}]
    sort_cards(language_cards,language_s_cards)
    return language_s_cards[start:end]
    
def movies_data_search(search) :
    movies_cards = list()
    movies_s_cards = list()
    obj = Movies.objects.get(title=search)
    movies_card = dict()
    make_card_dict(movies_card,obj)
    movies_cards.append(movies_card)   
    return movies_cards
    


m_objects = Movies.objects.all()
cards = list()
s_cards = list()
for obj in  m_objects:
    card = dict()
    make_card_dict(card,obj)
    cards.append(card)

sort_cards(cards,s_cards)
