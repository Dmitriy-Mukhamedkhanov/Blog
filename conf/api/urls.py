from django.urls import path

from api.views import Photo, Info, Random, PhotoListView, CommentListView

urlpatterns = [
    path("photos/", PhotoListView.as_view()),
    path("comments/", CommentListView.as_view()),
    path("info/", Info.as_view()),
    path("random/", Random.as_view()),
    ]