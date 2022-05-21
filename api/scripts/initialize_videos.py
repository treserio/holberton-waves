import requests
import datetime
from api.models import Videos

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
    # print('test', h, m, s)
    return datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))

def init_Vids(q_topics):
    youtube_url = 'https://www.googleapis.com/youtube/v3/'
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
            if item['snippet']['liveBroadcastContent'] != 'none':
                continue
            newObj = {}
            newObj['topic'] = topic
            newObj['updated'] = datetime.date.today()
            newObj['videoId'] = item['id']['videoId']
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

    print(len(item_list))
    # start initializing objects to store in db
    for item in item_list:
        newVid = Videos(**item)
        newVid.save()

#####################

init_Vids(q_topics)
