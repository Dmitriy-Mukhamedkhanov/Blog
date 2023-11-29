from django.shortcuts import render, redirect
from django.views import View

from blog.form import FormCreateObject, FormChangeObject
from blog.services.post.change import ChangePostViewService
from blog.services.post.delete import PhotoDeleteViewService
from blog.services.post.search import SearchPostsViewService
from blog.services.post.create import PostCreateService
from blog.services.post.detail import PostDetailService
from blog.services.post.show_all import BlogViewService


class BlogView(View):
    def get(self, request):
        outcome = BlogViewService.execute({})
        return render(self.request, 'index.html',
                      context={'show': outcome})

class PostDetailView(View):
    '''Гиперссылка Отдельная страница записи'''

    def get(self, request, pk):
        outcome = PostDetailService.execute({"id": pk})
        # post = Photo.objects.get(id=pk)
        # comment = Comment.objects.filter(image_comment=post)
        return render(request, 'blog_page.html',
                context={
                            'post': outcome["photo"],
                            'comment': outcome["comments"]
                }
        )


class SearchPostsView(View):
    def get(self, request):
        if request.GET.get(
                'data'):  # data - ключ. Условие: если запрос есть/выполняется, получаем значение (что ввели в браузере)
            gets = request.GET.get('data')
            outcome = SearchPostsViewService.execute({"data": gets})
        return render(request, 'index.html', context={'show': outcome})


class PhotoDeleteView(View):
    def get(self, request, pk):
        PhotoDeleteViewService.execute({"id": pk})
        return redirect('dashboard')


class CreatePostView(View):
    def get(self, request):
        userform = FormCreateObject()
        return render(request, "transition_page.html",
                      {"form": userform})

    def post(self, request):
        outcome = PostCreateService.execute(
            {
                "name": request.POST["name"],
                "description": request.POST["description"],
                "user": request.user
            },
            {
                "image": request.FILES["image"],
            }
        )
        return redirect('dashboard')


class ChangePostView(View):
    def get(self, request, pk):
        userform = FormChangeObject()
        return render(request, "transition_page.html", {"form": userform})

    def post(self, request, pk):

        outcome = ChangePostViewService.execute(
            {
                "name": request.POST["name"],
                "description": request.POST["description"],
                "user": request.user,
                "id": pk
            },
            {
                "image": request.FILES.get("image"),
            }
        )
        return redirect('dashboard')
