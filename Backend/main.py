from flask import Flask, abort, jsonify
from random import randrange
import json

app = Flask(__name__)


def load_db():
    with open("flashcards_db.json") as f:
        return json.load(f)


db = load_db()


@app.route('/api/random_question/', methods=["GET"])
def api_card_detail():
    try:
        response = jsonify(db[randrange(30)])
        response.headers.add("Access-Control-Allow-Origin", "*")
        return response
    except IndexError:
        abort(404)
