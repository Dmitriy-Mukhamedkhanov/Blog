from rest_framework.response import Response
from rest_framework.views import APIView
import random
from api.serializers import PhotoSerializer, CommentSerializer, PhotoUpdateSerializer, CommentUpdateSerializer, \
    PhotoInfoSerializer
from blog.models import Photo, Comment


class PhotoListCreateView(APIView):
    def get(self, request):
        photos = Photo.objects.all()
        serializer = PhotoSerializer(photos, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = PhotoSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        photo = serializer.save()

        return Response(PhotoSerializer(photo).data)


class PhotoInfoView(APIView):
    def get(self, request, id):
        photo = Photo.objects.filter(id=id)
        photo = photo.first()
        if not photo:
            return Response({
                'error': 'not found photo with this id'
            })
        serializer = PhotoInfoSerializer(photo)
        return Response(serializer.data)


class PhotoUpdateView(APIView):
    def patch(self, request, id):
        photo = Photo.objects.filter(id=id)
        if not photo.exists():
            return Response({
                'error': 'not found photo with this id'
            })
        photo = photo.first()
        data = request.data
        serializer = PhotoUpdateSerializer(data=data,
                                           instance=photo)
        serializer.is_valid(raise_exception=True)
        photo = serializer.save()
        return Response(PhotoUpdateSerializer(photo).data)


class CommentListView(APIView):
    def get(self, request):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = CommentSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        comment = serializer.save()
        return Response(CommentSerializer(comment).data)


class CommentUpdateView(APIView):
    def patch(self, request, id):
        comment = Comment.objects.filter(id=id)
        if not comment.exists():
            return Response({
                'error': 'not found Comment with this id'
            })
        comment = comment.first()
        data = request.data
        serializer = CommentUpdateSerializer(data=data,
                                             instance=comment)
        serializer.is_valid(raise_exception=True)
        comment = serializer.save()
        return Response(CommentSerializer(comment).data)


class Info(APIView):
    def get(self, request):
        return Response({"name": "Петя", "last_name": "Иванов",
                         "age": 20})


class Random(APIView):
    def get(self, request):
        rand = random.randint(1, 100)
        return Response({"number": rand})
