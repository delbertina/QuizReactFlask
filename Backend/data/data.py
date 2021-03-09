import json


def load_flashcards_db():
    with open("data/flashcards_db.json") as f:
        return json.load(f)


def save_flashcards_db():
    with open("data/flashcards_db.json", "w") as f:
        return json.dump(flashcards_db, f)


def load_highscores_db():
    with open("data/highscores_db.json") as f:
        return json.load(f)


def save_highscores_db():
    with open("data/highscores_db.json", "w") as f:
        return json.dump(highscores_db, f)


def is_valid_question(input_question):
    print(input_question)
    errors = ""
    if input_question is None:
        errors += "Question object is null! "
    else:
        if input_question.get("question") is None\
                or input_question["question"] == ""\
                or not isinstance(input_question["question"], str):
            errors += "Question text is invalid! "
        if input_question.get("correctId") is None\
                or not isinstance(input_question["correctId"], int)\
                or input_question["correctId"] < 0\
                or input_question["correctId"] > 3:
            errors += "Question correctId is invalid! "
        if input_question.get("answers") is None\
                or input_question["answers"] is None \
                or len(input_question["answers"]) != 4\
                or input_question["answers"][0] is None or input_question["answers"][0] == ""\
                or input_question["answers"][1] is None or input_question["answers"][1] == ""\
                or input_question["answers"][2] is None or input_question["answers"][2] == ""\
                or input_question["answers"][3] is None or input_question["answers"][3] == "":
            errors += "Question answer array is invalid! "

    return {"return_value": (errors == ""), "errors": errors}


flashcards_db = load_flashcards_db()
highscores_db = load_highscores_db()
