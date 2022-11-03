from unittest.util import _MAX_LENGTH
from django.db import models
from datetime import datetime
# Create your models here.

class Artiste(models.Model): 
   first_name = models.CharField(max_length = 255) 
   last_name = models.CharField(max_length =255)
   age = models.IntegerField()

   def __str__(self):
       return self.first_name
   
  
class Song(models.Model):   
    artiste = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    title = models.CharField(max_length = 255)   
    date_released = models.DateField(default=datetime.now, blank=True)  
    likes = models.IntegerField(default=0) 

    def __str__(self):
       return self.title


class Lyric(models.Model): 
    artiste = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete= models.CASCADE)
    content = models.CharField(max_length = 2000) 
    
   

   