from django.contrib.auth import login, authenticate, logout
from users.forms import SignUpForm
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from users.models import Movies , Languages ,Genres, User
import random as rd
from users.utils import *


# Create your views here.
GENRE = ["action", "adventure", "darkmovies", "drama", "fantasy", "musical", "romance", "scifi", "thriller", "comedy", "history"]
LANGUAGE = ["hindi", "marathi", "english", "french", "german", "spanish", "russian", "italian", "japanese", "chinese"]
def home(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("loginindex"))
    return render(request,'users/home.html')

def User_(request,userid):
    if not (request.user.is_authenticated and request.user.username==userid):
        return HttpResponseRedirect(reverse("login"))
    user=User.objects.get(u_id=userid)
    return render(request, "users/user.html",{
        "user":user,
    })

def loginindex(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    name=request.user.username
    try:
        user=User.objects.get(u_id=name)
    except:
        user=User(u_id=request.user.username,u_name=request.user.first_name +" " + request.user.last_name)
        user.save()
    return HttpResponseRedirect(reverse('User',args=(user.u_id,)))


def login_view(request):
    if request.method =="POST":
        username= request.POST['username']
        password= request.POST['password']
        user =authenticate(request, username=username, password= password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("loginindex"))
        else:
            return render(request, "users/home.html",{
                "message": "Invalid Credentials",
                'logincard':True
            })

    return render(request, "users/home.html",{
        'logincard':True
    })

def prefer(request):
    return render(request, "users/prefer.html")

def prefer_genre(request) :
    return render(request, "users/prefer_genre.html")

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('prefer')
    else:
        form = SignUpForm()
    return render(request, 'users/home.html', {
        'form': form,
        'signupcard':True
    })

def logout_view(request):
    logout(request)
    return redirect('home')

def getdata(request):
    start = int(request.GET.get("start") or 0)
    end = int(request.GET.get("end") or (start + 9))
    if not request.user.is_authenticated:
        cards = movies_data_load(start,end)
        return JsonResponse({
            "cards" : cards,
        })
    uname = request.user.username
    user_prio = User.objects.get(u_id=uname)
    genre=list()
    lang = list()
    #sort this properly to get accurate cards
    genre = [str(ge).capitalize() for ge in GENRE if obj_val(user_prio,ge)>0]
    lang = [str(l).capitalize() for l in LANGUAGE if obj_val(user_prio,l)>0]
    cards = movies_data_prio(lang.copy(),genre.copy(),start,end)
    return JsonResponse({
        "cards" : cards,
    })

    

def getchat_mood(request):
    mood = request.GET.get("mood") or "happy"
    lang = request.GET.get("lang") or "English"
    cards = movies_data_load_mood(mood,lang)
    return JsonResponse({
        "cards" : cards,
    })

def getchat_genre(request):
    genre = request.GET.get("genre") or "Action"
    num = int(request.GET.get("count") or 5)
    lang = request.GET.get("lang") or "English"
    cards = movies_data_load_genre(genre,lang,num)
    return JsonResponse({
        "cards" : cards,
    })

def get_single_card(request):
    mid = request.GET.get("mid")
    card = dict()
    make_card_dict(card,Movies.objects.get(mid=mid))
    cards=list()
    cards.append(card)
    return JsonResponse({
        "cards" : cards,
    })

def search_bar(request) : 
    m_name = request.GET.get("m_name")
    print(m_name)
    card = dict()
    cards=list()
    try:
        obj=Movies.objects.get(title=m_name)
        make_card_dict(card,obj)
        cards.append(card)
        return JsonResponse({
            "cards" : cards,
        })
    except:
        message = {"message":"No Movie found"}
        cards.append(message)
        return JsonResponse({
            "cards" : cards,
        })

def get_data_g_l(request):
    language = str(request.GET.get("lang")).split(',')
    genre = str(request.GET.get("genre")).split(',')
    start = int(request.GET.get("start") or 0)
    end = int(request.GET.get("end") or (start + 9))
    cards = list()
    cards = movies_data_lg(language.copy(),genre.copy(),start,end)
    if(len(cards)!=0):
        return JsonResponse({
            "cards" : cards,
        })
    else:
        message = {"message":"No more Movie found"}
        cards.append(message)
        return JsonResponse({
            "cards" : cards,
        })

def incr_priority(request):
    max_val = 200
    name = str(request.GET.get("name")).lower()
    num = int(request.GET.get("num") or 1)
    genre_list = list()
    lang_list=list()
    uname = request.user.username
    try:
        user_prio = User.objects.get(u_id=uname)
    except:
        user_prio=User(u_id=request.user.username,u_name=request.user.first_name +" " + request.user.last_name)
        user_prio.save()
    for ge in GENRE:
        genre_list.append(obj_val(user_prio,ge))
    for lang in LANGUAGE:
        lang_list.append(obj_val(user_prio,lang))
    
    if(len(genre_list)!=0 and max(genre_list)>=max_val):
        mi_v = min(i for i in genre_list if i>0)
        genre_list = [x - mi_v + 1 if x > 0 else x for x in genre_list]
        for ge,val in zip(GENRE,genre_list):
            user_prio= obj_val_save(user_prio,ge,val)
            user_prio.save()
    if(len(lang_list)!=0 and max(lang_list)>=max_val):
        mi_v = min(i for i in lang_list if i>0)
        lang_list = [x - mi_v + 1 if x > 0 else x for x in lang_list]
        for lang,val in zip(LANGUAGE,lang_list):
            user_prio= obj_val_save(user_prio,lang,val)
            user_prio.save()

    if(name in GENRE):
        user_prio=obj_val_save(user_prio,name,obj_val(user_prio,name)+num)
        user_prio.save()
    elif(name in LANGUAGE):
        user_prio=obj_val_save(user_prio,name,obj_val(user_prio,name)+num)
        user_prio.save()
    else:
        return JsonResponse({
            "message":"Failed priority incr",
        })
    print(name)
    return JsonResponse({
        "message":"Done",
    })