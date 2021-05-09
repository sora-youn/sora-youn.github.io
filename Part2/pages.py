from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Part2_Instruction(Page):
    def is_displayed(self):
        if self.round_number == 1:
            return True
        else:
            return self.participant.vars["fail"]

class Part2_CQ(Page):
    form_model = 'player'
    form_fields = [
        'part2_cq1',
        'part2_cq2_bin1_mine',
        'part2_cq2_bin2_mine',
        'part2_cq2_bin3_mine',
        'part2_cq2_bin4_mine',
        'part2_cq2_bin5_mine',
        'part2_cq2_bin6_mine',
        'part2_cq2_bin7_mine',
        'part2_cq2_bin8_mine',
        'part2_cq2_bin9_mine',
        'part2_cq2_bin10_mine',
        'part2_cq2_bin1_teammate',
        'part2_cq2_bin2_teammate',
        'part2_cq2_bin3_teammate',
        'part2_cq2_bin4_teammate',
        'part2_cq2_bin5_teammate',
        'part2_cq2_bin6_teammate',
        'part2_cq2_bin7_teammate',
        'part2_cq2_bin8_teammate',
        'part2_cq2_bin9_teammate',
        'part2_cq2_bin10_teammate',
        'part2_cq3',
        ]

    def error_message(self, values):
        if values['part2_cq2_bin1_mine'] + values['part2_cq2_bin2_mine'] + values['part2_cq2_bin3_mine'] + values['part2_cq2_bin4_mine'] + values['part2_cq2_bin5_mine'] + values['part2_cq2_bin6_mine'] + values['part2_cq2_bin7_mine'] + values['part2_cq2_bin8_mine'] + values['part2_cq2_bin9_mine'] + values['part2_cq2_bin10_mine'] != 100 or values['part2_cq2_bin1_teammate'] + values['part2_cq2_bin2_teammate'] + values['part2_cq2_bin3_teammate'] + values['part2_cq2_bin4_teammate'] + values['part2_cq2_bin5_teammate'] + values['part2_cq2_bin6_teammate'] + values['part2_cq2_bin7_teammate'] + values['part2_cq2_bin8_teammate'] + values['part2_cq2_bin9_teammate'] + values['part2_cq2_bin10_teammate'] != 100  :
            return 'You must distribute exactly 100 tokens for each estimate.'

    def before_next_page(self):
        if self.player.part2_cq1 == Constants.ans_part2_cq1 and [self.player.part2_cq2_bin1_mine, self.player.part2_cq2_bin2_mine, self.player.part2_cq2_bin3_mine, self.player.part2_cq2_bin4_mine, self.player.part2_cq2_bin5_mine, self.player.part2_cq2_bin6_mine, self.player.part2_cq2_bin7_mine, self.player.part2_cq2_bin8_mine, self.player.part2_cq2_bin9_mine, self.player.part2_cq2_bin10_mine] == Constants.ans_part2_cq2_mine and [self.player.part2_cq2_bin1_teammate, self.player.part2_cq2_bin2_teammate, self.player.part2_cq2_bin3_teammate, self.player.part2_cq2_bin4_teammate, self.player.part2_cq2_bin5_teammate, self.player.part2_cq2_bin6_teammate, self.player.part2_cq2_bin7_teammate, self.player.part2_cq2_bin8_teammate, self.player.part2_cq2_bin9_teammate, self.player.part2_cq2_bin10_teammate] == Constants.ans_part2_cq2_teammate :
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

class Part2_Task(Page):
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

    def is_displayed(self):
        return self.round_number >= Constants.num_attention_check_tries

    def before_next_page(self):
        self.player.set_payoff()










# the coreography of pages
page_sequence = [
                    Part2_Instruction,
                    Part2_CQ,
                    SecondChance,
                    FailedAttentionCheck,
                    Part2_Task
]
