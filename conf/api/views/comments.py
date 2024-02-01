from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from api.serializers.comments import CommentSerializer, CommentUpdateSerializer
from blog.models import Comment


class CommentListCreateView(APIView):
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


class CommentDetailUpdateDeleteView(APIView):
    def get(self, request, id):
        comment = Comment.objects.filter(id=id)
        comment = comment.first()
        if not comment:
            return Response({
                'error': 'not found comment with this id'
            })
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

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

    def delete(self, request, id):
        photo = get_object_or_404(Comment, id=id)
        photo.delete()
        return Response(status=204)
