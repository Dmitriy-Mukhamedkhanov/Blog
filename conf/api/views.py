from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
import random
from api.serializers import PhotoSerializer, CommentSerializer
from blog.models import Photo, Comment, User


# Create your views here.
class PhotoListView(APIView):
    def get(self, request):
        photos = Photo.objects.all()
        serializer = PhotoSerializer(photos, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = PhotoSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        author = User.objects.filter(id=serializer.validated_data['author'])
        if len(author) == 0:
            return Response({'error': 'ошибка'}, status=404)
        photo = Photo.objects.create(
            name=serializer.validated_data['name'],
            description=serializer.validated_data['description'],
            image=serializer.validated_data['image'],
            author_id=serializer.validated_data['author'],
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

        # text_comment_r = request.data["text_comment"]
        # author_comment_r = request.data["author_comment"]
        # image_comment_r = request.data["image_comment"]
        image = Photo.objects.filter(id=serializer.validated_data['image_comment'])
        if not image.exists():
            return Response({'error': 'фотографии с таким image_comment не существует'}, status=404)
        comment = Comment.objects.create(
            text_comment=serializer.validated_data['text_comment'],
            author_comment=serializer.validated_data['author_comment'],
            image_comment_id=serializer.validated_data['image_comment'],
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
