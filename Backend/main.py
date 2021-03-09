from flask import Flask
from src.question import question
from src.highscore import highscore

app = Flask(__name__)
app.register_blueprint(question)
app.register_blueprint(highscore)


def return_cors_response(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response
