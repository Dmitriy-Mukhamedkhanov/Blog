from rest_framework.response import Response
from rest_framework.views import APIView
import random

from blog.models import Photo


# Create your views here.
class PhotosListView(APIView):
    def get(self, request):
        photos = Photo.objects.all().values()
        return Response({"photos": photos})

class Info(APIView):
    def get(self, request):
        return Response({"name": "Петя","jjj": "Петя","last_name": "Иванов",
                         "age": 20})
class Random(APIView):
    def get(self, request):
        rand = random.randint(1,100)
        return Response({"number": rand})

