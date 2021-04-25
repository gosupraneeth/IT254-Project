from django.contrib import admin
from .models import Movies,Genres, Languages,User

# Register your models here.

class MoviesAdmin(admin.ModelAdmin):
    list_display=("mid","title","year","duration",'director','writer','production','actors','description','rating')
    filter_horizontal = ('language','genre',)

class GenresAdmin(admin.ModelAdmin):
    list_display = ("g_name",)

class LanguagesAdmin(admin.ModelAdmin):
    list_display = ("l_name",)

class UserAdmin(admin.ModelAdmin):
    list_display=("u_id","u_name","action", "adventure", "darkmovies", "drama", "fantasy", "musical", "romance", "scifi", "thriller", "comedy", "history","hindi", "marathi", "english", "french", "german", "spanish", "russian", "italian", "japanese", "chinese",)



admin.site.register(Movies,MoviesAdmin)
admin.site.register(Genres,GenresAdmin)
admin.site.register(Languages,LanguagesAdmin)
admin.site.register(User,UserAdmin)