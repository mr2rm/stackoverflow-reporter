import requests
import webbrowser
import time

import settings


reported_questions = set()
access_token = None


def question_filter(question):
    return not question['is_answered'] and question['question_id'] not in reported_questions


def get_access_token():
    redirect_url = 'https%3a%2f%2fapi.stackexchange.com%2fdocs%2foauth_landing'
    url = f'{settings.ACCESS_TOKEN_API}?client_id=1&key={settings.KEY}&redirect_uri={redirect_url}'
    webbrowser.get('firefox').open(url)


def get_my_unanswered_questions():
    response = requests.get(url=settings.MY_UNANSWERED_API, params={
        **settings.REQUEST_PARAMETERS,
        'key': settings.KEY,
        'access_token': access_token
    }).json()

    question_list = list(filter(question_filter, response['items']))
    return question_list


def get_questions():
    parameters = {**settings.REQUEST_PARAMETERS}
    question_list = []

    for tag in settings.TAG_LIST:
        parameters.update({'tagged': tag})
        response = requests.get(
            url=settings.QUESTIONS_API,
            params=parameters
        ).json()

        questions = filter(question_filter, response['items'])
        selected_questions = map(lambda q: q['question_id'], question_list)
        questions = filter(
            lambda q: q['question_id'] not in selected_questions, questions
        )
        question_list.extend(questions)

    return question_list


if __name__ == "__main__":
    get_access_token()
    access_token = input("Enter the access token ('access_token' in URL): ")

    while True:
        # question_list = get_questions()
        question_list = get_my_unanswered_questions()

        question_list.sort(key=lambda q: (-q['score'], q['view_count']))
        for question in question_list[:5]:
            reported_questions.add(question['question_id'])
            webbrowser.get('firefox').open(question['link'], autoraise=False)

        if settings.MODE == 'auto':
            time.sleep(settings.REFRESH_TIME)
        else:
            input("Press Enter to continue...")
