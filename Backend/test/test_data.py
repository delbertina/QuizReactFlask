from data.data import is_valid_question

test_data_1 = {
    "question": "What is 0 + 1 ?",
    "correctId": 0,
    "answers": ["1", "2", "3", "0"]
}
test_data_2 = {
    "question": "What is 0 + 1 ?",
    "correctId": -1,
    "answers": ["1", "2", "3", "0"]
}


def test_is_valid_question():
    test_result_1 = is_valid_question(test_data_1)
    assert test_result_1["errors"] == ""
    text_result_2 = is_valid_question(test_data_2)
    assert text_result_2["errors"] != ""
