from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Part6_Instructions(Page):
    form_model = 'player'
    form_fields = ['practice'] # the demo MPL

    # values that are to be displayed (dictionary)
    def vars_for_template(self):
        # retrieve values from constants and store them in a dictionary
        return{
        'f1':Constants.f1,
        'f2':Constants.f2,
        'f3':Constants.f3,
        'f4':Constants.f4
        }

class Part6_Task(Page):
# which forms are needed from class player
    form_model = 'player'
    form_fields = ['ambig1','ambig2','ambig3','ambig4','ambig5','ambig6','ambig7','ambig8','ambig9','ambig10','ambig11','ambig12','ambig13','ambig14','ambig15','ambig16','ambig17','ambig18','ambig19','ambig20'] 

    # values that are to be displayed (dictionary)
    def vars_for_template(self):
        # retrieve values from constants and store them in a dictionary
        return{
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




# the coreography of pages
page_sequence = [
                    Part6_Instructions,
                    Part6_Task
]
