from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import numpy as np
import random
import time
from scipy.stats import bernoulli

author = 'S. Youn'

doc = """
        Experiment for testing Heidhues, Koszegi, and Strack (2018)
"""

class Constants(BaseConstants):
    name_in_url = 'WorkAllocationTask'
    players_per_group = None
    num_rounds = 50
    identifiability = 1 
    nonidentifiability = 2
    robot = 50
    sigma = 10  # standard deviation. NOT variance. 
    ED_guess = 100
    ED_lottery = 500
    max_lt = 2500

class Group(BaseGroup):
    pass

class Subsession(BaseSubsession):
    identifiable  = models.BooleanField()

    def creating_session(self):
        self.identifiable = self.session.config.get('identifiable')

        for p in self.get_players():
            if self.identifiable:
                p.trt = Constants.identifiability
            else:
                p.trt = Constants.nonidentifiability

        if self.round_number == 1:
            # paying round - Task A
            paying_taskA = random.randint(1, Constants.num_rounds)
            self.session.vars['paying_taskA'] = paying_taskA

            # paying round - Task B
            paying_taskB = random.randint(1, Constants.num_rounds)
            self.session.vars['paying_taskB'] = paying_taskB


class Player(BasePlayer):

    trt = models.FloatField()

    my_prod = models.FloatField()
    teammate_prod = models.FloatField()

    guess_mine = models.IntegerField(min=0, max=100)
    guess_teammate = models.IntegerField(min=0, max=100)

    draw_urn1 = models.IntegerField(min=0, max=100)
    draw_urn2 = models.IntegerField(min=0, max=100)

    team_prod = models.FloatField()
    lucky_num = models.FloatField()
    points = models.FloatField(min=0, max=100)

    check_DecisionSlider = models.BooleanField(blank=True)
    check_GuessInput = models.BooleanField(blank=True, choices=[ [True, 'Confirm'] ])


    ######################################################################### 
    def set_payoff(self):

        self.my_prod = self.participant.vars['my_prod']
        self.teammate_prod = self.participant.vars['teammate_prod']

        ######## guess outcome ##########
        if self.guess_mine == self.my_prod :
            self.participant.vars['Earning_A1'] = Constants.ED_guess
        else:
            self.participant.vars['Earning_A1'] = 0

        if self.guess_teammate == self.teammate_prod :
            self.participant.vars['Earning_A2'] = Constants.ED_guess
        else:
            self.participant.vars['Earning_A2'] = 0

        ######## action choice ##########
        self.draw_urn2 = 100 - self.draw_urn1

        ######## treatment conditions ##########
        if self.trt == 1 :
            Prod_Urn1 = self.my_prod
            Prod_Urn2 = self.teammate_prod
        else :
            Prod_Urn1 = (self.my_prod + self.teammate_prod)/2
            Prod_Urn2 = Constants.robot

        ######## team productivity ##########
        self.team_prod = Prod_Urn1 * pow(self.draw_urn1, 0.5) + Prod_Urn2 * pow(self.draw_urn2, 0.5)

        ######## lucky number ##########
        self.lucky_num = np.random.normal(0, Constants.sigma)

        ######## points ##########
        self.points = round(self.team_prod + self.lucky_num, 2)

        ######## Draw a random number for the lottery ##########
        self.participant.vars['lottery'] = random.randint(0,Constants.max_lt)

        ######## lottery outcome ##########
        if self.points >= self.participant.vars['lottery'] :
            self.participant.vars['Earning_B'] = Constants.ED_lottery
        else:
            self.participant.vars['Earning_B'] = 0


        ############################ PAYOFF REALIZATION ############################
        if self.round_number == self.session.vars['paying_taskA']:
            self.participant.vars['Pay_TaskA']  = self.participant.vars['Earning_A1'] + self.participant.vars['Earning_A2']
        else :
            self.participant.vars['Pay_TaskA'] = 0

        if self.round_number == self.session.vars['paying_taskB']:
            self.participant.vars['Pay_TaskB']  = self.participant.vars['Earning_B'] 
        else :
            self.participant.vars['Pay_TaskB'] = 0
        
        ## Total payoff
        self.payoff = self.participant.vars['Pay_TaskA'] + self.participant.vars['Pay_TaskB']

