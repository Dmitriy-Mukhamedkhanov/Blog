from rest_framework import serializers

from blog.models import User, Photo


class PhotoSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=150)
    description = serializers.CharField()
    published = serializers.DateField(read_only=True)
    image = serializers.ImageField()
    author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

class CommentSerializer(serializers.Serializer):
    published_comment = serializers.DateField(read_only=True)
    text_comment = serializers.CharField()
    author_comment = serializers.CharField()
    image_comment = serializers.PrimaryKeyRelatedField(queryset=Photo.objects.all())
