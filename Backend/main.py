from flask import Flask, abort, jsonify, request
from random import randrange
from data.data import db, is_valid_question

app = Flask(__name__)


@app.route('/api/question/', methods=["GET"])
def api_get_random_question():
    try:
        response = jsonify(db[randrange(len(db) - 1)])
        response.headers.add("Access-Control-Allow-Origin", "*")
        return response
    except IndexError:
        abort(404)


@app.route('/api/question/<int:index>/', methods=["GET", "POST", "DELETE"])
def api_specific_question(index):
    try:
        response = jsonify({})
        if request.method == "GET":
            response = jsonify(db[index])
            return response
        elif request.method == "POST":
            incoming_question = request.get_json()
            is_valid = is_valid_question(incoming_question)
            if is_valid["return_value"]:
                db[index] = incoming_question
                response = jsonify(incoming_question)
            else:
                abort(400, {'message': is_valid["errors"]})
        elif request.method == "DELETE":
            response = jsonify(db[index])
            del db[index]
        response.headers.add("Access-Control-Allow-Origin", "*")
        return response
    except IndexError:
        abort(404)


@app.route('/api/question_new/', methods=["POST"])
def api_new_question():
    incoming_question = request.get_json()
    is_valid = is_valid_question(incoming_question)
    if is_valid["return_value"]:
        db.append(incoming_question)
        response = jsonify(incoming_question)
        response.headers.add("Access-Control-Allow-Origin", "*")
        return response
    else:
        abort(400, {'message': is_valid["errors"]})


@app.route('/api/question_total/', methods=["GET"])
def api_get_question_total():
    return jsonify({'total': len(db)})
