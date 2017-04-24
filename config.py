import os
basedir = os.path.abspath(os.path.dirname(__file__))

# -- Alarm Settings
PIN = 10                       # Pin to which motor is connected
ALARM_DURATION = 1            # Motor duration in minutes

# -- General Config
DEBUG = True
CSRF_ENABLED = True
BASIC_AUTH_FORCE = True
BASIC_AUTH_USERNAME = 'patil215'
BASIC_AUTH_PASSWORD = 'default'

# -- Custom Happy Messages
MESSAGES = [
    "Water alarm clock created by Neil Patil."
]

