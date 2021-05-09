import os
from os import environ

SESSION_CONFIGS = [
    # dict(
    #     name='Part1',
    #     display_name="Part1",
    #     num_demo_participants=3,
    #     app_sequence=['Part1'],
    # ),
    # dict(
    #     name='Part2',
    #     display_name="Part2",
    #     num_demo_participants=3,
    #     app_sequence=['Part2'],
    # ),
    # dict(
    #     name='Part3_T1',
    #     display_name="Part3_T1",
    #     num_demo_participants=3,
    #     app_sequence=['Part3_T1'],
    # ),
    # dict(
    #     name='Part3_T2',
    #     display_name="Part3_T2",
    #     num_demo_participants=3,
    #     app_sequence=['Part3_T2'],
    # ),
    # dict(
    #     name='Part4',
    #     display_name="Part4",
    #     num_demo_participants=3,
    #     app_sequence=['Part4'],
    # ),
    # dict(
    #     name='Part5',
    #     display_name="Part5",
    #     num_demo_participants=3,
    #     app_sequence=['Part5'],
    # ),
    # dict(
    #     name='Part6',
    #     display_name="Part6",
    #     num_demo_participants=3,
    #     app_sequence=['Part6'],
    # ),
    # dict(
    #     name='Part7',
    #     display_name="Part7",
    #     num_demo_participants=3,
    #     app_sequence=['Part7'],
    # ),
    dict(
        name='Full_Sequence_T1',
        display_name="Full_Sequence_T1",
        num_demo_participants=3,
        app_sequence=['Part1', 'Part2','Part3_T1','Part4','Part5','Part6','Part7'],
    ),
    dict(
        name='Full_Sequence_T2',
        display_name="Full_Sequence_T2",
        num_demo_participants=3,
        app_sequence=['Part1', 'Part2','Part3_T2','Part4','Part5','Part6','Part7'],
    ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=0.1, participation_fee=5.00, doc=""
)

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ROOMS = [
    dict(
        name='econ101',
        display_name='Econ 101 class',
        participant_label_file='_rooms/econ101.txt',
    ),
    dict(name='live_demo', display_name='Room for live demo (no participant labels)'),
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
Here are some oTree games.
"""


SECRET_KEY = '1o3dc8s=s^$7mexh1hf21=uulkm_t%8mbjlm*%)6(deg%xjtdd'

INSTALLED_APPS = ['otree']
