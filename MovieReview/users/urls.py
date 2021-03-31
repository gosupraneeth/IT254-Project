from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name='home'),
    path('login',views.login_view,name='login'),
    path('signup',views.signup,name='signup'),
    path('loginindex',views.loginindex,name='loginindex'),
    path('logout',views.logout_view,name='logout'),
]