from django.db import models

# Create your models here.

#user details 
class User(models.Model):
    u_id = models.CharField(max_length=30,primary_key=True)
    u_name = models.CharField(max_length=64)
    hindi   = models.IntegerField(default=0)
    marathi = models.IntegerField(default=0)
    english = models.IntegerField(default=0)
    french  = models.IntegerField(default=0)
    german  = models.IntegerField(default=0)
    spanish = models.IntegerField(default=0)
    russian = models.IntegerField(default=0)
    italian = models.IntegerField(default=0)
    japanese=models.IntegerField(default=0)
    chinese = models.IntegerField(default=0)
    comedy  = models.IntegerField(default=0)
    adventure= models.IntegerField(default=0)
    musical =  models.IntegerField(default=0)
    thriller= models.IntegerField(default=0)
    drama   = models.IntegerField(default=0)
    romance = models.IntegerField(default=0)
    action  = models.IntegerField(default=0)
    darkmovies = models.IntegerField(default=0)
    fantasy = models.IntegerField(default=0)
    scifi   = models.IntegerField(default=0)
    history = models.IntegerField(default=0)



#database

class Movies(models.Model):
    mid = models.CharField(max_length=20, primary_key= True)
    title = models.CharField(max_length=100)
    year = models.FloatField()
    duration = models.FloatField()
    director = models.CharField(max_length=150)
    writer = models.CharField(max_length=150)
    production = models.CharField(max_length=200)
    actors = models.TextField()
    description = models.TextField()
    rating = models.FloatField()

class Languages(models.Model):
    l_name =  models.CharField(max_length=64)
    movies = models.ManyToManyField(Movies,blank=True,related_name="language")

class Genres(models.Model):
    g_name = models.CharField(max_length=64)
    movies = models.ManyToManyField(Movies,blank=True,related_name="genre")