import os
import json
import tweepy

if __name__ == "__main__":
    current_path=os.getcwd()
    path="\\".join(current_path.split('\\')[:-1])
    os.chdir(path)
    
#setup
with open('src/keys.json') as file:
    keys=json.loads(file.readlines()[0])
    auth = tweepy.OAuthHandler(keys['api_key'], keys['api_secret'])
    auth.set_access_token(keys['access_token'], keys['access_secret'])
    twapi = tweepy.API(auth)

def slash(string):
    return '//'.join(string.split("\\"))
#===============================><========================#
def tweet(text, *img_path):
    if img_path:
        print(f'media: {img_path[0]}')
        media=twapi.media_upload(img_path[0])
        twapi.update_status(text, media_ids=[media.media_id])
    else:
        twapi.update_status(text)

def dm(user, text, *img_path):
    user_id=twapi.search_users(f'@{user}', count=1)[0]._json['id']
    if img_path:
        print(f'media: {img_path[0]}')
        media=twapi.media_upload(img_path[0])
        twapi.send_direct_message(user_id, text, attachment_type='media' ,attachment_media_id=media.media_id)
    else:
        twapi.send_direct_message(user_id, text)

    


        