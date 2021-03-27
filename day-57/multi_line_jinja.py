from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def get_blog():
    url = 'https://api.npoint.io/5abcca6f4e39b4955965'
    all_posts = requests.get(url).json()
    return render_template("blog.html", blog_posts=all_posts)

@app.route("/blog/<num>")
def blog(num):
    print(num)
    return "<h1> Blog Here </h1>"

if __name__ == "__main__":
    app.run(debug=True)