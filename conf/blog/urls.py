from django.conf.urls.static import static
from django.urls import path
from blog.views.posts import *
from blog.views.comments import *
from blog.views.likes import *
from blog.views.users import *
from conf import settings

urlpatterns = [
    # Home
    path('', BlogView.as_view(), name='home'),

    # User
    path('user_page/', dashboard, name='dashboard'),
    path('login/', LoginBlogView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    # path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    # path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    # Post
    path('posts/', CreatePostView.as_view(), name='transition_page'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='page'),
    path('posts/<int:pk>/delete/', PhotoDeleteView.as_view(), name='delete'),
    path('posts/change/<int:pk>/change/', ChangePostView.as_view(), name='change'),
    path('posts/search/', SearchPostsView.as_view(), name='search_result'),

    # Comment
    path('posts/<int:pk>/comments/', AddComments.as_view(), name='add_comments'),
    path('comments/<int:pk>/delete/', CommentDeleteView.as_view(), name='delete_comment'),

    # Like
    path('posts/<int:pk>/add_likes/', AddLike.as_view(), name='add_likes'),
    path('posts/<int:pk>/delete_likes/', DeleteLike.as_view(), name='delete_likes'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
