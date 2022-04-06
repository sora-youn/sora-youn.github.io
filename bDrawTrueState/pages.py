from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class MyWaitPage(WaitPage):
    after_all_players_arrive = 'set_fundamental'

class next(Page):

    def before_next_page(self):
        self.player.set_payoff()
# the coreography of pages
page_sequence = [   MyWaitPage,
                    next
]
