from django.urls import path
from . import views


urlpatterns = [
    path("", views.PhotoView.as_view())
]