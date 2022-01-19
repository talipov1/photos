from django.contrib import admin
from .models import Categories, Actor, Genre, Photo, Rating, Review

admin.site.register(Categories)
admin.site.register(Actor)
admin.site.register(Genre)
admin.site.register(Photo)
admin.site.register(Rating)
admin.site.register(Review)


