# Refresh Time
REFRESH_TIME = 5 * 60

# Request Parameters
REQUEST_PARAMETERS = {}

# Favourite Tags
TAG_LIST = []

# Authentication
KEY = ''
ACCESS_TOKEN = ''

try:
    from local_settings import *
except ImportError:
    pass
