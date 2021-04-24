from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name='home'),
    path('search',views.search_bar, name = 'search'),
    path('login',views.login_view,name='login'),
    path('signup',views.signup,name='signup'),
    path('loginindex',views.loginindex,name='loginindex'),
    path('logout',views.logout_view,name='logout'),
    path('prefer',views.prefer,name="prefer"),
    path('getdata',views.getdata,name="getdata"),
    path('getchat_mood',views.getchat_mood,name="getchat_mood"),
    path('getchat_genre',views.getchat_genre,name="getchat_genre"),
    path('get_single_card',views.get_single_card,name="get_single_card"),
    path('get_genre',views.get_genre,name = "get_genre"),
    path('get_language',views.get_language, name = 'get_language'),
    path('prefer_genre',views.prefer_genre,name = 'prefer_genre'),
    path('home',views.home, name = 'home'),
]