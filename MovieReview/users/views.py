from django.contrib.auth import login, authenticate, logout
from users.forms import SignUpForm
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from users.models import Movies , Languages ,Genres
import random as rd
from users.utils import *


# Create your views here.

def home(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("loginindex"))
    return render(request,'users/home.html')

def loginindex(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request, "users/user.html")


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

def home(request) : 
    return render(request, "users/home.html")


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
    cards = movies_data_load(start,end)
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
    
def search_bar(request) : 
    search = request.GET.get("search")
    cards = movies_data_search(search)
    return JsonResponse({
        "cards" : cards,
    })
    
def get_genre(request) : 
    genre = request.GET.get("genre")
    start = int(request.GET.get("start") or 0)
    end = int(request.GET.get("end") or (start + 9))
    cards = movies_data_genre(genre,start,end)
    return JsonResponse({
        "cards" : cards,
    })
    
def get_language(request,name):
    language = name
    start = int(request.GET.get("start") or 0)
    end = int(request.GET.get("end") or (start + 9))
    cards = movies_data_language(language,start,end)
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