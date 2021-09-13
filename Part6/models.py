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
    name_in_url = 'part6'
    players_per_group = None
    num_rounds = 1
    # these are the lottery payoffs
    g0 = 200
    g1 = 164
    g2 = 172
    g3 = 180
    g4 = 188
    g5 = 196
    g6 = 204
    g7 = 212
    g8 = 220
    g9 = 228
    g10 = 236
    g11 = 244
    g12 = 252
    g13 = 260
    g14 = 268
    g15 = 276
    g16 = 284
    g17 = 292
    g18 = 300
    g19 = 308
    g20 = 316

class Group(BaseGroup):
    pass

class Subsession(BaseSubsession):
    pass

class Player(BasePlayer):
    ambig = models.PositiveIntegerField(choices=[[0, ''],[1, ''],[2, ''],[3, ''],[4, ''],[5, ''],[6, ''],[7, ''],[8, ''],[9, ''],[10, ''],[11, ''],[12, ''],[13, ''],[14, ''],[15, ''],[16, ''],[17, ''],[18, ''],[19, '']],widget=widgets.RadioSelectHorizontal)

    # This is needed for the instructions
    practice = models.PositiveIntegerField(choices=[[1, ''],[2, '']],widget=widgets.RadioSelectHorizontal, blank=True)

    # Define here the methods associated to Players
    # this method is needed to compute payoffs
    def set_payoff(self):
        #*******************************************
        # select random row and random outcome
        #*******************************************

        # select one row randomly for payment (from module random)
        self.participant.vars['Payment_row'] = random.randint(1,20)
        
        # define the number of red balls 
        # Urn A
        self.participant.vars['num_reds_UrnA'] = 50 
        # Urn B
        self.participant.vars['num_reds_UrnB'] = random.randint(0,100)

        # select the number x that defines the outcome of the lottery 
        # if x<=num_reds_Urn, win the lottery; otherwise, earn 0.
        # write it to participant.vars['RandomNum']
        self.participant.vars['RandomNum'] = random.randint(1,100)

        #*******************************************
        # select choices in correspondence to random row
        #*******************************************

        # create a list of prizes
        prize = [Constants.g1,Constants.g2,Constants.g3,Constants.g4,Constants.g5,Constants.g6,Constants.g7,Constants.g8,Constants.g9,Constants.g10,Constants.g11,Constants.g12,Constants.g13,Constants.g14,Constants.g15,Constants.g16,Constants.g17,Constants.g18,Constants.g19,Constants.g20]

        # create a list of choices
        choice = []
        for p in range(0,20) :
            if p <= self.ambig :
                choice.insert(p, "A")
            else :
                choice.insert(p, "B")
    
        # define the paid choice
        self.participant.vars['Part6_choice'] = choice[self.participant.vars['Payment_row']-1]

        #*******************************************
        # Compute here the payoffs
        #*******************************************
        if self.participant.vars['Part6_choice'] == "A":
            if self.participant.vars['RandomNum'] <= self.participant.vars['num_reds_UrnA']:
                self.participant.vars['points_earned_Part6'] = Constants.g0
            else:
                self.participant.vars['points_earned_Part6'] = 0
        else: 
            if self.participant.vars['RandomNum'] <= self.participant.vars['num_reds_UrnB']:
                self.participant.vars['points_earned_Part6'] = prize[self.participant.vars['Payment_row']-1]
            else:
                self.participant.vars['points_earned_Part6'] = 0

        # write the payoff to player.payoff
        if self.participant.vars['pref_payment'] == 2:
            self.payoff = self.participant.vars['points_earned_Part6']
        else:
            self.payoff = 0
        


  








