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
import time

class Constants(BaseConstants):
    name_in_url = 'part4'
    players_per_group = None
    num_rounds = 1

    
class Group(BaseGroup):
    pass

class Subsession(BaseSubsession):
    pass

class Player(BasePlayer):

    bin1_mine = models.IntegerField(min=0, max=100)
    bin2_mine = models.IntegerField(min=0, max=100)
    bin3_mine = models.IntegerField(min=0, max=100)
    bin4_mine = models.IntegerField(min=0, max=100)
    bin5_mine = models.IntegerField(min=0, max=100)
    bin6_mine = models.IntegerField(min=0, max=100)
    bin7_mine = models.IntegerField(min=0, max=100)
    bin8_mine = models.IntegerField(min=0, max=100)
    bin9_mine = models.IntegerField(min=0, max=100)
    bin10_mine = models.IntegerField(min=0, max=100)

    bin1_teammate = models.IntegerField(min=0, max=100)
    bin2_teammate = models.IntegerField(min=0, max=100)
    bin3_teammate = models.IntegerField(min=0, max=100)
    bin4_teammate = models.IntegerField(min=0, max=100)
    bin5_teammate = models.IntegerField(min=0, max=100)
    bin6_teammate = models.IntegerField(min=0, max=100)
    bin7_teammate = models.IntegerField(min=0, max=100)
    bin8_teammate = models.IntegerField(min=0, max=100)
    bin9_teammate = models.IntegerField(min=0, max=100)
    bin10_teammate = models.IntegerField(min=0, max=100)


    

