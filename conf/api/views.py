from rest_framework.response import Response
from rest_framework.views import APIView
import random

# Create your views here.
class Photo(APIView):
    def get(self, request):
        return Response({"test": 1})

class Info(APIView):
    def get(self, request):
        return Response({"name": "Петя","last_name": "Иванов",
                         "age": 20})
class Random(APIView):
    def get(self, request):
        rand = random.randint(1,100)
        return Response({"number": rand})

