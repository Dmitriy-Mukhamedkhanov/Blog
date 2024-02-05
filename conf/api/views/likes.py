from rest_framework.views import APIView
from rest_framework.response import Response

from api.serializers.likes import LikeListCreateSerializer, LikeCreateSerializer
from blog.models import Likes


class LikeCreateUpdateView(APIView):
    def get(self, request):
        like = Likes.objects.filter(pos_id=request.data['pos'])

        if not like.exists():
            return Response({
                'error': 'not found likes this photo'
            })

        serializer = LikeListCreateSerializer(like, many=True)

        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = LikeCreateSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        likes = serializer.save()
        return Response(LikeListCreateSerializer(likes).data)
