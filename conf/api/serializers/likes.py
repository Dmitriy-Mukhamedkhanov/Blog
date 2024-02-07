from rest_framework import serializers
from rest_framework.response import Response

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
    pos = serializers.SerializerMethodField(read_only=True)

    def get_pos(self, obj):
        pos = self.context['id']
        return pos

    class Meta:
        model = Likes
        fields = (
            'boolean_value',
            'pos',
            'user'
        )

    def create(self, validated_data):
        like = Likes.objects.create(
            boolean_value=validated_data['boolean_value'],
            pos_id=self.context['id'],
            user_id=validated_data['user'].id,
        )
        return like


class LikeUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Likes
        fields = (
            'boolean_value',
            'pos',
            'user',
        )

    def update(self, instance, validated_data):
        A = instance.boolean_value
        B = validated_data['boolean_value']
        if validated_data['boolean_value'] != None:
            instance.boolean_value = validated_data['boolean_value']
        else:
            return Response({
                'error': 'enter boolean_value'
            })

        instance.save()
        return instance
