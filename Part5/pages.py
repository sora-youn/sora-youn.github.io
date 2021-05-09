from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Part5_Instruction(Page):
    form_model = 'player'
    form_fields = ['practice'] 

    # values that are to be displayed (dictionary)
    def vars_for_template(self):
        # retrieve values from constants and store them in a dictionary
        return{
        'f1':Constants.f1,
        'f2':Constants.f2,
        'f3':Constants.f3,
        'f4':Constants.f4
        }

class Part5_Task(Page):
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

    # before moving to next page, compute payoffs (avoids that with refreshing payoffs are recomputed again)
    def before_next_page(self):
        # built-in method 
        self.player.set_payoff()# see in models in Player class


# the coreography of pages
page_sequence = [
                    Part5_Instruction,
                    Part5_Task
]
