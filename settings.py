from os import environ
SESSION_CONFIG_DEFAULTS = dict(real_world_currency_per_point=0.1, participation_fee=5)
SESSION_CONFIGS = [dict(name='Quota', num_demo_participants=10, app_sequence=['quota'])]
LANGUAGE_CODE = 'de'
REAL_WORLD_CURRENCY_CODE = 'EUR'
USE_POINTS = False
DEMO_PAGE_INTRO_HTML = ''
PARTICIPANT_FIELDS = ['quota_full']
SESSION_FIELDS = ['num_participants_finished']
ROOMS = []

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

SECRET_KEY = 'blahblah'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']


