from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from scipy.stats import bernoulli

class Part3_Instruction(Page):
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
    
    def vars_for_template(self):
        return dict(
            num_game_round = Constants.num_rounds-1,
            prize = Constants.prize,
            max_lt = Constants.max_lt,
            subcontractor = Constants.subcontractor,
            urn2_green = round(Constants.subcontractor/2),
            urn2_black = round(100-Constants.subcontractor/2)
        )

    def is_displayed(self):
        if self.round_number == 1:
            return True

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
            player_in_previous_rounds = self.player.in_previous_rounds(),
            game_round_number = self.player.round_number,
            num_game_round = Constants.num_rounds-1 
        )

    def is_displayed(self):
        return self.round_number <= 50


class Part3_Result(Page):
    def vars_for_template(self):
        return dict(
            player_in_previous_rounds = self.player.in_previous_rounds(),
            round_number = self.subsession.round_number,
            draw_urn1 = self.player.draw_urn1,
            draw_urn2 = self.player.draw_urn2,
            num_Gballs = self.player.num_Gballs,
            num_LTs_Awarded = self.player.num_LTs_Awareded,
            num_game_round = Constants.num_rounds-1
        )

    def is_displayed(self):
        return self.round_number <= 50

class Part3_Summary(Page):
    def vars_for_template(self):
        return dict(
            player_in_previous_rounds = self.player.in_previous_rounds(),
            round_number = self.subsession.round_number,
            draw_urn1 = self.player.draw_urn1,
            draw_urn2 = self.player.draw_urn2,
            num_Gballs = self.player.num_Gballs,
            num_LTs_Awarded = self.player.num_LTs_Awareded,
            num_game_round = Constants.num_rounds-1
        )

    def is_displayed(self):
        return self.round_number ==51 

# the coreography of pages
page_sequence = [
                    Part3_Instruction,
                    Part3_Task,
                    Part3_Result,
                    Part3_Summary,
]    
