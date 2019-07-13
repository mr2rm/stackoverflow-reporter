# Authentication
# Get KEY from https://api.stackexchange.com/docs/unanswered-questions-my-tags
KEY = 'U4DMV*8nvpm3EOpvf69Rxw(('

# General Settings
MODE = 'auto'
REFRESH_TIME = 5 * 60
# Need for QUESTIONS_API
TAG_LIST = []

# Request Configuration
REQUEST_PARAMETERS = {
    'site': 'stackoverflow',
    'order': 'desc',
    'sort': 'creation'
}

# APIs
MY_UNANSWERED_API = 'https://api.stackexchange.com/2.2/questions/unanswered/my-tags'
QUESTIONS_API = 'https://api.stackexchange.com/2.2/questions'

try:
    from local_settings import *
except ImportError:
    pass
