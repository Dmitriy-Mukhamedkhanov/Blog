from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

from api.serializers.likes import (LikeListCreateSerializer, LikeCreateSerializer, LikeUpdateSerializer,
                                   LikeDeleteSerializer)
from blog.models import Likes, Photo


class LikeCreateUpdateView(APIView):
    def get(self, request, id):
        photo = Photo.objects.filter(id=id)
        if not photo.exists():
            return Response({
                'error': 'no photo found with this ID'
            })
        photo = photo.first()
        like = Likes.objects.filter(pos=photo, boolean_value=True)
        if not like.exists():
            return Response({
                'error': 'this photo has not likes'
            })
        serializer = LikeListCreateSerializer(like, many=True)
        return Response(serializer.data)

    def post(self, request, id):
        photo = Photo.objects.filter(id=id)
        if not photo.exists():
            return Response({
                'error': 'no photo found with this ID'
            })
        user = User.oblects.filter(id=request.POST.get('user'))

        like = Likes.objects.filter(pos=id, user=request.POST['user'])
        if like.exists():
            return Response({
                'error': 'like already exists'
            })

        data = request.data
        serializer = LikeCreateSerializer(data=data, context={'id': id})
        serializer.is_valid(raise_exception=True)
        likes = serializer.save()
        return Response(LikeListCreateSerializer(likes).data)

    def patch(self, request, id):
        photo = Photo.objects.filter(id=id)
        if not photo.exists():
            return Response({
                'error': 'no photo found with this ID'
            })
        like = Likes.objects.filter(pos=id, user=request.POST['user'])
        if not like.exists():
            return Response({
                'error': 'no such like'
            })
        like = like.first()
        data = request.data
        serializer = LikeUpdateSerializer(data=data,
                                          instance=like)
        serializer.is_valid(raise_exception=True)
        like = serializer.save()
        return Response(LikeUpdateSerializer(like).data)

    def delete(self, request, id):
        photo = Photo.objects.filter(id=id)
        if not photo.exists():
            return Response({
                'error': 'no photo found with this ID'
            })
        like = Likes.objects.filter(pos=id, user=request.POST['user'])
        id_like = like.first().id
        if not like.exists():
            return Response({
                'error': 'no such like'
            })
        data = request.data
        serializer = LikeDeleteSerializer(data=data,
                                          instance=like.first())
        serializer.is_valid(raise_exception=True)
        like = serializer.save()
        like = get_object_or_404(Likes, id=id_like)
        like.delete()
        return Response(status=204)
