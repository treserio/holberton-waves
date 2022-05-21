from django.shortcuts import render
from django.http import JsonResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView
from rest_framework.filters import OrderingFilter

from .models import Videos
from .serializers import VideosSerializer

class apiVideos(ListAPIView):
    queryset = Videos.objects.all()
    serializer_class = VideosSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = [
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
    ordering_fields = [
        'likes',
        'views',
        'published',
    ]
