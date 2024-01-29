from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from blog.models import Photo, Comment


class PhotoSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()

    def get_author(self, obj):
        author = obj.author.username
        return author

    class Meta:
        model = Photo

        fields = (
            'name',
            'description',
            'image',
            'author',
        )

    def create(self, validated_data):
        photo = Photo.objects.create(
            name=validated_data['name'],
            description=validated_data['description'],
            image=validated_data['image'],
            author=validated_data['author'],
        )
        return photo

    def validate(self, attrs):
        if attrs['author'].username == 'Ivan':
            raise ValidationError('Иван не имеет право выкладывать фото')
        return attrs

    def validate_description(self, value):  # value - значение с описанием, description - ключ
        for word in value.split():
            if word[0] == 'a':
                raise ValidationError(f'Слово {word} не должно начинаться с буквы а')
        return value


class PhotoUpdateSerializer(serializers.Serializer):
    name = serializers.CharField()
    description = serializers.CharField(required=False)
    image = serializers.ImageField(required=False)

    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        if validated_data.get('description'):
            instance.description = validated_data['description']
        if validated_data.get('image'):
            instance.image = validated_data['image']
        instance.save()
        return instance


class PhotoInfoSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()

    def get_author(self, obj):
        author = obj.author.username
        return author

    text_comment = serializers.SerializerMethodField()

    def get_text_comment(self, obj):
        text_comment = obj.comment_photo.all()
        serializer = CommentForPhotoSerializer(text_comment, many=True)
        return serializer.data

    likes_count = serializers.SerializerMethodField()

    def get_likes_count(self, obj):
        likes_count = obj.likes_set.all().count()
        return likes_count
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
class CommentForPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            'text_comment',
            'author_comment',
        )


class CommentSerializer(serializers.Serializer):
    published_comment = serializers.DateField(read_only=True)
    text_comment = serializers.CharField()
    author_comment = serializers.CharField()
    image_comment = serializers.PrimaryKeyRelatedField(queryset=Photo.objects.all())

    def create(self, validated_data):
        comment = Comment.objects.create(
            text_comment=validated_data['text_comment'],
            author_comment=validated_data['author_comment'],
            image_comment=validated_data['image_comment'],
        )
        return comment

    def validate(self, attrs):
        if len(attrs['text_comment'].split()) > 20:
            raise ValidationError('Текст комментария должно быть менее 20 слов')
        if not attrs['image_comment'].name.isalpha():
            raise ValidationError('Фото нельзя комментировать, т.к. в названии имеется цифра')
        return attrs

    def validate_text_comment(self, value):
        ban_words = ['Дурак', 'ужас', 'удали быстро']
        for word in ban_words:
            if word.lower() in value.lower():
                raise ValidationError(f'Некорректный комментрий "{word.title()}" - недопустимое слово')
        return value


class CommentUpdateSerializer(serializers.Serializer):
    text_comment = serializers.CharField(required=False)

    def update(self, instance, validated_data):
        if validated_data['text_comment']:
            instance.text_comment = validated_data['text_comment']
        instance.save()
        return instance
