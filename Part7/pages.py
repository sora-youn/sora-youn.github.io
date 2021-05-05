from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class ExitSurvey(Page):
# forms to retrieve individual information
    form_model = 'player'
    form_fields = ['comment','like','sex','age']# plyaer.comment, player.like, ...

    # before moving to next page, compute payoffs (avoids that with refreshing payoffs are recomputed again)
    def before_next_page(self):
        # built-in method 
        self.player.set_payoffs_slider()# see in models in Player class



# the coreography of pages
page_sequence = [
                    ExitSurvey
                ]
