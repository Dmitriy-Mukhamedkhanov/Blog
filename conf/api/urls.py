from django.urls import path

from api.views import Photo, Info, Random, CommentListView, PhotoListCreateView, PhotoUpdateView, CommentUpdateView, \
    PhotoInfoView

urlpatterns = [
    path("photos/", PhotoListCreateView.as_view()),
    path("photos/<int:id>/", PhotoUpdateView.as_view()),
    path("posts/<int:id>/", PhotoInfoView.as_view()),
    path("comments/", CommentListView.as_view()),
    path("comments/<int:id>/", CommentUpdateView.as_view()),
    path("info/", Info.as_view()),
    path("random/", Random.as_view()),
]
