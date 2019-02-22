# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Movies(models.Model):

    index = models.IntegerField(primary_key=True, blank=True, null=False)
    
    color = models.TextField(blank=True, null=True)
    director_name = models.TextField(blank=True, null=True)
    duration = models.FloatField(blank=True, null=True)
    actor_2_name = models.TextField(blank=True, null=True)
    genres = models.TextField(blank=True, null=True)
    actor_1_name = models.TextField(blank=True, null=True)
    movie_title = models.TextField(blank=True, null=True)
    actor_3_name = models.TextField(blank=True, null=True)
    plot_keywords = models.TextField(blank=True, null=True)
    language = models.TextField(blank=True, null=True)
    country = models.TextField(blank=True, null=True)
    title_year = models.IntegerField(blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'movies'
    
    def info(self):
        _info_attrs = ['color', 'director_name', 'duration', 'actor_1_name', 'actor_2_name', 'genres', 'movie_title', 'actor_3_name', 'language', 'plot_keywords', 'title_year', 'country']
        return {x: getattr(self, x) for x in _info_attrs}
        
    def __str__(self):
        return f'{self.movie_title}: {self.title_year}'
