from django.contrib import admin

# Register your models here.
# ?part=snippet&key=AIzaSyALk_NgfR9gUn-sTC2ZquYBuxn1H3ryaK0&q=Sound&type=video&maxResults=20
# https://www.googleapis.com/youtube/v3/search?
# &key=AIzaSyALk_NgfR9gUn-sTC2ZquYBuxn1H3ryaK0
# &part=snippet
# &q=Sound%20Waves
# &type=video
# &maxResults=10

# fields too restrictive, probably do it without
# &fields=items(id/videoId,snippet/title,snippet/description,snippet/channelTitle)

# mayneed additional searches for various channel ids to collect image urls n such
