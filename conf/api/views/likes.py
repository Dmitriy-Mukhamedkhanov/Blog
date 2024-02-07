from rest_framework.views import APIView
from rest_framework.response import Response

from api.serializers.likes import LikeListCreateSerializer, LikeCreateSerializer, LikeUpdateSerializer
from blog.models import Likes


class LikeCreateUpdateView(APIView):
    def get(self, request, id):
        like = Likes.objects.filter(pos=id)
        if not like.exists():
            return Response({
                'error': 'not found Photo with this id or this user'
            })

        serializer = LikeListCreateSerializer(like, many=True)

        return Response(serializer.data)

    def patch(self, request, id):
        like = Likes.objects.filter(pos=id, user=request.POST['user'])
        if not like.exists():
            return Response({
                'error': 'not found Photo with this id'
            })
        like = like.first()
        if request.POST['boolean_value'] == '':
            return Response({
                'error': 'enter value "boolean_value"'
            })
        data = request.data
        serializer = LikeUpdateSerializer(data=data,
                                          instance=like)
        serializer.is_valid(raise_exception=True)
        like = serializer.save()
        return Response(LikeUpdateSerializer(like).data)
class LikeAddView(APIView):

    def post(self, request, id):

        like = Likes.objects.filter(pos=id, user=request.POST['user'])
        if not like.exists():
            # Likes.objects.create(pos=id, user=request.POST['user'], boolean_value = True)
            return Response({
                'error': 'not found Photo with this id or this user'
            })


        data = request.data
        serializer = LikeCreateSerializer(data=data, context={'id': id})
        serializer.is_valid(raise_exception=True)
        likes = serializer.save()
        return Response(LikeListCreateSerializer(likes).data)


