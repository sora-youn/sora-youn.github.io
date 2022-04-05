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
    name_in_url = 'RiskAmb'
    players_per_group = None
    num_rounds = 1

    # these are the lottery payoffs, f1 and f2 refer to lottery A and f3 and f4 to lottery B
    f1 = 20
    f2 = 16
    f3 = 38.5
    f4 = 1

    # these are the lottery payoffs
    g0 = 20
    g1 = 16.4
    g2 = 17.2
    g3 = 18
    g4 = 18.8
    g5 = 19.6
    g6 = 20.4
    g7 = 21.2
    g8 = 22
    g9 = 22.8
    g10 = 23.6
    g11 = 24.4
    g12 = 25.2
    g13 = 26
    g14 = 26.8
    g15 = 27.6
    g16 = 28.4
    g17 = 29.2
    g18 = 30
    g19 = 30.8
    g20 = 31.6

class Group(BaseGroup):
    pass

class Subsession(BaseSubsession):
    pass

class Player(BasePlayer):
    risk = models.PositiveIntegerField(choices=[[0, ''],[1, ''],[2, ''],[3, ''],[4, ''],[5, ''],[6, ''],[7, ''],[8, ''],[9, ''],[10, '']],widget=widgets.RadioSelectHorizontal)
    ambig = models.PositiveIntegerField(choices=[[0, ''],[1, ''],[2, ''],[3, ''],[4, ''],[5, ''],[6, ''],[7, ''],[8, ''],[9, ''],[10, ''],[11, ''],[12, ''],[13, ''],[14, ''],[15, ''],[16, ''],[17, ''],[18, ''],[19, '']],widget=widgets.RadioSelectHorizontal)

    def set_payoff(self):

    # Risk preferences

        #*******************************************
        # select random row and random outcome
        #*******************************************

        # select one row randomly for payment (from module random)
        self.participant.vars['Payment_row_risk'] = random.randint(0,10) # start and end both included
        
        # select the number x that defines the outcome of the lottery (if x<=p, outcome is left f1 or f3, otherwise f2 or f4)
        # write it to participant.vars['RandomNum']
        self.participant.vars['RandomNum_risk'] = random.randint(0,10) # start and end both included
        
        #*******************************************
        # select choices in correspondence to random row
        #*******************************************
        
        # create a list of choices
        choice_risk = []
        for p in range(0,11) :    # range(0,10) = [0,1,2,...,9,10]
            if p < self.risk :
                choice_risk.insert(p, "A")
            else :
                choice_risk.insert(p, "B")

        # select from the list the choice in correspondence to the randomly drawn row (notice the offset)
        # write it to participant.vars['risk_choice']
        self.participant.vars['risk_choice'] = choice_risk[self.participant.vars['Payment_row_risk']]

        #*******************************************
        # Compute here the payoffs
        #*******************************************

        # Notice the winning probability of each row equals to ('payment_row')/10
        if self.participant.vars['risk_choice'] == "A":
            if self.participant.vars['RandomNum_risk'] <= self.participant.vars['Payment_row_risk']:
                self.participant.vars['ED_risk'] = Constants.f1
            else:
                self.participant.vars['ED_risk'] = Constants.f2
        else: 
            if self.participant.vars['RandomNum_risk'] <= self.participant.vars['Payment_row_risk']:
                self.participant.vars['ED_risk'] = Constants.f3
            else:
                self.participant.vars['ED_risk'] = Constants.f4

    # Ambiguity preferences

        #*******************************************
        # select random row and random outcome
        #*******************************************

        # select one row randomly for payment (from module random)
        self.participant.vars['Payment_row_amb'] = random.randint(1,20) # start and end both included
        
        # define the number of red balls 
        # Urn A
        self.participant.vars['num_reds_UrnA'] = 50 
        # Urn B
        self.participant.vars['num_reds_UrnB'] = random.randint(0,100) # start and end both included

        # select the number x that defines the outcome of the lottery 
        # if x<=num_reds_Urn, win the lottery; otherwise, earn 0.
        # write it to participant.vars['RandomNum']
        self.participant.vars['RandomNum_amb'] = random.randint(1,100) # start and end both included

        #*******************************************
        # select choices in correspondence to random row
        #*******************************************

        # create a list of prizes
        prize = [Constants.g1,Constants.g2,Constants.g3,Constants.g4,Constants.g5,Constants.g6,Constants.g7,Constants.g8,Constants.g9,Constants.g10,Constants.g11,Constants.g12,Constants.g13,Constants.g14,Constants.g15,Constants.g16,Constants.g17,Constants.g18,Constants.g19,Constants.g20]

        # create a list of choices
        choice_amb = []
        for p in range(0,20) :
            if p < self.ambig :
                choice_amb.insert(p, "A")
            else :
                choice_amb.insert(p, "B")
    
        # define the paid choice
        self.participant.vars['amb_choice'] = choice_amb[self.participant.vars['Payment_row_amb']-1]

        #*******************************************
        # Compute here the payoffs
        #*******************************************
        if self.participant.vars['amb_choice'] == "A":
            if self.participant.vars['RandomNum_amb'] <= self.participant.vars['num_reds_UrnA']:
                self.participant.vars['ED_amb'] = Constants.g0
            else:
                self.participant.vars['ED_amb'] = 0
        else: 
            if self.participant.vars['RandomNum_amb'] <= self.participant.vars['num_reds_UrnB']:
                self.participant.vars['ED_amb'] = prize[self.participant.vars['Payment_row_amb']-1]
            else:
                self.participant.vars['ED_amb'] = 0


        #*******************************************
        # Final payoff
        #*******************************************

        # select which part will be paid
        self.participant.vars['pref_payment'] = random.randint(1,2)

        ##
        if self.participant.vars['pref_payment'] == 1:
            self.payoff = self.participant.vars['ED_risk']
        else:
            self.payoff = self.participant.vars['ED_amb']
        





