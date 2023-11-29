from django import forms
from service_objects.services import Service
from blog.models import Comment, Photo


class PostDetailService(Service):
    id = forms.IntegerField()
    def process(self):
        post = Photo.objects.get(pk=self.cleaned_data['id'])
        comment = Comment.objects.filter(image_comment=post)
        return {
            "photo": post,
            "comments": comment
        }
