from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import numpy as np

class Intro(Page):
    pass

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

    def vars_for_template(self):
        return dict(
            correct_upper_bound = Constants.correct_upper_bound,
            correct_lower_bound = Constants.correct_lower_bound
        )       

    def before_next_page(self):
        self.player.set_payoff()

class SliderCompletion(Page):
    pass

class SliderStart(Page):
    pass

# the coreography of pages
page_sequence = [   
                    Intro,
                    SliderStart,
                    Part1_Task,
                    SliderCompletion,
                ]
