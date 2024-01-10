from rest_framework.response import Response
from rest_framework.views import APIView
import random
from api.serializers import PhotoSerializer, CommentSerializer
from blog.models import Photo, Comment

class PhotoListView(APIView):
    def get(self, request):
        photos = Photo.objects.all()
        serializer = PhotoSerializer(photos, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = PhotoSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        photo = Photo.objects.create(
            name=serializer.validated_data['name'],
            description=serializer.validated_data['description'],
            image=serializer.validated_data['image'],
            author=serializer.validated_data['author'],
        )
        return Response(PhotoSerializer(photo).data)


class CommentListView(APIView):
    def get(self, request):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = CommentSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        comment = Comment.objects.create(
            text_comment=serializer.validated_data['text_comment'],
            author_comment=serializer.validated_data['author_comment'],
            image_comment=serializer.validated_data['image_comment'],
        )
        return Response(CommentSerializer(comment).data)


class Info(APIView):
    def get(self, request):
        return Response({"name": "Петя", "last_name": "Иванов",
                         "age": 20})


class Random(APIView):
    def get(self, request):
        rand = random.randint(1, 100)
        return Response({"number": rand})
