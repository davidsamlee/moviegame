from flask import Flask, redirect
from questions import questionAndAnswers
from moviedata import getRandomMovies
from util import ApiError
import jsonify

app = Flask('app', static_url_path='', static_folder='static')

@app.route('/')
def root_page():
    return redirect("index.html", code=302)


# Returns a JSON object with a question and some answers
@app.route('/question')
def movie_list():
    return questionAndAnswers()


# Returns a random movie (for testing purposes)
@app.route('/random')
def random():
    return getRandomMovies(1)[0]


@app.errorhandler(ApiError)
def handle_error(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

app.run(host='0.0.0.0', port=8080)
