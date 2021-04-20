from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name='home'),
    path('login',views.login_view,name='login'),
    path('signup',views.signup,name='signup'),
    path('loginindex',views.loginindex,name='loginindex'),
    path('logout',views.logout_view,name='logout'),
    path('prefer',views.prefer,name="prefer"),
    path('getdata',views.getdata,name="getdata"),
    path('getchat_mood',views.getchat_mood,name="getchat_mood"),
    path('getchat_genre',views.getchat_genre,name="getchat_genre"),
]