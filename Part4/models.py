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
    prize = 30

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

    fundamental = models.FloatField()

    
    def set_payoff(self):
        
        self.fundamental = self.participant.vars['fundamental']

        ##
        Indicator_mine = []
        for p in range(0,10) :
            if p == self.participant.vars['bin_index_mine']:
                Indicator_mine.insert(p,1)
            else :
                Indicator_mine.insert(p,0)
        
        ##
        Indicator_teammate = []
        for p in range(0,10) :
            if p == self.participant.vars['bin_index_teammate']:
                Indicator_teammate.insert(p,1)
            else :
                Indicator_teammate.insert(p,0)        

        ##
        bin_mine = [self.bin1_mine,self.bin2_mine,self.bin3_mine,self.bin4_mine,self.bin5_mine,self.bin6_mine,self.bin7_mine,self.bin8_mine,self.bin9_mine,self.bin10_mine]
        bin_teammate = [self.bin1_teammate,self.bin2_teammate,self.bin3_teammate,self.bin4_teammate,self.bin5_teammate,self.bin6_teammate,self.bin7_teammate,self.bin8_teammate,self.bin9_teammate,self.bin10_teammate]

        ##
        A_mine = []
        for p in range(0,10) :
            A_mine.append(pow(bin_mine[p] - 100*Indicator_mine[p],2))
        
        A_mine_score = sum(A_mine)

        ##
        A_teammate = []
        for p in range(0,10) :
            A_teammate.append(pow(bin_teammate[p] - 100*Indicator_teammate[p],2))
        
        A_teammate_score = sum(A_teammate)

        ##
        self.participant.vars['Part4_X_mine'] = random.randint(0,20000)
        self.participant.vars['Part4_X_teammate'] = random.randint(0,20000)

        ##
        if A_mine_score <= self.participant.vars['Part4_X_mine'] :
            self.participant.vars['points_earned_Part4_mine'] = Constants.prize
        else:
            self.participant.vars['points_earned_Part4_mine'] = 0

        ##
        if A_teammate_score <= self.participant.vars['Part4_X_teammate'] :
            self.participant.vars['points_earned_Part4_teammate'] = Constants.prize
        else:
            self.participant.vars['points_earned_Part4_teammate'] = 0


        ##
        self.payoff = self.participant.vars['points_earned_Part4_mine'] + self.participant.vars['points_earned_Part4_teammate']



    

