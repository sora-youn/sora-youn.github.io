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
    f1 = 200
    f2 = 160
    f3 = 385
    f4 = 10

class Group(BaseGroup):
    pass

class Subsession(BaseSubsession):
    pass

class Player(BasePlayer):

    # This is for main choices, each variable is one row in the choice table MPL
    risk1 = models.PositiveIntegerField(choices=[[1, 'A'],[2, 'B']],widget=widgets.RadioSelectHorizontal)
    risk2 = models.PositiveIntegerField(choices=[[1, 'A'],[2, 'B']],widget=widgets.RadioSelectHorizontal)
    risk3 = models.PositiveIntegerField(choices=[[1, 'A'],[2, 'B']],widget=widgets.RadioSelectHorizontal)
    risk4 = models.PositiveIntegerField(choices=[[1, 'A'],[2, 'B']],widget=widgets.RadioSelectHorizontal)
    risk5 = models.PositiveIntegerField(choices=[[1, 'A'],[2, 'B']],widget=widgets.RadioSelectHorizontal)
    risk6 = models.PositiveIntegerField(choices=[[1, 'A'],[2, 'B']],widget=widgets.RadioSelectHorizontal)
    risk7 = models.PositiveIntegerField(choices=[[1, 'A'],[2, 'B']],widget=widgets.RadioSelectHorizontal)
    risk8 = models.PositiveIntegerField(choices=[[1, 'A'],[2, 'B']],widget=widgets.RadioSelectHorizontal)
    risk9 = models.PositiveIntegerField(choices=[[1, 'A'],[2, 'B']],widget=widgets.RadioSelectHorizontal)
    risk10 = models.PositiveIntegerField(choices=[[1, 'A'],[2, 'B']],widget=widgets.RadioSelectHorizontal)

    # This is for main choices, each variable is one row in the choice table MPL
    ambig1 = models.PositiveIntegerField(choices=[[1, 'A'],[2, 'B']],widget=widgets.RadioSelectHorizontal)
    ambig2 = models.PositiveIntegerField(choices=[[1, 'A'],[2, 'B']],widget=widgets.RadioSelectHorizontal)
    ambig3 = models.PositiveIntegerField(choices=[[1, 'A'],[2, 'B']],widget=widgets.RadioSelectHorizontal)
    ambig4 = models.PositiveIntegerField(choices=[[1, 'A'],[2, 'B']],widget=widgets.RadioSelectHorizontal)
    ambig5 = models.PositiveIntegerField(choices=[[1, 'A'],[2, 'B']],widget=widgets.RadioSelectHorizontal)
    ambig6 = models.PositiveIntegerField(choices=[[1, 'A'],[2, 'B']],widget=widgets.RadioSelectHorizontal)
    ambig7 = models.PositiveIntegerField(choices=[[1, 'A'],[2, 'B']],widget=widgets.RadioSelectHorizontal)
    ambig8 = models.PositiveIntegerField(choices=[[1, 'A'],[2, 'B']],widget=widgets.RadioSelectHorizontal)
    ambig9 = models.PositiveIntegerField(choices=[[1, 'A'],[2, 'B']],widget=widgets.RadioSelectHorizontal)
    ambig10 = models.PositiveIntegerField(choices=[[1, 'A'],[2, 'B']],widget=widgets.RadioSelectHorizontal)

    # This is needed for the instructions
    practice = models.PositiveIntegerField(choices=[[1, 'A'],[2, 'B']],widget=widgets.RadioSelectHorizontal,blank=True)

    # These variables are collected in the final questionnaire
    sex = models.StringField(widget=widgets.RadioSelectHorizontal(),choices=['Male', 'Female'])
    age = models.IntegerField(choices = range(18,60,1))
    comment = models.TextField(label="Your comment here:")
    like = models.FloatField()

    payoff_slider = models.FloatField()

    # Define here the methods associated to Players
    # this method is needed to compute payoffs
    def set_payoff_HL(self):
        #*******************************************
        # select random row and random outcome
        #*******************************************
        self.participant.vars['HL_row'] = random.randint(1,10)
        # select one row randomly for payment (from module random)
        self.participant.vars['HL_random'] = random.randint(1,10)
        # select the number x that defines the outcome of the lottery (if x<=p, outcome is left f1 or f3, otherwise f2 or f4)
        # write it to participant.vars['HL_random']

        #*******************************************
        # select choices in correspondence to random row
        #*******************************************
        choices = [self.risk1,self.risk2,self.risk3,self.risk4,self.risk5,self.risk6,self.risk7,self.risk8,self.risk9,self.risk10]
        # create a list with all choices of the player (see self)
        self.participant.vars['HL_choice'] = choices[self.participant.vars['HL_row']-1]
        # select from the list the choice in correspondence to the randomly drawn row (notice the offset)
        # write it to participant.vars['HL_choice']

        #*******************************************
        # Compute here the payoffs
        #*******************************************
        if self.participant.vars['HL_random'] <= self.participant.vars['HL_row']:
        # if the random number is smaller equal than the random row
            if self.participant.vars['HL_choice'] == 1: #A
            # if the choice was A
                self.participant.vars['payoff_HL'] = Constants.f1
                # because HL_row is the same as p in the MPL
            else :
            # if the choice was B
                self.participant.vars['payoff_HL'] = Constants.f3
        else:
        # if the random number is slarger than the random row
            if self.participant.vars['HL_choice'] == 1 :#A
                # if the choice was A
                self.participant.vars['payoff_HL'] = Constants.f2
                # because HL_row is the same as p in the MPL
            else :
                self.participant.vars['payoff_HL'] = Constants.f4

        self.payoff = self.participant.vars['payoff_HL']
        # write the payoff to player.payoff


    def set_payoffs_slider(self):
        if self.like <= 50.5 :
            if self.like >= 49.5: 
                self.payoff_slider = 1
            
            else :
                self.payoff_slider = 0
        else : 
            self.payoff_slider = 0









