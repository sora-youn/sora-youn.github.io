from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import numpy as np
import statistics
import pandas as pd
import math

author = 'S. Youn'

doc = """
        Experiment for testing Heidhues, Koszegi, and Strack (2018)
"""

import random
import time

class Constants(BaseConstants):
    name_in_url = 'SliderTask'
    players_per_group = None
    num_rounds = 1
    point_per_correct_slider = 1
    correct_upper_bound = 51
    correct_lower_bound = 49
    SimpleSpace = 5   
    ComplexSpace = 100

class Subsession(BaseSubsession):
    simple  = models.BooleanField()

    def creating_session(self):
        self.simple = self.session.config.get('simple')

        for p in self.get_players():
            if self.simple:
                p.StateSpace = Constants.SimpleSpace
            else:
                p.StateSpace = Constants.ComplexSpace

    def set_payoff_s(self):
        for p in self.get_players():
            p.set_payoff()

class Group(BaseGroup):
    pass

class Player(BasePlayer):

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

    StateSpace = models.FloatField()

    num_slider = models.FloatField()
    pct = models.FloatField()
    roundup_pct = models.FloatField()

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
        self.participant.vars['num_slider'] = 0

        for x in slider:
            if x <= Constants.correct_upper_bound :
                if x >= Constants.correct_lower_bound: 
                    self.participant.vars['num_slider'] = self.participant.vars['num_slider'] + 1
                else :
                    self.participant.vars['num_slider'] = self.participant.vars['num_slider'] + 0
            else : 
                self.participant.vars['num_slider'] = self.participant.vars['num_slider'] + 0

        self.num_slider = self.participant.vars['num_slider']   


        ## payoff from Part 1 = the number of correctly positioned sliders * point_per_correct_slider
        self.payoff = self.participant.vars['num_slider'] * Constants.point_per_correct_slider


        ## The performance of over 200 participants who completed the same slider task last year.
        PerformanceList = [ 0,
                            0,
                            0,
                            0,
                            1,
                            1,
                            2,
                            4,
                            6,
                            7,
                            7,
                            7,
                            7,
                            7,
                            8,
                            8,
                            8,
                            9,
                            9,
                            9,
                            9,
                            10,
                            11,
                            12,
                            14,
                            14,
                            14,
                            14,
                            15,
                            16,
                            16,
                            18,
                            18,
                            18,
                            18,
                            18,
                            18,
                            19,
                            19,
                            19,
                            19,
                            19,
                            20,
                            20,
                            20,
                            21,
                            21,
                            21,
                            21,
                            21,
                            21,
                            21,
                            21,
                            21,
                            22,
                            22,
                            22,
                            22,
                            22,
                            22,
                            22,
                            23,
                            23,
                            23,
                            23,
                            23,
                            24,
                            24,
                            24,
                            24,
                            24,
                            25,
                            25,
                            25,
                            25,
                            26,
                            26,
                            26,
                            26,
                            26,
                            27,
                            27,
                            27,
                            27,
                            27,
                            27,
                            27,
                            27,
                            28,
                            28,
                            28,
                            28,
                            28,
                            28,
                            28,
                            28,
                            28,
                            29,
                            29,
                            29,
                            29,
                            29,
                            29,
                            29,
                            29,
                            29,
                            30,
                            30,
                            30,
                            30,
                            30,
                            30,
                            30,
                            30,
                            30,
                            30,
                            30,
                            31,
                            31,
                            31,
                            31,
                            31,
                            31,
                            31,
                            31,
                            31,
                            32,
                            32,
                            32,
                            32,
                            32,
                            32,
                            32,
                            32,
                            32,
                            33,
                            33,
                            33,
                            33,
                            33,
                            33,
                            33,
                            33,
                            33,
                            33,
                            34,
                            34,
                            34,
                            34,
                            34,
                            35,
                            35,
                            35,
                            35,
                            35,
                            36,
                            36,
                            36,
                            36,
                            36,
                            36,
                            36,
                            36,
                            36,
                            37,
                            37,
                            37,
                            37,
                            38,
                            38,
                            38,
                            38,
                            39,
                            39,
                            39,
                            39,
                            39,
                            39,
                            39,
                            39,
                            40,
                            40,
                            40,
                            40,
                            40,
                            41,
                            41,
                            41,
                            42,
                            42,
                            42,
                            43,
                            43,
                            43,
                            43,
                            43,
                            43,
                            43,
                            44,
                            44,
                            44,
                            44,
                            44,
                            44,
                            44,
                            45,
                            45,
                            46,
                            46,
                            46,
                            47,
                            49,
                            50,
                            50,
                            50,
                            52,
                            52,
                            53,
                            54,
                            55,
                            56,
                            56]

        PerformanceList.append(self.participant.vars['num_slider'])


        ##################################################################
        ## Find the subject's percentile
        data = {'performance': PerformanceList}  
        df = pd.DataFrame(data)  
        df['Percentile Rank'] = df.performance.rank(pct = True)
        print(df)  

        self.participant.vars['pct'] = df['Percentile Rank'].iloc[222] # the subject = the last row 
        self.participant.vars['pct'] = self.participant.vars['pct'] * 100
        self.participant.vars['roundup_pct'] = math.ceil(self.participant.vars['pct'])

        self.pct = self.participant.vars['pct']
        self.roundup_pct = self.participant.vars['roundup_pct']


        
        ## individual productivity

        # state space = {10, 30, 50, 70, 90}
        if self.StateSpace == Constants.SimpleSpace:

            if self.participant.vars['roundup_pct'] < 20 :
                self.participant.vars['my_prod']  = 10

            elif self.participant.vars['roundup_pct'] >= 20 and self.participant.vars['roundup_pct'] < 40 :
                self.participant.vars['my_prod']  = 30      

            elif self.participant.vars['roundup_pct'] >= 40 and self.participant.vars['roundup_pct'] < 60 :
                self.participant.vars['my_prod']  = 50    

            elif self.participant.vars['roundup_pct'] >= 60 and self.participant.vars['roundup_pct'] < 80:
                self.participant.vars['my_prod']  = 70    

            else :
                self.participant.vars['roundup_pct']  = 90    

        # state space = {1,2,3,...,98,99,100}
        else : 
            self.participant.vars['my_prod']  = self.participant.vars['roundup_pct']   

