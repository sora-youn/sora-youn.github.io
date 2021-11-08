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
    name_in_url = 'part5'
    players_per_group = None
    num_rounds = 1
    # these are the lottery payoffs, f1 and f2 refer to lottery A and f3 and f4 to lottery B
    f1 = 20
    f2 = 16
    f3 = 38.5
    f4 = 1

class Group(BaseGroup):
    pass

class Subsession(BaseSubsession):
    pass

class Player(BasePlayer):
    risk = models.PositiveIntegerField(choices=[[0, ''],[1, ''],[2, ''],[3, ''],[4, ''],[5, ''],[6, ''],[7, ''],[8, ''],[9, '']],widget=widgets.RadioSelectHorizontal)

    # Define here the methods associated to Players
    # this method is needed to compute payoffs
    def set_payoff(self):
        #*******************************************
        # select between part 5 and part 6 for payment
        #*******************************************

        # select which part will be paid
        self.participant.vars['pref_payment'] = random.randint(1,2)

        #*******************************************
        # select random row and random outcome
        #*******************************************

        # select one row randomly for payment (from module random)
        self.participant.vars['Payment_row'] = random.randint(1,10)
        
        # select the number x that defines the outcome of the lottery (if x<=p, outcome is left f1 or f3, otherwise f2 or f4)
        # write it to participant.vars['RandomNum']
        self.participant.vars['RandomNum'] = random.randint(1,10)
        
        #*******************************************
        # select choices in correspondence to random row
        #*******************************************
        
        # create a list of choices
        choice = []
        for p in range(0,10) :
            if p < self.risk :
                choice.insert(p, "A")
            else :
                choice.insert(p, "B")

        # select from the list the choice in correspondence to the randomly drawn row (notice the offset)
        # write it to participant.vars['Part5_choice']
        self.participant.vars['Part5_choice'] = choice[self.participant.vars['Payment_row']-1]

        #*******************************************
        # Compute here the payoffs
        #*******************************************

        # Notice the winning probability of each row equals to 'payment_row'
        if self.participant.vars['Part5_choice'] == "A":
            if self.participant.vars['RandomNum'] <= self.participant.vars['Payment_row']:
                self.participant.vars['points_earned_Part5'] = Constants.f1
            else:
                self.participant.vars['points_earned_Part5'] = Constants.f2
        else: 
            if self.participant.vars['RandomNum'] <= self.participant.vars['Payment_row']:
                self.participant.vars['points_earned_Part5'] = Constants.f3
            else:
                self.participant.vars['points_earned_Part5'] = Constants.f4

        # write the payoff to player.payoff
        if self.participant.vars['pref_payment'] == 1:
            self.payoff = self.participant.vars['points_earned_Part5']
        else:
            self.payoff = 0
        









