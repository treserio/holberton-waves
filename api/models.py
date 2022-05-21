# Create your models here.
from django.db import models
from datetime import date

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


class Videos(models.Model):
    #topic = q string it was searched with, "Ocean Waves", "Meditation Sounds", ""
    topic = models.TextField(null=True)
    #updated = date.today()
    updated = models.DateField(null=True)
    #videoId = item.id.videoId
    videoId = models.CharField(max_length=20, null=True)
    #thumb_url = item.snippet.thumbnails.medium.url
    thumbnail = models.URLField(null=True)
    #title = item.snippet.title
    title = models.CharField(max_length=200, null=True)
    #subtitle = item.snippet.description
    description = models.TextField(null=True)
    #author = item.snippet.channelTitle
    author = models.CharField(max_length=200, null=True)
    #published = item.snippet.publishTime eg: "2021-10-18T01:00:09Z"
    published = models.CharField(max_length=23, null=True)

    # ========== video search values, item.id.videoId ==========
    #duration = item.contentDetails.duration eg: "PT54M34S"
    duration = models.DurationField(null=True)
    #likes = video search res.items[0].statistics.likeCount
    likes = models.IntegerField(null=True)
    #views = video search res.items[0].statistics.viewCount
    views = models.BigIntegerField(null=True)

    # ========== channel search values, item.snippet.channelId ==========
    #author_pic_url =
    author_pic_url = models.URLField(null=True)
