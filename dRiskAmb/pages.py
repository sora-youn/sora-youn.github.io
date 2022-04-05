from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Instruction(Page):
    # values that are to be displayed (dictionary)
    def vars_for_template(self):
        # retrieve values from constants and store them in a dictionary
        return{
        'f1':Constants.f1,
        'f2':Constants.f2,
        'f3':Constants.f3,
        'f4':Constants.f4
        }

class Risk_Task(Page):
# which forms are needed from class player
    form_model = 'player'
    form_fields = ['risk'] 
    
    # values that are to be displayed (dictionary)
    def vars_for_template(self):
        # retrieve values from constants and store them in a dictionary
        return{
        'f1':Constants.f1,
        'f2':Constants.f2,
        'f3':Constants.f3,
        'f4':Constants.f4
        }

class Amb_Task(Page):
# which forms are needed from class player
    form_model = 'player'
    form_fields = ['ambig'] 

    # values that are to be displayed (dictionary)
    def vars_for_template(self):
        # retrieve values from constants and store them in a dictionary
        return{
        'g0':Constants.g0,    
        'g1':Constants.g1,
        'g2':Constants.g2,
        'g3':Constants.g3,
        'g4':Constants.g4,
        'g5':Constants.g5,
        'g6':Constants.g6,
        'g7':Constants.g7,
        'g8':Constants.g8,
        'g9':Constants.g9,
        'g10':Constants.g10,
        'g11':Constants.g11,
        'g12':Constants.g12,
        'g13':Constants.g13,
        'g14':Constants.g14,
        'g15':Constants.g15,
        'g16':Constants.g16,
        'g17':Constants.g17,
        'g18':Constants.g18,
        'g19':Constants.g19,
        'g20':Constants.g20,
        }

    # before moving to next page, compute payoffs (avoids that with refreshing payoffs are recomputed again)
    def before_next_page(self):
        # built-in method 
        self.player.set_payoff()# see in models in Player class


# the coreography of pages
page_sequence = [
                    Instruction,
                    Risk_Task,
                    Amb_Task,
]
