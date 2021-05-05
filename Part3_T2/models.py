from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import numpy as np
from scipy.stats import bernoulli

author = 'S. Youn'

doc = """
        Experiment for testing Heidhues, Koszegi, and Strack (2018)
"""

import random
import time

class Constants(BaseConstants):
    name_in_url = 'part3_T2'
    players_per_group = None
    num_attention_check_tries = 2
    num_game_round = 10
    num_rounds = num_attention_check_tries + num_game_round - 1
    ans_part3_cq1 = [100,90]
    ans_part3_cq2 = [50,45]
    ans_part3_cq3 = 0
    ans_part3_cq4 = 0
    ans_part3_cq5 = 0
    fundamental = 70 

class Group(BaseGroup):
    pass

class Subsession(BaseSubsession):

    def creating_session(self):
        if self.round_number == 1:
            paying_round = random.randint(1, Constants.num_rounds)
            self.session.vars['paying_round'] = paying_round


class Player(BasePlayer):
    part3_cq1_a = models.IntegerField(min=0, max=100)
    part3_cq1_b = models.IntegerField(min=0, max=100)
    part3_cq2_a = models.IntegerField(min=0, max=100)
    part3_cq2_b = models.IntegerField(min=0, max=100)
    part3_cq3 = models.PositiveIntegerField(choices=[[0, 'True'],[1, 'False']],widget=widgets.RadioSelectHorizontal)
    part3_cq4 = models.PositiveIntegerField(choices=[[0, 'True'],[1, 'False']],widget=widgets.RadioSelectHorizontal)
    part3_cq5 = models.PositiveIntegerField(choices=[[0, 'True'],[1, 'False']],widget=widgets.RadioSelectHorizontal)

    guess_mine = models.IntegerField(min=0, max=100)
    guess_teammate = models.IntegerField(min=0, max=100)

    draw_urn1 = models.IntegerField(min=0, max=100)
    draw_urn2 = models.IntegerField(min=0, max=100)

    num_redballs_urn1 = models.IntegerField(min=0, max=100)
    num_redballs_urn2 = models.IntegerField(min=0, max=100)
    num_redballs = models.IntegerField(min=0, max=100)

    num_LTs_Awareded_Urn1 = models.IntegerField(min=0, max=100)
    num_LTs_Awareded_Urn2 = models.IntegerField(min=0, max=100)
    num_LTs_Awareded = models.IntegerField(min=0, max=100)

    game_round_number = models.IntegerField(min=0, max=100)

    check_DecisionSlider = models.BooleanField(blank=True)