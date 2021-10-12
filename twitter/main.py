import os
import json
import tweepy

class Twitter:
    def __init__(self, keys):
        auth = tweepy.OAuthHandler(keys['api_key'], keys['api_secret'])
        auth.set_access_token(keys['access_token'], keys['access_secret'])
        self.api = tweepy.API(auth)

    def tweet(self, text, *img_path):
        if img_path:
            print(f'media: {img_path[0]}')
            media=self.api.media_upload(img_path[0])
            self.api.update_status(text, media_ids=[media.media_id])
        else:
            self.api.update_status(text)

    def dm(self, user, text, *img_path):
        user_id=self.api.search_users(f'@{user}', count=1)[0]._json['id']
        if img_path:
            print(f'media: {img_path[0]}')
            media=self.api.media_upload(img_path[0])
            self.api.send_direct_message(user_id, text, attachment_type='media' ,attachment_media_id=media.media_id)
        else:
            self.api.send_direct_message(user_id, text)

    


        