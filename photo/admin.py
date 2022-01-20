from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Categories, Actor, Genre, Photo, Rating, Review


class PhotoModelAdmin(ModelAdmin):
    list_display = ("id", "name", "slogan")


admin.site.register(Categories)
admin.site.register(Actor)
admin.site.register(Genre)
admin.site.register(Photo, PhotoModelAdmin)
admin.site.register(Rating)
admin.site.register(Review)
