import random as rd
from users.models import Movies , Languages ,Genres

GENRE = ["Action","Adventure","Crime","Drama","Fantasy","Musical","Romance","Thriller","Comedy","History"]
GENRE2 = ["Action", "Adventure", "DarkMovies", "Drama", "Fantasy", "Musical", "Romance", "SciFi", "Thriller", "Comedy", "History"]
LANG = ['Hindi','Marathi','English','French','German','Spanish','Russian','Italian','Japanese','Chinese']

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

def  genre_callable(genre) : 
    if(genre=='Comedy'):
        obj = Genres.objects.get(g_name='Family').movies.all()
        obj = obj.union(Genres.objects.get(g_name='Comedy').movies.all())
    elif genre=='Adventure':
        obj = Genres.objects.get(g_name='War').movies.all()
        obj = obj.union(Genres.objects.get(g_name='Adventure').movies.all())
    elif genre == 'Musical':
        obj = Genres.objects.get(g_name='Music').movies.all()
        obj = obj.union(Genres.objects.get(g_name='Musical').movies.all())
    elif genre == 'Thriller':
        obj = Genres.objects.get(g_name='Mystery').movies.all()
        obj = obj.union(Genres.objects.get(g_name='Thriller').movies.all())
    elif genre == 'DarkMovies':
        obj = Genres.objects.get(g_name='Crime').movies.all()
        obj = obj.union(Genres.objects.get(g_name='Horror').movies.all())
        obj = obj.union(Genres.objects.get(g_name='FilmNoir').movies.all())
    else:
        obj = Genres.objects.get(g_name=genre).movies.all()
    
    return obj

def sort_cards(cards,s_cards):
    for s in sorted(cards, key=lambda y: y['rating'],reverse=True):
        s_cards.append(s)


def movies_data_load(start,end):
    return s_cards[start-1:end]

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
    if(genre=='Darkmovies'):
        genre='DarkMovies'
    genre = genre.capitalize()
    for obj in genre_callable(genre) & Languages.objects.get(l_name=lang).movies.all():
        genre_card = dict()
        make_card_dict(genre_card,obj)
        genre_cards.append(genre_card)
    
    genre_cards = [dict(t) for t in {tuple(d.items()) for d in genre_cards}]
    sort_cards(genre_cards,genre_s_cards)
    return genre_s_cards[:num]


def movies_data_lg(language,gen,start,end):
    lg_cards = list()
    lg_s_cards = list()
    if(len(gen)==1 and gen[0]==''):
        if(len(language)==1 and language[0]==''):
            return s_cards[start-1:end]
        else:
            x = Languages.objects.get(l_name=language[0]).movies.all()
            for i in range(1,len(language)):
                x=x.union(Languages.objects.get(l_name=language[i]).movies.all())
    else:
        if(len(language)==1 and language[0]==''):
            x = genre_callable(gen[0])
            for i in range(1,len(gen)):
                x=x.union(genre_callable(gen[i]))
        else:
            x = Languages.objects.get(l_name=language[0]).movies.all()
            for i in range(1,len(language)):
                x=x.union(Languages.objects.get(l_name=language[i]).movies.all())
            
            y = genre_callable(str(gen[0]))
            for i in range(1,len(gen)):
                y=y.union(genre_callable(str(gen[i])))
            
            x = x.intersection(y)

    for obj in x:
        lg_card = dict()
        make_card_dict(lg_card,obj)
        lg_cards.append(lg_card)
    lg_cards = [dict(t) for t in {tuple(d.items()) for d in lg_cards}]
    sort_cards(lg_cards,lg_s_cards)
    if(start<=len(lg_s_cards)):
        return lg_s_cards[start-1:end]
    else:
        return []

