from django.urls import path
from . import views


urlpatterns = [
    path("", views.PhotoView.as_view()),
    path("<slug:slug>/", views.PhotoDetailView.as_view(), name='photo_detail')
]