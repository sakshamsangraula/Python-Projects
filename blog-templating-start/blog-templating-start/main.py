from flask import Flask, render_template
import requests


app = Flask(__name__)

@app.route('/')
def home():
    all_posts = requests.get('https://api.npoint.io/5abcca6f4e39b4955965')
    all_posts = all_posts.json()
    return render_template("index.html", all_posts = all_posts)


if __name__ == "__main__":
    app.run(debug=True)
