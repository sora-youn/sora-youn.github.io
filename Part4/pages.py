from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Part4_Instruction(Page):
    def is_displayed(self):
        if self.round_number == 1:
            return True
        else:
            return self.participant.vars["fail"]

class Part4_Task(Page):
# forms to retrieve individual information
    form_model = 'player'
    form_fields = [
        'bin1_mine',
        'bin2_mine',
        'bin3_mine',
        'bin4_mine',
        'bin5_mine',
        'bin6_mine',
        'bin7_mine',
        'bin8_mine',
        'bin9_mine',
        'bin10_mine',
        'bin1_teammate',
        'bin2_teammate',
        'bin3_teammate',
        'bin4_teammate',
        'bin5_teammate',
        'bin6_teammate',
        'bin7_teammate',
        'bin8_teammate',
        'bin9_teammate',
        'bin10_teammate'
    ]

    def error_message(self, values):
        if values['bin1_mine'] + values['bin2_mine'] + values['bin3_mine'] + values['bin4_mine'] + values['bin5_mine'] + values['bin6_mine'] + values['bin7_mine'] + values['bin8_mine'] + values['bin9_mine'] + values['bin10_mine'] != 100 or values['bin1_teammate'] + values['bin2_teammate'] + values['bin3_teammate'] + values['bin4_teammate'] + values['bin5_teammate'] + values['bin6_teammate'] + values['bin7_teammate'] + values['bin8_teammate'] + values['bin9_teammate'] + values['bin10_teammate'] != 100  :
            return 'The numbers in each column must add up to 100'

    def before_next_page(self):
        self.player.set_payoff()

# the coreography of pages
page_sequence = [
                    Part4_Instruction,
                    Part4_Task
]
