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
    name_in_url = 'part1'
    players_per_group = None
    num_attention_check_tries = 2
    num_game_round = 1
    num_rounds = num_attention_check_tries + num_game_round - 1
    payment_per_correct_answer = 1 
    ans_part1_cq1 = 0
    ans_part1_cq2 = 0
    ans_part1_cq3 = 1

class Group(BaseGroup):

    ############################ SET THE FUNDAMENTAL ############################
    def set_fundamental(self):

        all_players = self.get_players()
        fundamental_list = [p.productivity for p in all_players]

        for p in all_players:
            p.participant.vars['fundamental'] = statistics.median_high(fundamental_list)

            ##
            if p.participant.vars['fundamental'] <=10:
                p.participant.vars['bin_index_teammate'] = 0
            elif p.participant.vars['fundamental']>10 and p.participant.vars['fundamental']<=20:
                p.participant.vars['bin_index_teammate'] = 1
            elif p.participant.vars['fundamental']>20 and p.participant.vars['fundamental']<=30:
                p.participant.vars['bin_index_teammate'] = 2
            elif p.participant.vars['fundamental']>30 and p.participant.vars['fundamental']<=40:
                p.participant.vars['bin_index_teammate'] = 3
            elif p.participant.vars['fundamental']>40 and p.participant.vars['fundamental']<=50:
                p.participant.vars['bin_index_teammate'] = 4
            elif p.participant.vars['fundamental']>50 and p.participant.vars['fundamental']<=60:
                p.participant.vars['bin_index_teammate'] = 5
            elif p.participant.vars['fundamental']>60 and p.participant.vars['fundamental']<=70:
                p.participant.vars['bin_index_teammate'] = 6
            elif p.participant.vars['fundamental']>70 and p.participant.vars['fundamental']<=80:
                p.participant.vars['bin_index_teammate'] = 7
            elif p.participant.vars['fundamental']>80 and p.participant.vars['fundamental']<=90:
                p.participant.vars['bin_index_teammate'] = 8
            elif p.participant.vars['fundamental']>90 and p.participant.vars['fundamental']<=100:
                p.participant.vars['bin_index_teammate'] = 9
            

        

class Subsession(BaseSubsession):
    pass

