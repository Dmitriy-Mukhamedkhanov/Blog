from rest_framework.response import Response
from rest_framework.views import APIView
import random

from blog.models import Photo, Comment


# Create your views here.
class PhotoListView(APIView):
    def get(self, request):
        photos = Photo.objects.all().values()
        return Response({"photos": photos})

    def post(self, request):
        name_r = request.data["name"]
        description_r = request.data["description"]
        image_r = request.data["image"]
        author_r = request.data["author"]
        photo = Photo.objects.create(
            name=name_r,
            description=description_r,
            image=image_r,
            author_id=author_r
        )

        return Response({
            'name': name_r,
            'description': description_r,
            'image': str(image_r),
            'author_id': author_r
        })

class CommentListView(APIView):
    def get(self, request):
        comments = Comment.objects.all().values()
        return Response({"comments": comments})

    def post(self, request):
        text_comment_r = request.data["text_comment"]
        author_comment_r = request.data["author_comment"]
        image_comment_r = request.data["image_comment"]

        comment = Comment.objects.create(
            text_comment=text_comment_r,
            author_comment=author_comment_r,
            image_comment_id=image_comment_r,
        )

        return Response({
            'text_comment': text_comment_r,
            'author_comment': author_comment_r,
            'image_comment_id': image_comment_r
        })

class Info(APIView):
    def get(self, request):
        return Response({"name": "Петя", "last_name": "Иванов",
                         "age": 20})


class Random(APIView):
    def get(self, request):
        rand = random.randint(1, 100)
        return Response({"number": rand})
