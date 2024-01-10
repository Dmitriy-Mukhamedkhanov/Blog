from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from blog.models import User, Photo


class PhotoSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=150)
    description = serializers.CharField()
    published = serializers.DateField(read_only=True)
    image = serializers.ImageField()
    author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    def validate(self, attrs):
        if attrs['author'].username == 'Ivan':
            raise ValidationError('Иван не имеет право выкладывать фото')
        return attrs

    def validate_description(self, value):  # value - значение с описанием, description - ключ
        for word in value.split():
            if word[0] == 'a':
                raise ValidationError(f'Слово {word} не должно начинаться с буквы а')
        return value


class CommentSerializer(serializers.Serializer):
    published_comment = serializers.DateField(read_only=True)
    text_comment = serializers.CharField()
    author_comment = serializers.CharField()
    image_comment = serializers.PrimaryKeyRelatedField(queryset=Photo.objects.all())

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
