from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from scipy.stats import bernoulli

class Part3_Instruction(Page):
    def is_displayed(self):
        if self.round_number == 1:
            return True
        else:
            return self.participant.vars["fail"]

    def vars_for_template(self):
        return dict(
            num_game_round = Constants.num_game_round,
            prize = Constants.prize,
            max_lt = Constants.max_lt
        )

class Part3_CQ(Page):
    form_model = 'player'
    form_fields = [
        'part3_cq1_a',
        'part3_cq1_b',
        'part3_cq2_a',
        'part3_cq2_b',
        'part3_cq3',
        'part3_cq4',
        'part3_cq5'
    ]    

    def before_next_page(self):
        if [self.player.part3_cq1_a, self.player.part3_cq1_b] == Constants.ans_part3_cq1 and [self.player.part3_cq2_a, self.player.part3_cq2_b] == Constants.ans_part3_cq2 and self.player.part3_cq3 == Constants.ans_part3_cq3 and self.player.part3_cq4 == Constants.ans_part3_cq4 and self.player.part3_cq5 == Constants.ans_part3_cq5:
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

class Part3_Task(Page):
    form_model = 'player'
    form_fields = [
        'guess_mine',
        'guess_teammate',
        'check_DecisionSlider',
        'draw_urn1',
    ]

    def error_message(self, value):
        if value["check_DecisionSlider"] != True:
            return 'Please use the slider to make a decision.'

    def before_next_page(self):
        self.player.set_payoff()

    def vars_for_template(self):
        
        return dict(
            # player_in_previous_rounds=self.player.in_previous_rounds(),
            player_in_previous_rounds=self.player.in_rounds(2,self.subsession.round_number-1),
            game_round_number = self.subsession.round_number - 1,
            num_game_round = Constants.num_game_round
        )

    def is_displayed(self):
        return self.round_number >= Constants.num_attention_check_tries


class Part3_Result(Page):
    def vars_for_template(self):
        return dict(
            player_in_previous_rounds=self.player.in_previous_rounds(),
            round_number = self.subsession.round_number - 1,
            draw_urn1 = self.player.draw_urn1,
            draw_urn2 = self.player.draw_urn2,
            num_redballs = self.player.num_redballs,
            num_LTs_Awarded = self.player.num_LTs_Awareded,
            num_game_round = Constants.num_game_round
        )

    def is_displayed(self):
        return self.round_number >= Constants.num_attention_check_tries


# the coreography of pages
page_sequence = [
                    Part3_Instruction,
                    Part3_CQ,
                    SecondChance,
                    FailedAttentionCheck,
                    Part3_Task,
                    Part3_Result
]
