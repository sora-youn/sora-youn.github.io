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
    name_in_url = 'part3_T1'
    players_per_group = None
    num_attention_check_tries = 2
    num_game_round = 3
    num_rounds = num_attention_check_tries + num_game_round - 1
    ans_part3_cq1 = [0,0]
    ans_part3_cq2 = [50,40]
    ans_part3_cq3 = 0
    ans_part3_cq4 = 1
    ans_part3_cq5 = 0
    prize = 200
    max_lt = 25

class Group(BaseGroup):
    pass

class Subsession(BaseSubsession):

    def creating_session(self):
        if self.round_number == 1:
            paying_round = random.randint(1, Constants.num_rounds)
            self.session.vars['paying_round'] = paying_round


class Player(BasePlayer):
    part3_cq1_a = models.PositiveIntegerField(choices=[[0, 'True'],[1, 'False']],widget=widgets.RadioSelectHorizontal)
    part3_cq1_b = models.PositiveIntegerField(choices=[[0, 'True'],[1, 'False']],widget=widgets.RadioSelectHorizontal)
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


    def set_payoff(self):

        ############################ PAYOFF FOR EACH ROUND ############################

        self.draw_urn2 = 100 - self.draw_urn1

        ## T1
        Prob_Red_Urn1 = self.participant.vars['productivity']/100
        Prob_Red_Urn2 = self.participant.vars['fundamental']/100

        DrawnBalls_Urn1 = bernoulli.rvs(Prob_Red_Urn1, size = self.draw_urn1)
        DrawnBalls_Urn2 = bernoulli.rvs(Prob_Red_Urn2, size = self.draw_urn2)

        self.num_redballs_urn1 = sum(DrawnBalls_Urn1)
        self.num_redballs_urn2 = sum(DrawnBalls_Urn2)

        self.num_redballs =  sum(DrawnBalls_Urn1) + sum(DrawnBalls_Urn2)

        Prob_Lotterytickets_Urn1 = Prob_Red_Urn1 * pow(self.draw_urn1, -0.5) 
        Prob_Lotterytickets_Urn2 = Prob_Red_Urn2 * pow(self.draw_urn2, -0.5) 

        AwardedLTs_Urn1 = bernoulli.rvs(Prob_Lotterytickets_Urn1, size = self.num_redballs_urn1)
        AwardedLTs_Urn2 = bernoulli.rvs(Prob_Lotterytickets_Urn2, size = self.num_redballs_urn2)

        self.num_LTs_Awareded_Urn1 = sum(AwardedLTs_Urn1) *1
        self.num_LTs_Awareded_Urn2 = sum(AwardedLTs_Urn2) *1
        
        self.num_LTs_Awareded = self.num_LTs_Awareded_Urn1 + self.num_LTs_Awareded_Urn2

        self.game_round_number = self.subsession.round_number - 1


        ## Draw a random number
        self.participant.vars['Part3_X'] = random.randint(0,Constants.max_lt)

        ##
        if self.num_LTs_Awareded >= self.participant.vars['Part3_X'] :
            self.participant.vars['points_earned_Part3'] = Constants.prize
        else:
            self.participant.vars['points_earned_Part3'] = 0


        ############################ PAYOFF REALIZATION ############################

        if self.round_number == self.session.vars['paying_round'] +1:
            self.payoff = self.participant.vars['points_earned_Part3'] 
        else :
            self.payoff = 0

        






