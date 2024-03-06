from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView

from api.permissions import IsAuthorObject
from api.serializers.comments import CommentSerializer, CommentUpdateSerializer
from blog.models import Comment


class CommentListCreateView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self, request):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = CommentSerializer(data=data, context={'author_id': request.user})
        serializer.is_valid(raise_exception=True)
        comment = serializer.save()
        return Response(CommentSerializer(comment).data)


class CommentDetailUpdateDeleteView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorObject]
    def get(self, request, id):
        comment = get_object_or_404(Comment, id=id)
        self.check_object_permissions(request, comment.author_comment)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    def patch(self, request, id):
        comment = get_object_or_404(Comment, id=id)
        self.check_object_permissions(request, comment.author_comment)
        data = request.data
        serializer = CommentUpdateSerializer(data=data,
                                             instance=comment)
        serializer.is_valid(raise_exception=True)
        comment = serializer.save()
        return Response(CommentSerializer(comment).data)

    def delete(self, request, id):
        comment = get_object_or_404(Comment, id=id)
        self.check_object_permissions(request, comment.author_comment)
        comment.delete()
        return Response(status=204)
