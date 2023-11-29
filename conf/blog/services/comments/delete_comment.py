from django import forms
from service_objects.services import Service
from blog.models import Comment


class CommentDeleteViewService(Service):
    id = forms.IntegerField()
    def process(self):
        coment = Comment.objects.get(id=self.cleaned_data['id'])
        photo = coment.image_comment
        coment.delete()
        return photo.id

