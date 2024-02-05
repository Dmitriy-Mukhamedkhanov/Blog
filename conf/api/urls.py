from django.urls import path

# from api.views.likes import AddLike
from api.viewsWWWWWWW import (Info, Random)
from api.views.posts import PhotoListCreateView, PhotoDetailUpdateDeleteView
from api.views.comments import CommentListCreateView, CommentDetailUpdateDeleteView
from api.views.likes import LikeCreateUpdateView

urlpatterns = [
    # Photos
    path("photos/", PhotoListCreateView.as_view()),
    path("photos/<int:id>/", PhotoDetailUpdateDeleteView.as_view()),
    # Comments
    path("comments/", CommentListCreateView.as_view()),
    path("comments/<int:id>/", CommentDetailUpdateDeleteView.as_view()),
    # Likes
    path("likes/", LikeCreateUpdateView.as_view()),
    # Other
    path("info/", Info.as_view()),
    path("random/", Random.as_view()),
]
