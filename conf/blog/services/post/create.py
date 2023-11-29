from django import forms
from service_objects.fields import ModelField
from service_objects.services import Service

from blog.models import User, Photo


class PostCreateService(Service):
    name = forms.CharField()
    description = forms.CharField()
    image = forms.ImageField()
    user = ModelField(User)

    def process(self):
        Photo.objects.create(
            name=self.cleaned_data['name'],
            image=self.cleaned_data['image'],
            description=self.cleaned_data['description'],
            author=self.cleaned_data['user']
        )
        return self
