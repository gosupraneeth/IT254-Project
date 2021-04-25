from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name='home'),
    path('login',views.login_view,name='login'),
    path('signup',views.signup,name='signup'),
    path('loginindex',views.loginindex,name='loginindex'),
    path('logout',views.logout_view,name='logout'),
    path('prefer',views.prefer,name="prefer"),
    path('prefer_genre',views.prefer_genre,name = 'prefer_genre'),
    path('getdata',views.getdata,name="getdata"),
    path('getchat_mood',views.getchat_mood,name="getchat_mood"),
    path('getchat_genre',views.getchat_genre,name="getchat_genre"),
    path('get_single_card',views.get_single_card,name="get_single_card"),
    path('searchbar',views.search_bar, name = 'searchbar'),
    path('get_data_g_l',views.get_data_g_l, name = 'get_data_g_l'),
    path('incr_priority',views.incr_priority,name="incr_priority"),
    path('user/<str:userid>',views.User_,name="User"),
]