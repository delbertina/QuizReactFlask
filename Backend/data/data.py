import json


def load_db():
    with open("data/flashcards_db.json") as f:
        return json.load(f)


def save_db():
    with open("data/flashcards_db.json", "w") as f:
        return json.dump(db, f)


def is_valid_question(input_question):
    print(input_question)
    errors = ""
    if input_question is None:
        errors += "Question object is null! "
    if input_question["question"] is None \
            or not isinstance(input_question["question"], str):
        errors += "Question text is invalid! "
    if input_question["correctId"] is None \
            or not isinstance(input_question["correctId"], int)\
            or input_question["correctId"] < 0\
            or input_question["correctId"] > 3:
        errors += "Question correctId is invalid! "
    if input_question["answers"] is None \
            or len(input_question["answers"]) != 4\
            or input_question["answers"][0] is None or input_question["answers"][0] == ""\
            or input_question["answers"][1] is None or input_question["answers"][1] == ""\
            or input_question["answers"][2] is None or input_question["answers"][2] == ""\
            or input_question["answers"][3] is None or input_question["answers"][3] == "":
        errors += "Question answer array is invalid! "

    return {"return_value": (errors == ""), "errors": errors}


db = load_db()
