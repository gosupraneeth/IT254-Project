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
    #path('language/<str:language>',views.get_m_lang,name="get_m_lang"),
    #path('genre/<str:genre>',views.get_m_genre,name="get_m_genre"),
]