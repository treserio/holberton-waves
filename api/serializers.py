from rest_framework import serializers
from .models import Videos

class VideosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Videos
        fields = [
            'id',
            'topic',
            'updated',
            'videoId',
            'thumbnail',
            'title',
            'description',
            'author',
            'published',
            'duration',
            'likes',
            'views',
            'author_pic_url',
        ]
