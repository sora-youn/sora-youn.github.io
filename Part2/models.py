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
    name_in_url = 'part2'
    players_per_group = None
    num_attention_check_tries = 2
    num_game_round = 1
    num_rounds = num_attention_check_tries + num_game_round - 1
    ans_part2_cq1 = 0
    ans_part2_cq2_mine = [0,0,0,0,0,100,0,0,0,0]
    ans_part2_cq2_teammate = [0,0,0,50,50,0,0,0,0,0]
    ans_part2_cq3 = 0
    
class Group(BaseGroup):
    pass

class Subsession(BaseSubsession):
    pass

class Player(BasePlayer):
    part2_cq1 = models.PositiveIntegerField(choices=[[0, 'True'],[1, 'False']],widget=widgets.RadioSelectHorizontal)
   
    part2_cq2_bin1_mine = models.IntegerField(min=0, max=100)
    part2_cq2_bin2_mine = models.IntegerField(min=0, max=100)
    part2_cq2_bin3_mine = models.IntegerField(min=0, max=100)
    part2_cq2_bin4_mine = models.IntegerField(min=0, max=100)
    part2_cq2_bin5_mine = models.IntegerField(min=0, max=100)
    part2_cq2_bin6_mine = models.IntegerField(min=0, max=100)
    part2_cq2_bin7_mine = models.IntegerField(min=0, max=100)
    part2_cq2_bin8_mine = models.IntegerField(min=0, max=100)
    part2_cq2_bin9_mine = models.IntegerField(min=0, max=100)
    part2_cq2_bin10_mine = models.IntegerField(min=0, max=100)

    part2_cq2_bin1_teammate = models.IntegerField(min=0, max=100)
    part2_cq2_bin2_teammate = models.IntegerField(min=0, max=100)
    part2_cq2_bin3_teammate = models.IntegerField(min=0, max=100)
    part2_cq2_bin4_teammate = models.IntegerField(min=0, max=100)
    part2_cq2_bin5_teammate = models.IntegerField(min=0, max=100)
    part2_cq2_bin6_teammate = models.IntegerField(min=0, max=100)
    part2_cq2_bin7_teammate = models.IntegerField(min=0, max=100)
    part2_cq2_bin8_teammate = models.IntegerField(min=0, max=100)
    part2_cq2_bin9_teammate = models.IntegerField(min=0, max=100)
    part2_cq2_bin10_teammate = models.IntegerField(min=0, max=100)

    part2_cq3 = models.PositiveIntegerField(choices=[[0, 'True'],[1, 'False']],widget=widgets.RadioSelectHorizontal)

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


    

