from rest_framework import serializers

class PhotoSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=150)
    description = serializers.CharField()
    published = serializers.DateField(read_only=True)
    image = serializers.ImageField()
    author = serializers.CharField()

class CommentSerializer(serializers.Serializer):
    published_comment = serializers.DateField(read_only=True)
    text_comment = serializers.CharField()
    author_comment = serializers.CharField()
    image_comment = serializers.CharField()
