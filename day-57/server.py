from flask import Flask, render_template
import random
from datetime import date

app = Flask(__name__)

@app.route("/")
def hello():
    num = random.randint(1, 10)
    today_date = date.today()
    year = today_date.year
    # MAKE SURE THE HTML FILE IS UNDER "TEMPLATES" DIRECTORY
    return render_template("index.html", num=num, year=year)

if __name__ == "__main__":
    app.run(debug=True)
