from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from photo.models import Photo


class PhotoView(ListView):
    """список фото"""
    model = Photo
    queryset = Photo.objects.filter(draft=False)
    # template_name = "photo/photo_list.html"
    # def get(self, request):
    #     photo = Photo.objects.all()
    #     return render(request, "photo/photo_list.html", {"photo_list": photo})


class PhotoDetailView(DetailView):
    """список фото"""
    model = Photo
    slug_field = "url"


    # def get(self, request, slug):
    #                                     # try:
    #                                     #     photo = Photo.objects.get(pk=pk)
    #                                     # except Photo.DoesNotExist as err:
    #                                     #     return HttpResponse(status=404, content=f"No photo with id {pk}")
    #     photo = Photo.objects.get(url=slug)
    #     return render(request, "photo/photo_detail.html", {"photo": photo})
