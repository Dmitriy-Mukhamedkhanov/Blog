from django.urls import path

from api.views import PhotosListView, Info, Random

urlpatterns = [
    path("photos/", PhotosListView.as_view()),
    path("info/", Info.as_view()),
    path("random/", Random.as_view()),
    ]