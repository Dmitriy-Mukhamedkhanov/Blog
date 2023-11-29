from django import forms
from service_objects.services import Service
from blog.models import Photo


class PhotoDeleteViewService(Service):
    id = forms.IntegerField()
    def process(self):
        Photo.objects.get(id=self.cleaned_data['id']).delete()

