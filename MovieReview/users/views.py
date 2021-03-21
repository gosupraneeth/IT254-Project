from django.contrib.auth import login, authenticate, logout
from users.forms import SignUpForm
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.

def home(request):
    return render(request,'users/home.html')