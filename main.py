import requests
import webbrowser
import time

from settings import REFRESH_TIME, REQUEST_PARAMETERS, TAG_LIST, KEY, ACCESS_TOKEN


reported_questions = set()


def question_filter(question):
    return not question['is_answered'] and question['question_id'] not in reported_questions


def get_my_unanswered_questions():
    url = 'https://api.stackexchange.com/2.2/questions/unanswered/my-tags'
    parameters = {
        **REQUEST_PARAMETERS,
        'key': KEY,
        'access_token': ACCESS_TOKEN
    }

    while True:
        response = requests.get(url=url, params=parameters).json()
        questions = filter(question_filter, response['items'])

        sorted_questions = sorted(
            questions, key=lambda q: (-q['score'], q['view_count']))
        for question in sorted_questions[:5]:
            reported_questions.add(question['question_id'])
            webbrowser.open(question['link'])

        time.sleep(REFRESH_TIME)


def get_questions():
    url = 'https://api.stackexchange.com/2.2/questions'
    parameters = {**REQUEST_PARAMETERS}

    while True:
        question_list = []

        for tag in TAG_LIST:
            parameters.update({'tagged': tag})
            response = requests.get(url=url, params=parameters).json()

            questions = filter(question_filter, response['items'])
            selected_questions = map(lambda q: q['question_id'], question_list)
            questions = filter(
                lambda q: q['question_id'] not in selected_questions, questions
            )
            question_list.extend(questions)

        question_list.sort(key=lambda q: (-q['score'], q['view_count']))
        for question in question_list[:7]:
            reported_questions.add(question['question_id'])
            webbrowser.open(question['link'])

        time.sleep(REFRESH_TIME)


if __name__ == "__main__":
    # get_questions()
    get_my_unanswered_questions()
