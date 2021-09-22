from rest_framework import serializers
from ..models import Pikcha


class PikchaListSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    url = serializers.CharField()
    picture = serializers.CharField()
    width = serializers.IntegerField()
    height = serializers.IntegerField()
    parent_picture = serializers.IntegerField()

    class Meta:
        model = Pikcha
        fields = [
           'id', 'name', 'url', 'picture', 'width', 'height', 'parent_picture'
        ]


class PikchaDetailSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    url = serializers.CharField()
    picture = serializers.CharField()
    width = serializers.IntegerField()
    height = serializers.IntegerField()
    parent_picture = serializers.IntegerField()

    class Meta:
        model = Pikcha
        fields = [
            'id', 'name', 'url', 'picture', 'width', 'height', 'parent_picture'
        ]

