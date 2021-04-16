import random as rd
from users.models import Movies , Languages ,Genres

m_objects = Movies.objects.all()
cards = list()
s_cards = list()
for obj in  m_objects:
    card = dict()
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
    cards.append(card)
for s in sorted(cards, key=lambda y: y['rating'],reverse=True):
    s_cards.append(s)


def movies_data_load(start,end):
    return s_cards[start:end]