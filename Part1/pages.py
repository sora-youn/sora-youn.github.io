from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Intro_Part1_Instruction(Page):
    def is_displayed(self):
        if self.round_number == 1:
            return True
        else:
            return self.participant.vars["fail"]


class Part1_CQ(Page):            
    form_model = 'player'
    form_fields = [
        'part1_cq1',
        'part1_cq2',
        'part1_cq3',
        ]

    def before_next_page(self):
        if self.player.part1_cq1 == Constants.ans_part1_cq1 and self.player.part1_cq2 == Constants.ans_part1_cq2 and self.player.part1_cq3 == Constants.ans_part1_cq3 :
            self.participant.vars["fail"] = False
        else :
            self.participant.vars["fail"] = True

    def is_displayed(self):
        if self.round_number == 1:
            return True
        else:
            return self.participant.vars["fail"]    


class SecondChance(Page):
    def is_displayed(self):
        if self.round_number == 1:
            return self.participant.vars["fail"]
        else:
            return False

class FailedAttentionCheck(Page):
    def is_displayed(self):
        if self.round_number > 1:
            return self.participant.vars["fail"]
        else:
            return False


class Part1_Task(Page):
    form_model = 'player'
    form_fields = [
        'slider1',
        'slider2',
        'slider3',
        'slider4',
        'slider5',
        'slider6',
        'slider7',
        'slider8',
        'slider9',
        'slider10',
        'slider11',
        'slider12',
        'slider13',
        'slider14',
        'slider15',
        'slider16',
        'slider17',
        'slider18',
        'slider19',
        'slider20',
        'slider1',
        'slider2',
        'slider3',
        'slider4',
        'slider5',
        'slider6',
        'slider7',
        'slider8',
        'slider9',
        'slider10',
        'slider11',
        'slider12',
        'slider13',
        'slider14',
        'slider15',
        'slider16',
        'slider17',
        'slider18',
        'slider19',
        'slider20',
        'slider21',
        'slider22',
        'slider23',
        'slider24',
        'slider25',
        'slider26',
        'slider27',
        'slider28',
        'slider29',
        'slider30',
        'slider31',
        'slider32',
        'slider33',
        'slider34',
        'slider35',
        'slider36',
        'slider37',
        'slider38',
        'slider39',
        'slider40',
        'slider41',
        'slider42',
        'slider43',
        'slider44',
        'slider45',
        'slider46',
        'slider47',
        'slider48',
        'slider49',
        'slider50',
        'slider51',
        'slider52',
        'slider53',
        'slider54',
        'slider55',
        'slider56',
        'slider57',
        'slider58',
        'slider59',
        'slider60',
        'slider61',
        'slider62',
        'slider63',
        'slider64',
        'slider65',
        'slider66',
        'slider67',
        'slider68',
        'slider69',
        'slider70',
        'slider71',
        'slider72',
        'slider73',
        'slider74',
        'slider75',
        'slider76',
        'slider77',
        'slider78',
        'slider79',
        'slider80',
        'slider81',
        'slider82',
        'slider83',
        'slider84',
        'slider85',
        'slider86',
        'slider87',
        'slider88',
        'slider89',
        'slider90',
        'slider91',
        'slider92',
        'slider93',
        'slider94',
        'slider95',
        'slider96',
        'slider97',
        'slider98',
        'slider99',
        'slider100',
    ]
    
    timeout_seconds = 300   

    def before_next_page(self):
        self.player.set_payoff()

    def is_displayed(self):
        return self.round_number >= Constants.num_attention_check_tries and self.participant.vars["fail"] == False   


class Part2_Begins_Soon(WaitPage):
    after_all_players_arrive = 'set_fundamental'

    def is_displayed(self):
        return self.round_number >= Constants.num_attention_check_tries


# the coreography of pages
page_sequence = [
                    Intro_Part1_Instruction,
                    Part1_CQ,
                    SecondChance,
                    FailedAttentionCheck,
                    Part1_Task,
                    Part2_Begins_Soon
                ]
