from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from blog.form import LoginForm
from blog.models import Photo


@login_required
def dashboard(request):
    person_photo = Photo.objects.filter(author=request.user)
    # person_photo = Photo.objects.filter(author__id=request.user.id)
    return render(request, 'user_page.html', {'person_photo': person_photo})


class LoginBlogView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'registration/login.html', {'form': form})

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return HttpResponse('Попробуйте снова')


def logout_view(request):
    logout(request)  # вывести на главную страницу
    return redirect('home')
