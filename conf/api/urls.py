from django.urls import path

from api.viewsWWWWWWW import (Info, Random)
from api.views.posts import PhotoListCreateView, PhotoDetailUpdateDeleteView
from api.views.comments import CommentListCreateView, CommentDetailUpdateDeleteView

urlpatterns = [
    # Photos
    path("photos/", PhotoListCreateView.as_view()),
    path("photos/<int:id>/", PhotoDetailUpdateDeleteView.as_view()),
    # Comments
    path("comments/", CommentListCreateView.as_view()),
    path("comments/<int:id>/", CommentDetailUpdateDeleteView.as_view()),
    # Other
    path("info/", Info.as_view()),
    path("random/", Random.as_view()),
]
