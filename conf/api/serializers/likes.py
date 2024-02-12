from rest_framework import serializers
from rest_framework.response import Response

from blog.models import Likes, Photo


class LikeListCreateSerializer(serializers.ModelSerializer):
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




class LikeCreateSerializer(serializers.ModelSerializer):

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
            user_id=validated_data['user'].id
        )
        return like

    # def validate(self, attrs):
        # user = attrs['user'].id
        # id = self.context['id']
        # photo = Photo.objects.filter(id=id)
        # if not photo.exists():
        #     return Response({
        #         'error': 'no photo found with this ID'
        #     })
        # like = Likes.objects.filter(pos=id, user=user)
        # if like.exists():
        #     return Response({
        #         'error': 'like already exists'
        #     })
        # return attrs


class LikeUpdateSerializer(serializers.ModelSerializer):
    pos = serializers.SerializerMethodField(read_only=True)

    def get_pos(self, obj):
        pos = obj.pos_id
        return pos
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

class LikeDeleteSerializer(serializers.ModelSerializer):
    pos = serializers.SerializerMethodField(read_only=True)

    def get_pos(self, obj):
        pos = obj.pos_id
        return pos
    class Meta:
        model = Likes
        fields = (
            'boolean_value',
            'pos',
            'user',
        )
