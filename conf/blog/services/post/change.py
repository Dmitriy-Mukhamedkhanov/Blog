from django import forms
from service_objects.fields import ModelField
from service_objects.services import Service

from blog.models import User, Photo


class ChangePostViewService(Service):
    name = forms.CharField(required=False)
    description = forms.CharField(required=False)
    image = forms.ImageField(required=False)
    id = forms.IntegerField()
    user = ModelField(User)

    def process(self):
        name = self.cleaned_data['name']
        image =self.cleaned_data['image']
        description = self.cleaned_data['description']
        photo = Photo.objects.get(id=self.cleaned_data['id'])
        if name:
            photo.name = name
        if image:
            photo.image = image
        if description:
            photo.description = description
        photo.save()

