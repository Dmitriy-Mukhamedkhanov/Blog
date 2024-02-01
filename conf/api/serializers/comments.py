from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from blog.models import Comment


class CommentForPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            'text_comment',
            'author_comment',
        )


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            'published_comment',
            'text_comment',
            'author_comment',
            'image_comment',
        )

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


class CommentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            'text_comment',
        )

    def update(self, instance, validated_data):
        if validated_data['text_comment']:
            instance.text_comment = validated_data['text_comment']
        instance.save()
        return instance
