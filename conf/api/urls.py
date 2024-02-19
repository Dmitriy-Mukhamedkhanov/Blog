from django.urls import path

from api.views.posts import PhotoListCreateView, PhotoDetailUpdateDeleteView
from api.views.comments import CommentListCreateView, CommentDetailUpdateDeleteView
from api.views.likes import LikeListCreateUpdateDeleteView

urlpatterns = [
    # Photos
    path("photos/", PhotoListCreateView.as_view()),
    path("photos/<int:id>/", PhotoDetailUpdateDeleteView.as_view()),
    # Comments
    path("comments/", CommentListCreateView.as_view()),
    path("comments/<int:id>/", CommentDetailUpdateDeleteView.as_view()),
    # Likes
    path("photos/<int:id>/likes/", LikeListCreateUpdateDeleteView.as_view())
]
