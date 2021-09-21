from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class ExitSurvey(Page):
# forms to retrieve individual information
    form_model = 'player'
    form_fields = ['comment','like','enjoy','sex','age']# plyaer.comment, player.like, ...

class Finish(Page):

    def vars_for_template(self):
        # retrieve values from constants and store them in a dictionary
        return{
        'final_payout':self.participant.payoff_plus_participation_fee()
        }

# the coreography of pages
page_sequence = [
                    ExitSurvey,
                    Finish
                ]
