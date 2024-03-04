from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from api.serializers.posts import PhotoListCreateSerializer, PhotoInfoSerializer, PhotoUpdateSerializer
from blog.models import Photo


class PhotoListCreateView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self, request):
        photos = Photo.objects.all()
        serializer = PhotoListCreateSerializer(photos, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = PhotoListCreateSerializer(data=data, context={'author_id': request.user})
        serializer.is_valid(raise_exception=True)
        photo = serializer.save()
        return Response(PhotoListCreateSerializer(photo).data)


class PhotoDetailUpdateDeleteView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self, request, id):
        photo = get_object_or_404(Photo, id=id)
        serializer = PhotoInfoSerializer(photo)
        return Response(serializer.data)

    def patch(self, request, id):
        photo = get_object_or_404(Photo, id=id)
        if photo.author != request.user:
            return Response({
                'error': 'this user not found'
            }, status=403)
        data = request.data
        serializer = PhotoUpdateSerializer(data=data,
                                           instance=photo)
        serializer.is_valid(raise_exception=True)
        photo = serializer.save()
        return Response(PhotoUpdateSerializer(photo).data)

    def delete(self, request, id):
        photo = get_object_or_404(Photo, id=id)
        if photo.author != request.user:
            return Response({
                'error': 'this user not found'
            }, status=403)
        photo.delete()
        return Response(status=204)
