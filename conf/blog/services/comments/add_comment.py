from django import forms
from service_objects.fields import ModelField
from service_objects.services import Service
from blog.models import Comment, Photo, User


class AddCommentsService(Service):
    text_comment = forms.CharField()
    author_comment = ModelField(User)
    id = forms.IntegerField()
    def process(self):
        photo = Photo.objects.get(id=self.cleaned_data["id"])
        Comment.objects.create(text_comment=self.cleaned_data["text_comment"],
                               author_comment=self.cleaned_data["author_comment"],
                               image_comment=photo)