def movies_data_prio(lang,gen,start,end):
    print(lang,gen)
    prio_s_f_cards = list()
    for i in range(max(len(lang),len(gen))):
        prio_cards =list()
        prio_s_cards=list()
        if(i<len(gen) and gen[i]=='Darkmovies'):
            gen[i]='DarkMovies'
        if(i<len(gen) and gen[i]=='Scifi'):
            gen[i]='SciFi'
        if i<len(lang):
            x = Languages.objects.get(l_name=lang[i]).movies.all()
        if i<len(gen):
            y = genre_callable(str(gen[i]))
            x = x.intersection(y)
        for obj in x:
            prio_card = dict()
            make_card_dict(prio_card,obj)
            prio_cards.append(prio_card)
        prio_cards = [dict(t) for t in {tuple(d.items()) for d in prio_cards}]
        sort_cards(prio_cards,prio_s_cards)
        for card in prio_s_cards:
            prio_s_f_cards.append(card)
        if(end<=len(prio_s_f_cards)):
            print(1)
            return prio_s_f_cards[start-1:end]
    for i in range(len(LANG)):
        if LANG[i] not in lang and GENRE2[i] not in gen:
            x = Languages.objects.get(l_name=LANG[i]).movies.all()
            y = genre_callable(str(GENRE2[i]))
            x = x.intersection(y)
            for obj in x:
                prio_card = dict()
                make_card_dict(prio_card,obj)
                prio_cards.append(prio_card)
            prio_cards = [dict(t) for t in {tuple(d.items()) for d in prio_cards}]
            sort_cards(prio_cards,prio_s_cards)
            for card in prio_s_cards:
                prio_s_f_cards.append(card)
            if(end<=len(prio_s_f_cards)):
                print(2)
                return prio_s_f_cards[start-1:end]
    print(3)
    return s_cards[start-1:end]


def obj_val(obj,name):
    if(name=='action'):
        return obj.action
    if(name=='adventure'):
        return obj.adventure
    if(name=='darkmovies'):
        return obj.darkmovies
    if(name=='drama'):
        return obj.drama
    if(name=='fantasy'):
        return obj.fantasy
    if(name=='musical'):
        return obj.musical
    if(name=='romance'):
        return obj.romance
    if(name=='scifi'):
        return obj.scifi
    if(name=='thriller'):
        return obj.thriller
    if(name=='comedy'):
        return obj.comedy
    if(name=='history'):
        return obj.history
    if(name=='hindi'):
        return obj.hindi
    if(name=='marathi'):
        return obj.marathi
    if(name=='english'):
        return obj.english
    if(name=='french'):
        return obj.french
    if(name=='german'):
        return obj.german
    if(name=='spanish'):
        return obj.spanish
    if(name=='russian'):
        return obj.russian
    if(name=='italian'):
        return obj.italian
    if(name=='japanese'):
        return obj.japanese
    if(name=='chinese'):
        return obj.chinese

def obj_val_save(obj,name,val):
    if(name=='action'):
        obj.action = val
    if(name=='adventure'):
        obj.adventure = val
    if(name=='darkmovies'):
        obj.darkmovies = val
    if(name=='drama'):
        obj.drama = val
    if(name=='fantasy'):
        obj.fantasy = val
    if(name=='musical'):
        obj.musical = val
    if(name=='romance'):
        obj.romance = val
    if(name=='scifi'):
        obj.scifi = val
    if(name=='thriller'):
        obj.thriller = val
    if(name=='comedy'):
        obj.comedy = val
    if(name=='history'):
        obj.history = val
    if(name=='hindi'):
        obj.hindi = val
    if(name=='marathi'):
        obj.marathi = val
    if(name=='english'):
        obj.english = val
    if(name=='french'):
        obj.french = val
    if(name=='german'):
        obj.german = val
    if(name=='spanish'):
        obj.spanish = val
    if(name=='russian'):
        obj.russian = val
    if(name=='italian'):
        obj.italian = val
    if(name=='japanese'):
        obj.japanese = val
    if(name=='chinese'):
        obj.chinese = val
    return obj


m_objects = Movies.objects.all()
cards = list()
s_cards = list()
for obj in  m_objects:
    card = dict()
    make_card_dict(card,obj)
    cards.append(card)

sort_cards(cards,s_cards)
