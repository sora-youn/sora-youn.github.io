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
    num_rounds = 51
    ans_part3_cq1 = [0,1]
    ans_part3_cq2 = [45,50]
    ans_part3_cq3 = 0
    ans_part3_cq4 = 1
    ans_part3_cq5 = 0
    prize = 500
    subcontractor = 100
    max_lt = 2500

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

    num_Gballs_urn1 = models.IntegerField(min=0, max=100)
    num_Gballs_urn2 = models.IntegerField(min=0, max=100)
    num_Gballs = models.IntegerField(min=0, max=100)

    num_LTs_Awareded_Urn1 = models.FloatField(min=0, max=100)
    num_LTs_Awareded_Urn2 = models.FloatField(min=0, max=100)
    num_LTs_Awareded = models.FloatField(min=0, max=100)

    check_DecisionSlider = models.BooleanField(blank=True)


    def set_payoff(self):

        ############################ PAYOFF FOR EACH ROUND ############################

        self.draw_urn2 = 100 - self.draw_urn1

        ## T1
        Prob_G_Urn1 = ( self.participant.vars['GreenReceived'] + self.participant.vars['fundamental'] )/200
        Prob_G_Urn2 = Constants.subcontractor/200

        DrawnBalls_Urn1 = bernoulli.rvs(Prob_G_Urn1, size = self.draw_urn1) # realization of the ball-draw from urn 1
        DrawnBalls_Urn2 = bernoulli.rvs(Prob_G_Urn2, size = self.draw_urn2) # realization of the ball-draw from urn 2

        # print(DrawnBalls_Urn1)
        # print(DrawnBalls_Urn2)

        self.num_Gballs_urn1 = sum(DrawnBalls_Urn1)
        self.num_Gballs_urn2 = sum(DrawnBalls_Urn2)

        self.num_Gballs =  sum(DrawnBalls_Urn1) + sum(DrawnBalls_Urn2)

        self.num_LTs_Awareded_Urn1 = self.num_Gballs_urn1 * pow(self.draw_urn1, -0.5) *100 # the number of drawn green balls * the number of lottery tickets per green ball
        self.num_LTs_Awareded_Urn2 = self.num_Gballs_urn2 * pow(self.draw_urn2, -0.5) *100 # the number of drawn green balls * the number of lottery tickets per green ball

        self.num_LTs_Awareded = round(self.num_LTs_Awareded_Urn1 + self.num_LTs_Awareded_Urn2,2)

        ## Draw a random number
        self.participant.vars['Part3_X'] = random.randint(0,Constants.max_lt)


        ##
        if self.num_LTs_Awareded >= self.participant.vars['Part3_X'] :
            self.participant.vars['points_earned_Part3'] = Constants.prize
        else:
            self.participant.vars['points_earned_Part3'] = 0


        ############################ PAYOFF REALIZATION ############################

        if self.round_number == self.session.vars['paying_round']:
            self.payoff = self.participant.vars['points_earned_Part3'] 
        else :
            self.payoff = 0



############################ ATTENTION CHECK ############################ 
    def part3_cq1_a_error_message(self, value):
        if value != Constants.ans_part3_cq1[0] :
            return 'Wrong!'
    
    def part3_cq1_b_error_message(self, value):
        if value != Constants.ans_part3_cq1[1]:
            return 'Wrong!'

    def part3_cq2_a_error_message(self, value):
        if value != Constants.ans_part3_cq2[0]:
            return 'Wrong!'

    def part3_cq2_b_error_message(self, value):
        if value != Constants.ans_part3_cq2[1]:
            return 'Wrong!'

    def part3_cq3_error_message(self, value):
        if value != Constants.ans_part3_cq3:
            return 'Wrong!'

    def part3_cq4_error_message(self, value):
        if value != Constants.ans_part3_cq4:
            return 'Wrong!'

    def part3_cq5_error_message(self, value):
        if value != Constants.ans_part3_cq5:
            return 'Wrong!'