class Player(BasePlayer):
    part1_cq1 = models.PositiveIntegerField(choices=[[0, 'True'],[1, 'False']],widget=widgets.RadioSelectHorizontal)
    part1_cq2 = models.PositiveIntegerField(choices=[[0, 'True'],[1, 'False']],widget=widgets.RadioSelectHorizontal)
    part1_cq3 = models.PositiveIntegerField(choices=[[0, 'True'],[1, 'False']],widget=widgets.RadioSelectHorizontal)

    slider1 = models.FloatField()
    slider2 = models.FloatField()
    slider3 = models.FloatField()
    slider4 = models.FloatField()
    slider5 = models.FloatField()
    slider6 = models.FloatField()
    slider7 = models.FloatField()
    slider8 = models.FloatField()
    slider9 = models.FloatField()
    slider10 = models.FloatField()
    slider11 = models.FloatField()
    slider12 = models.FloatField()
    slider13 = models.FloatField()
    slider14 = models.FloatField()
    slider15 = models.FloatField()
    slider16 = models.FloatField()
    slider17 = models.FloatField()
    slider18 = models.FloatField()
    slider19 = models.FloatField()
    slider20 = models.FloatField()
    slider21 = models.FloatField()
    slider22 = models.FloatField()
    slider23 = models.FloatField()
    slider24 = models.FloatField()
    slider25 = models.FloatField()
    slider26 = models.FloatField()
    slider27 = models.FloatField()
    slider28 = models.FloatField()
    slider29 = models.FloatField()
    slider30 = models.FloatField()
    slider31 = models.FloatField()
    slider32 = models.FloatField()
    slider33 = models.FloatField()
    slider34 = models.FloatField()
    slider35 = models.FloatField()
    slider36 = models.FloatField()
    slider37 = models.FloatField()
    slider38 = models.FloatField()
    slider39 = models.FloatField()
    slider40 = models.FloatField()
    slider41 = models.FloatField()
    slider42 = models.FloatField()
    slider43 = models.FloatField()
    slider44 = models.FloatField()
    slider45 = models.FloatField()
    slider46 = models.FloatField()
    slider47 = models.FloatField()
    slider48 = models.FloatField()
    slider49 = models.FloatField()
    slider50 = models.FloatField()
    slider51 = models.FloatField()
    slider52 = models.FloatField()
    slider53 = models.FloatField()
    slider54 = models.FloatField()
    slider55 = models.FloatField()
    slider56 = models.FloatField()
    slider57 = models.FloatField()
    slider58 = models.FloatField()
    slider59 = models.FloatField()
    slider60 = models.FloatField()
    slider61 = models.FloatField()
    slider62 = models.FloatField()
    slider63 = models.FloatField()
    slider64 = models.FloatField()
    slider65 = models.FloatField()
    slider66 = models.FloatField()
    slider67 = models.FloatField()
    slider68 = models.FloatField()
    slider69 = models.FloatField()
    slider70 = models.FloatField()
    slider71 = models.FloatField()
    slider72 = models.FloatField()
    slider73 = models.FloatField()
    slider74 = models.FloatField()
    slider75 = models.FloatField()
    slider76 = models.FloatField()
    slider77 = models.FloatField()
    slider78 = models.FloatField()
    slider79 = models.FloatField()
    slider80 = models.FloatField()
    slider81 = models.FloatField()
    slider82 = models.FloatField()
    slider83 = models.FloatField()
    slider84 = models.FloatField()
    slider85 = models.FloatField()
    slider86 = models.FloatField()
    slider87 = models.FloatField()
    slider88 = models.FloatField()
    slider89 = models.FloatField()
    slider90 = models.FloatField()
    slider91 = models.FloatField()
    slider92 = models.FloatField()
    slider93 = models.FloatField()
    slider94 = models.FloatField()
    slider95 = models.FloatField()
    slider96 = models.FloatField()
    slider97 = models.FloatField()
    slider98 = models.FloatField()
    slider99 = models.FloatField()
    slider100 = models.FloatField()

    productivity = models.FloatField()


    ############################ SET PAYOFFS ############################ 
    def set_payoff(self):

        slider = [ 
            self.slider1,
            self.slider2,
            self.slider3,
            self.slider4,
            self.slider5,
            self.slider6,
            self.slider7,
            self.slider8,
            self.slider9,
            self.slider10,
            self.slider11,
            self.slider12,
            self.slider13,
            self.slider14,
            self.slider15,
            self.slider16,
            self.slider17,
            self.slider18,
            self.slider19,
            self.slider20,
            self.slider21,
            self.slider22,
            self.slider23,
            self.slider24,
            self.slider25,
            self.slider26,
            self.slider27,
            self.slider28,
            self.slider29,
            self.slider30,
            self.slider31,
            self.slider32,
            self.slider33,
            self.slider34,
            self.slider35,
            self.slider36,
            self.slider37,
            self.slider38,
            self.slider39,
            self.slider40,
            self.slider41,
            self.slider42,
            self.slider43,
            self.slider44,
            self.slider45,
            self.slider46,
            self.slider47,
            self.slider48,
            self.slider49,
            self.slider50,
            self.slider51,
            self.slider52,
            self.slider53,
            self.slider54,
            self.slider55,
            self.slider56,
            self.slider57,
            self.slider58,
            self.slider59,
            self.slider60,
            self.slider61,
            self.slider62,
            self.slider63,
            self.slider64,
            self.slider65,
            self.slider66,
            self.slider67,
            self.slider68,
            self.slider69,
            self.slider70,
            self.slider71,
            self.slider72,
            self.slider73,
            self.slider74,
            self.slider75,
            self.slider76,
            self.slider77,
            self.slider78,
            self.slider79,
            self.slider80,
            self.slider81,
            self.slider82,
            self.slider83,
            self.slider84,
            self.slider85,
            self.slider86,
            self.slider87,
            self.slider88,
            self.slider89,
            self.slider90,
            self.slider91,
            self.slider92,
            self.slider93,
            self.slider94,
            self.slider95,
            self.slider96,
            self.slider97,
            self.slider98,
            self.slider99,
            self.slider100
        ]

        
        ## count the number of correctly positioned sliders
        self.participant.vars['productivity'] = 0

        for x in slider:
            if x <= 50.5 :
                if x >= 49.5: 
                    self.participant.vars['productivity'] = self.participant.vars['productivity'] + 1
                else :
                    self.participant.vars['productivity'] = self.participant.vars['productivity'] + 0
            else : 
                self.participant.vars['productivity'] = self.participant.vars['productivity'] + 0

        self.productivity = self.participant.vars['productivity']
        
        ## payoff from Part 1 = the number of correctly positioned sliders
        self.payoff = self.participant.vars['productivity']

        ##
        if self.participant.vars['productivity'] <=10:
            self.participant.vars['bin_index_mine'] = 0
        elif self.participant.vars['productivity']>10 and self.participant.vars['productivity']<=20:
            self.participant.vars['bin_index_mine'] = 1
        elif self.participant.vars['productivity']>20 and self.participant.vars['productivity']<=30:
            self.participant.vars['bin_index_mine'] = 2
        elif self.participant.vars['productivity']>30 and self.participant.vars['productivity']<=40:
            self.participant.vars['bin_index_mine'] = 3
        elif self.participant.vars['productivity']>40 and self.participant.vars['productivity']<=50:
            self.participant.vars['bin_index_mine'] = 4
        elif self.participant.vars['productivity']>50 and self.participant.vars['productivity']<=60:
            self.participant.vars['bin_index_mine'] = 5
        elif self.participant.vars['productivity']>60 and self.participant.vars['productivity']<=70:
            self.participant.vars['bin_index_mine'] = 6
        elif self.participant.vars['productivity']>70 and self.participant.vars['productivity']<=80:
            self.participant.vars['bin_index_mine'] = 7
        elif self.participant.vars['productivity']>80 and self.participant.vars['productivity']<=90:
            self.participant.vars['bin_index_mine'] = 8
        elif self.participant.vars['productivity']>90 and self.participant.vars['productivity']<=100:
            self.participant.vars['bin_index_mine'] = 9

        
    

   

