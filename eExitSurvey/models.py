from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import numpy as np

author = 'S. Youn'

doc = """
        Experiment for testing Heidhues, Koszegi, and Strack (2018)
"""

import random

class Constants(BaseConstants):
    name_in_url = 'part7'
    players_per_group = None
    num_rounds = 1

class Group(BaseGroup):
    pass

class Subsession(BaseSubsession):
    pass

class Player(BasePlayer):

    sex = models.StringField(widget=widgets.RadioSelectHorizontal(),choices=['Male', 'Female', 'Decline to state'])
    age = models.IntegerField(choices = range(18,60,1))
    major = models.StringField(widget=widgets.RadioSelectHorizontal(),choices=['Yes.', 'No.'])
    advice = models.TextField(label="Your comment here:")
    part1 = models.StringField(widget=widgets.RadioSelectHorizontal(),choices=['Very easy', 'Easy', 'Hard', 'Very hard'])
    comment = models.TextField(label="Your comment here:")
    










