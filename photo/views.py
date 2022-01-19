from django.shortcuts import render
from django.views.generic.base import View
from .models import Photo



class PhotoView(View):
    """список фото"""
    def get(self, request):
        photo = Photo.objects.all()
        return render(request, "photo/movies.html", {"photo_list": photo})



