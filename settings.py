# General Settings
REFRESH_TIME = 5 * 60

try:
    from local_settings import *
except ImportError:
    pass
