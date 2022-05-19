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
    #author_pic_url =4
    author_pic_url = models.URLField(null=True)


import requests
import datetime

q_topics = ['Ocean Waves',
            'Mindfulness',
            'Meditative Sound Waves']

def convertDuration(pt_Str):
    pt_Str = pt_Str[2:]
    if 'H' in pt_Str:
        h = pt_Str[:pt_Str.index('H')]
        pt_Str = pt_Str[pt_Str.index('H') + 1:]
    else:
        h = '00'
    if 'M' in pt_Str:
        m = pt_Str[:pt_Str.index('M')]
        pt_Str = pt_Str[pt_Str.index('M') + 1:]
    else:
        m = '00'
    if 'S' in pt_Str:
        s = pt_Str[:pt_Str.index('S')]
    else:
        s = '00'

    return datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))

def init_Vids(q_topics):
    youtube_url = 'https://www.googleapis.com/youtube/v3/'
    # search_url = youtube_url +  'search?'
    # video_url = youtube_url + 'videos?'
    # channel_url = youtube_url + 'channels?'
    api_key = '&key=AIzaSyALk_NgfR9gUn-sTC2ZquYBuxn1H3ryaK0'
    part = '&part=snippet'
    video_parts = '&part=contentDetails,statistics'
    max = '&maxResults=10'
    fields = '&fields=items/snippet/thumbnails/default/url'

    item_list = []
    for topic in q_topics:
        print(topic)
        # print("".join([youtube_url, 'search?', api_key, part, max, f'&q="{topic}"']))
        data = requests.get("".join([youtube_url, 'search?', api_key, part, max, f'&q="{topic}"'])).json()
        for item in data['items']:
            newObj = {}
            newObj['topic'] = topic
            newObj['updated'] = datetime.date.today()
            newObj['thumbnail'] = item['snippet']['thumbnails']['medium']['url']
            # Incorrect string value: '\\xF0\\x9F\\x8E\\xA7Me...
            newObj['title'] = item['snippet']['title'].encode('ascii', 'ignore').decode('ascii')
            newObj['description'] = item['snippet']['description']
            newObj['author'] = item['snippet']['channelTitle']
            newObj['published'] = item['snippet']['publishTime']
            # grab the video url info for the item to get additional info
            data2 = requests.get("".join([youtube_url, 'videos?', api_key, video_parts, f"&id={item['id']['videoId']}"])).json()
            newObj['duration'] = convertDuration(data2['items'][0]['contentDetails']['duration'])
            if 'likeCount' in data2['items'][0]['statistics']:
                newObj['likes'] = data2['items'][0]['statistics']['likeCount']
            else:
                newObj['likes'] = 0
            newObj['views'] = data2['items'][0]['statistics']['viewCount']
            # grab the channel icon from the channel search
            data3 = requests.get("".join([youtube_url, 'channels?', api_key, part, fields, f"&id={item['snippet']['channelId']}"])).json()
            newObj['author_pic_url'] = data3['items'][0]['snippet']['thumbnails']['default']['url']
            item_list.append(newObj)

    # why is this 10 and not 30
    print(len(item_list))
    # start initializing objects to store in db
    for item in item_list:
        newVid = Videos(**item)
        newVid.save()

#####################

init_Vids(q_topics)
