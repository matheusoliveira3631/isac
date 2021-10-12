import json, requests
def Search(query):
    key='AIzaSyAqEhsZ-FG_vFiUWhGW5Tz6GOmFHUkGI5M'
    qstr='+'.join(query.split(' '))
    req=json.loads(requests.get(f'https://www.googleapis.com/youtube/v3/search?part=snippet&q={qstr}&type=video&key={key}').content.decode('utf-8'))
    data=req['items'][0]
    videoId=data['id']['videoId']
    url=f'https://www.youtube.com/watch?v={videoId}&autoplay=1'
    return url
