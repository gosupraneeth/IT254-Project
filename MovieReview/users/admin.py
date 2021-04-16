from django.contrib import admin
from .models import Movies,Genres, Languages

# Register your models here.

class MoviesAdmin(admin.ModelAdmin):
    list_display=("mid","title","year","duration",'director','writer','production','actors','description','rating')
    filter_horizontal = ('language','genre',)

class GenresAdmin(admin.ModelAdmin):
    list_display = ("g_name",)

class LanguagesAdmin(admin.ModelAdmin):
    list_display = ("l_name",)

admin.site.register(Movies,MoviesAdmin)
admin.site.register(Genres,GenresAdmin)
admin.site.register(Languages,LanguagesAdmin)