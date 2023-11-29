from django import forms
from service_objects.services import Service
from blog.models import Photo


class SearchPostsViewService(Service):
    data = forms.CharField()
    def process(self):
        posts = Photo.objects.filter(name__icontains=self.cleaned_data['data'])
        return posts
