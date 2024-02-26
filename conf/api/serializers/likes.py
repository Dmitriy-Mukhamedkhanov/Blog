from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from blog.models import Likes, Photo


class LikeListSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField(read_only=True)
    pos = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Likes
        fields = (
            'boolean_value',
            'pos',
            'user'
        )

    def get_user(self, obj):
        user = obj.user.username
        return user

    def get_pos(self, obj):
        pos = obj.pos_id
        return pos


class LikeCreateUpdateSerializer(serializers.ModelSerializer):
    pos = serializers.IntegerField(required=False)
    boolean_value = serializers.BooleanField(required=True)

    class Meta:
        model = Likes
        fields = (
            'boolean_value',
            'pos'
        )

    def create(self, validated_data):
        like = Likes.objects.create(
            boolean_value=validated_data['boolean_value'],
            pos_id=self.context['id'],
            user_id=self.context['author_id'].id
        )
        return like

    def update(self, instance, validated_data):
        instance.boolean_value = validated_data['boolean_value']
        instance.save()
        return instance

    def validate(self, attrs):
        if self.context['method'] == 'POST':
            user_id = self.context['author_id']
            photo_id = self.context['id']
            photo = Photo.objects.filter(id=photo_id)
            if not photo.exists():
                raise ValidationError({
                    'error': 'no photo found with this ID'
                })
            like = Likes.objects.filter(pos=photo_id, user=user_id)
            if like.exists():
                raise ValidationError({
                    'error': 'like already exists'
                })
        return attrs
