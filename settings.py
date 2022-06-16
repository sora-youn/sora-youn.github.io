import os
from os import environ

SESSION_CONFIGS = [
    dict(
        name='CFXd',
        display_name="CFXd",
        num_demo_participants=4,
        app_sequence=['dRiskAmb', 'eExitSurvey'],
        simple = False,
        identifiable = False,
    ),   
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=0.02, participation_fee=10.00, doc=""
)

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ROOMS = [
    # dict(
    #     name='econ101',
    #     display_name='Econ 101 class',
    #     participant_label_file='_rooms/econ101.txt',
    # ),
    # dict(name='live_demo', display_name='Room for live demo (no participant labels)'),
    dict(
        name='ERL_Online_Experiment',
        display_name='ERL',
        participant_label_file='_rooms/participant_labels.txt',
    ),
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
Here are some oTree games.
"""


SECRET_KEY = '1o3dc8s=s^$7mexh1hf21=uulkm_t%8mbjlm*%)6(deg%xjtdd'

INSTALLED_APPS = ['otree', 'django.contrib.staticfiles']

STATIC_URL = '/static/'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
