from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from api.serializers.comments import CommentForPhotoSerializer
from blog.models import Photo


class PhotoListCreateSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Photo
        fields = (
            'name',
            'description',
            'image',
            'author',
        )

    def get_author(self, obj):
        author = obj.author.username
        return author

    def create(self, validated_data):
        photo = Photo.objects.create(
            name=validated_data['name'],
            description=validated_data['description'],
            image=validated_data['image'],
            author_id=validated_data['author_id'].id,
        )
        return photo

    def validate(self, attrs):
        if self.context['author_id'].id is None:
            raise ValidationError('you are not registred')
        attrs['author_id'] = self.context['author_id']
        return attrs


class PhotoUpdateSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=False)
    description = serializers.CharField(required=False)
    image = serializers.ImageField(required=False)

    class Meta:
        model = Photo
        fields = (
            'name',
            'description',
            'image',
        )

    def update(self, instance, validated_data):
        if validated_data.get('name'):
            instance.name = validated_data['name']
        if validated_data.get('description'):
            instance.description = validated_data['description']
        if validated_data.get('image'):
            instance.image = validated_data['image']
        instance.save()
        return instance


class PhotoInfoSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    text_comment = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()

    class Meta:
        model = Photo

        fields = (
            'likes_count',
            'name',
            'description',
            'image',
            'author',
            'text_comment',
        )

    def get_author(self, obj):
        author = obj.author.username
        return author

    def get_text_comment(self, obj):
        text_comment = obj.comment_photo.all()
        serializer = CommentForPhotoSerializer(text_comment, many=True)
        return serializer.data

    def get_likes_count(self, obj):
        likes_count = obj.likes_set.all().count()
        return likes_count
