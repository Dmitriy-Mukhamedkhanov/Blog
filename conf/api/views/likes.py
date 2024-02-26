from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

from api.serializers.likes import (LikeListSerializer, LikeCreateUpdateSerializer)
from blog.models import Likes, Photo


class LikeListCreateUpdateDeleteView(APIView):
    def get(self, request, id):
        photo = get_object_or_404(Photo, id=id)
        like = Likes.objects.filter(pos=photo, boolean_value=True)
        if not like.exists():
            return Response({
                'error': 'this photo has not likes'
            })
        serializer = LikeListSerializer(like, many=True)
        return Response(serializer.data)

    def post(self, request, id):
        data = request.data
        serializer = LikeCreateUpdateSerializer(data=data,
                                                context={'id': id,
                                                         'method': request.method,
                                                         'author_id': request.user})
        serializer.is_valid(raise_exception=True)
        likes = serializer.save()
        return Response(LikeListSerializer(likes).data)

    def patch(self, request, id):
        data = request.data
        like = get_object_or_404(Likes, pos=id, user=request.user)
        serializer = LikeCreateUpdateSerializer(data=data, instance=like,
                                                context={'method': request.method})
        serializer.is_valid(raise_exception=True)
        like = serializer.save()
        return Response(LikeListSerializer(like).data)

    def delete(self, request, id):
        like = get_object_or_404(Likes, pos=id, user=request.user)
        like.delete()
        return Response(status=204)
