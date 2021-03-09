from flask import abort, jsonify, request, Blueprint
from random import randrange
from data.data import flashcards_db, is_valid_question
from main import return_cors_response

question = Blueprint('question', __name__)


@question.route('/api/question/', methods=["GET"])
def api_get_random_question():
    try:
        response = jsonify(flashcards_db[randrange(len(flashcards_db) - 1)])
        return return_cors_response(response)
    except IndexError:
        abort(404)


@question.route('/api/question/<int:index>/', methods=["GET", "POST", "DELETE"])
def api_specific_question(index):
    try:
        response = jsonify({})
        if request.method == "GET":
            response = jsonify(flashcards_db[index])
        elif request.method == "POST":
            incoming_question = request.get_json()
            is_valid = is_valid_question(incoming_question)
            if is_valid["return_value"]:
                flashcards_db[index] = incoming_question
                response = jsonify(incoming_question)
            else:
                abort(400, {'message': is_valid["errors"]})
        elif request.method == "DELETE":
            response = jsonify(flashcards_db[index])
            del flashcards_db[index]
        return return_cors_response(response)
    except IndexError:
        abort(404)


@question.route('/api/question_new/', methods=["POST"])
def api_new_question():
    incoming_question = request.get_json()
    is_valid = is_valid_question(incoming_question)
    if is_valid["return_value"]:
        flashcards_db.append(incoming_question)
        response = jsonify(incoming_question)
        return return_cors_response(response)
    else:
        abort(400, {'message': is_valid["errors"]})


@question.route('/api/question_total/', methods=["GET"])
def api_get_question_total():
    response = jsonify({'total': len(flashcards_db)})
    return return_cors_response(response)


@question.route('/api/question_all/', methods=["GET"])
def api_get_question_all():
    return return_cors_response(jsonify(flashcards_db))
