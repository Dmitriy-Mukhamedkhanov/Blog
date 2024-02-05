from rest_framework import serializers

from blog.models import Likes


class LikeListCreateSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
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
class LikeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Likes
        fields = (
            'pos',
            'user'
        )
    def create(self, validated_data):
        like = Likes.objects.create(
            pos=validated_data['pos'],
            user=validated_data['user'],
        )
        return like