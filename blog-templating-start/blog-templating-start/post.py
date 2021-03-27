import requests

class Post:

    def __init__(self):
        self.all_posts = requests.get('https://api.npoint.io/5abcca6f4e39b4955965')
        self.all_posts = self.all_posts.json()

