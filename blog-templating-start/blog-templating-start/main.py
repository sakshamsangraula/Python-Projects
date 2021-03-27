from flask import Flask, render_template
import requests


app = Flask(__name__)

@app.route('/')
def home():
    all_posts = requests.get('https://api.npoint.io/5abcca6f4e39b4955965')
    all_posts = all_posts.json()
    return render_template("index.html", posts=all_posts)

# route the read links to respective blog posts
@app.route('/post/<int:num>')
def blog_posts(num):
    all_posts = requests.get('https://api.npoint.io/5abcca6f4e39b4955965')
    all_posts = all_posts.json()
    for post in all_posts:
        if post['id'] == num:
            select_post = post
    return render_template("post.html", post=select_post)

if __name__ == "__main__":
    app.run(debug=True)
