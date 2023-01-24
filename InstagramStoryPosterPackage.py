from instagrapi import Client
import config
import pyotp
import os

class instagram_story_poster_class:
    def instagram_story_poster():

        USERNAME = config.USERNAME
        PASSWORD = config.PASSWORD
        AUTH_KEY = config.AUTH_KEY
        IMAGE_PATH = os.path.abspath(r'todays_image.jpg')
        
        totp = pyotp.TOTP(AUTH_KEY)
        f2a_code = totp.now()
        print(f'F2A code is {f2a_code}')

        client = Client()
        print('Client instantiated')
        client.login(USERNAME, PASSWORD, verification_code=f2a_code)
        print('Successful login')
        client.photo_upload_to_story(
            IMAGE_PATH
        )
        print('Successful posted')

if __name__ == '__main__':
    instagram_story_poster_class.instagram_story_poster()