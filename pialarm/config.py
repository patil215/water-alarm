import os
basedir = os.path.abspath(os.path.dirname(__file__))

# -- Alarm Settings
PIN = 10                       # Pin to which motor is connected
ALARM_DURATION = 1            # Motor duration in minutes

# -- General Config
DEBUG = True
CSRF_ENABLED = True
BASIC_AUTH_FORCE = False
BASIC_AUTH_USERNAME = 'alarm'
BASIC_AUTH_PASSWORD = 'password'

# -- Custom Happy Messages
MESSAGES = [
    "Wat"
]
