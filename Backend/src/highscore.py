from flask import abort, jsonify, request, Blueprint
from data.data import highscores_db
from main import return_cors_response

highscore = Blueprint('highscore', __name__)


@highscore.route('/api/highscore/new/', methods=["POST"])
def api_add_new_highscore():
    incoming_highscore = request.get_json()
    highscores_db.append(incoming_highscore)
    return return_cors_response(jsonify(incoming_highscore))


@highscore.route('/api/highscore/reset/', methods=["DELETE"])
def api_reset_highscore():
    highscores_db.clear()
    return return_cors_response(jsonify(highscores_db))


@highscore.route('/api/highscore/total/', methods=["GET"])
def api_get_total_highscore():
    response = jsonify({"total": len(highscores_db)})
    return return_cors_response(response)


@highscore.route('/api/highscore/top/score/<int:count>/', methods=["GET"])
def api_get_top_highscores(count):
    try:
        response = jsonify(sorted(highscores_db, key=lambda i: i['score'], reverse=True)[:count])
        return return_cors_response(response)
    except IndexError:
        abort(404)


@highscore.route('/api/highscore/top/recent/<int:count>/', methods=["GET"])
def api_get_recent_highscores(count):
    try:
        response = jsonify(sorted(highscores_db, key=lambda i: i['timestamp'], reverse=True)[:count])
        return return_cors_response(response)
    except IndexError:
        abort(404)
