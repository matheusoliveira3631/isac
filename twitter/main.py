import tweepy, json
#setup
with open('src/keys.json') as file:
    keys=json.loads(file.readlines()[0])
    auth = tweepy.OAuthHandler(keys['api_key'], keys['api_secret'])
    auth.set_access_token(keys['access_token'], keys['access_secret'])
    ttapi = tweepy.API(auth)
#===============================><========================#
def tweet(text, *img_path):
    if img_path:
        print(f'media: {img_path[0]}')
        media=ttapi.media_upload(img_path[0])
        ttapi.update_status(text, media_ids=[media.media_id])
    else:
        ttapi.update_status(text)