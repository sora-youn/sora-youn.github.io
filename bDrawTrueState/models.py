from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import pandas as pd
import numpy as np
import statistics

author = 'S. Youn'

doc = """
        Experiment for testing Heidhues, Koszegi, and Strack (2018)
"""

import random
import time

class Constants(BaseConstants):
    name_in_url = 'DrawTrueState'
    players_per_group = 2
    num_rounds = 1
    
class Subsession(BaseSubsession):

    def creating_session(self):
        self.group_randomly(fixed_id_in_group=True)
        print(self.get_group_matrix())

class Group(BaseGroup):

    def set_fundamental(self):
        all_players = self.get_players()
        print(all_players)

        player1 = self.get_player_by_id(1)
        player2 = self.get_player_by_id(2)

        player1.participant.vars['teammate_prod'] = player2.participant.vars['my_prod']
        player2.participant.vars['teammate_prod'] = player1.participant.vars['my_prod']

class Player(BasePlayer):
    pass

    


        



















    


    

