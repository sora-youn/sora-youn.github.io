from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import numpy as np
import statistics

author = 'S. Youn'

doc = """
        Experiment for testing Heidhues, Koszegi, and Strack (2018)
"""

import random
import time

class Constants(BaseConstants):
    name_in_url = 'part2'
    players_per_group = 2
    num_rounds = 1
    ans_part2_cq1 = 0
    ans_part2_cq2_mine = [0,0,0,0,0,100,0,0,0,0]
    ans_part2_cq2_teammate = [0,0,0,50,50,0,0,0,0,0]
    ans_part2_cq3 = 0
    prize = 100
    
class Subsession(BaseSubsession):
    def creating_session(self):
        self.group_randomly(fixed_id_in_group=True)

        print(self.get_group_matrix())
    
class Group(BaseGroup):

    def set_fundamental(self):

        player1 = self.get_player_by_id(1)
        player2 = self.get_player_by_id(2)

        player1.participant.vars['fundamental'] = player2.participant.vars['GreenReceived']
        player1.participant.vars['bin_index_teammate'] = player2.participant.vars['bin_index_mine']

        player2.participant.vars['fundamental'] = player1.participant.vars['GreenReceived']
        player2.participant.vars['bin_index_teammate'] = player1.participant.vars['bin_index_mine']



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

    GreenReceived = models.FloatField()
    fundamental = models.FloatField()
    
    ############################ ATTENTION CHECK ############################ 
    def part2_cq1_error_message(self, value):
        if value != Constants.ans_part2_cq1 :
            return 'Wrong!'
    
    def part2_cq2_bin1_mine_error_message(self, value):
        if value != Constants.ans_part2_cq2_mine[0]:
            return 'Wrong!'

    def part2_cq2_bin2_mine_error_message(self, value):
        if value != Constants.ans_part2_cq2_mine[1]:
            return 'Wrong!'

    def part2_cq2_bin3_mine_error_message(self, value):
        if value != Constants.ans_part2_cq2_mine[2]:
            return 'Wrong!'

    def part2_cq2_bin4_mine_error_message(self, value):
        if value != Constants.ans_part2_cq2_mine[3]:
            return 'Wrong!'

    def part2_cq2_bin5_mine_error_message(self, value):
        if value != Constants.ans_part2_cq2_mine[4]:
            return 'Wrong!'

    def part2_cq2_bin6_mine_error_message(self, value):
        if value != Constants.ans_part2_cq2_mine[5]:
            return 'Wrong!'

    def part2_cq2_bin7_mine_error_message(self, value):
        if value != Constants.ans_part2_cq2_mine[6]:
            return 'Wrong!'

    def part2_cq2_bin8_mine_error_message(self, value):
        if value != Constants.ans_part2_cq2_mine[7]:
            return 'Wrong!'

    def part2_cq2_bin9_mine_error_message(self, value):
        if value != Constants.ans_part2_cq2_mine[8]:
            return 'Wrong!'

    def part2_cq2_bin10_mine_error_message(self, value):
        if value != Constants.ans_part2_cq2_mine[9]:
            return 'Wrong!'      

    def part2_cq2_bin1_teammate_error_message(self, value):
        if value != Constants.ans_part2_cq2_teammate[0]:
            return 'Wrong!'

    def part2_cq2_bin2_teammate_error_message(self, value):
        if value != Constants.ans_part2_cq2_teammate[1]:
            return 'Wrong!'

    def part2_cq2_bin3_teammate_error_message(self, value):
        if value != Constants.ans_part2_cq2_teammate[2]:
            return 'Wrong!'

    def part2_cq2_bin4_teammate_error_message(self, value):
        if value != Constants.ans_part2_cq2_teammate[3]:
            return 'Wrong!'

    def part2_cq2_bin5_teammate_error_message(self, value):
        if value != Constants.ans_part2_cq2_teammate[4]:
            return 'Wrong!'

    def part2_cq2_bin6_teammate_error_message(self, value):
        if value != Constants.ans_part2_cq2_teammate[5]:
            return 'Wrong!'

    def part2_cq2_bin7_teammate_error_message(self, value):
        if value != Constants.ans_part2_cq2_teammate[6]:
            return 'Wrong!'

    def part2_cq2_bin8_teammate_error_message(self, value):
        if value != Constants.ans_part2_cq2_teammate[7]:
            return 'Wrong!'

    def part2_cq2_bin9_teammate_error_message(self, value):
        if value != Constants.ans_part2_cq2_teammate[8]:
            return 'Wrong!'

    def part2_cq2_bin10_teammate_error_message(self, value):
        if value != Constants.ans_part2_cq2_teammate[9]:
            return 'Wrong!'          
    
    def part2_cq3_error_message(self, value):
        if value != Constants.ans_part2_cq3 :
            return 'Wrong!'


    ######################################################################### 
    def set_payoff(self):

        self.GreenReceived = self.participant.vars['GreenReceived']
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

        ## Draw random numbers
        self.participant.vars['Part2_X_mine'] = random.randint(0,20000)
        self.participant.vars['Part2_X_teammate'] = random.randint(0,20000)

        ##
        if A_mine_score <= self.participant.vars['Part2_X_mine'] :
            self.participant.vars['points_earned_Part2_mine'] = Constants.prize
        else:
            self.participant.vars['points_earned_Part2_mine'] = 0

        ##
        if A_teammate_score <= self.participant.vars['Part2_X_teammate'] :
            self.participant.vars['points_earned_Part2_teammate'] = Constants.prize
        else:
            self.participant.vars['points_earned_Part2_teammate'] = 0


        ##
        self.payoff = self.participant.vars['points_earned_Part2_mine'] + self.participant.vars['points_earned_Part2_teammate']
















    


    

