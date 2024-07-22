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
test_data_3 = {
    "question": "What is 0 + 1 ?",
    "correctId": 4,
    "answers": ["1", "2", "3", "0"]
}
test_data_4 = {
    "question": "What is 0 + 1 ?",
    "correctId": 0,
    "answers": ["1", "2", "3"]
}
test_data_5 = {
    "question": "What is 0 + 1 ?",
    "correctId": 0,
    "answers": ["1", "2", "3", "0", "4"]
}
test_data_6 = {
    "question": "",
    "correctId": 0,
    "answers": ["1", "2", "3", "0"]
}
test_data_7 = {
    "question": "What is 0 + 1 ?",
    "answers": ["1", "2", "3", "0"]
}
test_data_8 = {
    "correctId": 0,
    "answers": ["1", "2", "3", "0"]
}
test_data_9 = {
    "question": "What is 0 + 1 ?",
    "correctId": 0
}
test_data_10 = None


def test_is_valid_question():
    test_result_1 = is_valid_question(test_data_1)
    assert test_result_1["errors"] == ""
    text_result_2 = is_valid_question(test_data_2)
    assert text_result_2["errors"] != ""
    text_result_3 = is_valid_question(test_data_3)
    assert text_result_3["errors"] != ""
    text_result_4 = is_valid_question(test_data_4)
    assert text_result_4["errors"] != ""
    text_result_5 = is_valid_question(test_data_5)
    assert text_result_5["errors"] != ""
    text_result_6 = is_valid_question(test_data_6)
    assert text_result_6["errors"] != ""
    text_result_7 = is_valid_question(test_data_7)
    assert text_result_7["errors"] != ""
    text_result_8 = is_valid_question(test_data_8)
    assert text_result_8["errors"] != ""
    text_result_9 = is_valid_question(test_data_9)
    assert text_result_9["errors"] != ""
    text_result_10 = is_valid_question(test_data_10)
    assert text_result_10["errors"] != ""
