from django.urls import path

from api.views import Photo, Info, Random

urlpatterns = [
    path("test/", Photo.as_view()),
    path("info/", Info.as_view()),
    path("random/", Random.as_view()),
    ]