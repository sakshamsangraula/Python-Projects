from flask import Flask, request, render_template
import requests


app = Flask(__name__)

def guess_age(user_name):
    age_response = requests.get(url=f'https://api.agify.io?name={user_name}')
    age_json = age_response.json()
    age = age_json["age"]
    age = str(age)
    return age

def guess_gender(user_name):
    gender_response = requests.get(url=f'https://api.genderize.io?name={user_name}')
    gender_json = gender_response.json()
    print(gender_json)
    gender = gender_json["gender"]
    print(gender)
    # turn int to string
    gender = str(gender)
    print(gender)
    return gender

# USE XML LIKE BRACKETS TO GET THE INPUT
@app.route('/guess/<name>')
def print_guess(name):
    gender = guess_gender(name)
    year = guess_age(name)
    return render_template("index.html", name=name, gender=gender, year=year)
# #
if __name__ == "__main__":
    app.run(debug=True)

