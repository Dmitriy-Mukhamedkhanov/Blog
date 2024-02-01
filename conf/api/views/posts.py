from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from api.serializers.posts import PhotoListCreateSerializer, PhotoInfoSerializer, PhotoUpdateSerializer
from blog.models import Photo


class PhotoListCreateView(APIView):
    def get(self, request):
        photos = Photo.objects.all()
        serializer = PhotoListCreateSerializer(photos, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = PhotoListCreateSerializer(data=data, context={'author_id': data.get('author_id')})
        serializer.is_valid(raise_exception=True)
        photo = serializer.save()
        return Response(PhotoListCreateSerializer(photo).data)


class PhotoDetailUpdateDeleteView(APIView):
    def get(self, request, id):
        photo = Photo.objects.filter(id=id)
        photo = photo.first()
        if not photo:
            return Response({
                'error': 'not found photo with this id'
            })
        serializer = PhotoInfoSerializer(photo)
        return Response(serializer.data)

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

    def delete(self, request, id):
        photo = get_object_or_404(Photo, id=id)
        photo.delete()
        return Response(status=204)
