from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from scipy.stats import bernoulli


class PaperInstructions(Page):
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
        'check_GuessInput',
    ]

    def error_message(self, value):
        if value["check_DecisionSlider"] != True:
            return 'Please use the slider to make a decision.'

        if value["check_GuessInput"] != True:
            return 'Please confirm your final guess.'        

    def before_next_page(self):
        self.player.set_payoff()

    def vars_for_template(self):
        
        return dict(
            player_in_previous_rounds = self.player.in_previous_rounds(),
            game_round_number = self.player.round_number,
            num_game_round = Constants.num_rounds
        )

    def is_displayed(self):
        return self.round_number <= Constants.num_rounds 


class Part3_Result(Page):
    def vars_for_template(self):
        return dict(
            player_in_previous_rounds = self.player.in_previous_rounds(),
            round_number = self.subsession.round_number,
            draw_urn1 = self.player.draw_urn1,
            draw_urn2 = self.player.draw_urn2,
            num_game_round = Constants.num_rounds,
            points = self.player.points,
        )

# the coreography of pages
page_sequence = [
                    PaperInstructions,
                    Part3_Task,
                    Part3_Result,

]    
