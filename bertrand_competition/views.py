# -*- coding: utf-8 -*-
import bertrand_competition.forms as forms
from bertrand_competition.utilities import Page, MatchWaitPage, SubsessionWaitPage
from ptree.common import currency


class Introduction(Page):

    template_name = 'bertrand_competition/Introduction.html'

    def variables_for_template(self):
        return {
            'minimum_price': currency(self.treatment.minimum_price),
            'maximum_price': currency(self.treatment.maximum_price)
        }


class Compete(Page):

    template_name = 'bertrand_competition/Compete.html'

    def get_form_class(self):
        return forms.PriceForm

class ResultsWaitPage(MatchWaitPage):

    def action(self):
        for p in self.match.participants():
            p.set_payoff()

class Results(Page):

    template_name = 'bertrand_competition/Results.html'

    def variables_for_template(self):

        return {
            'payoff': currency(self.participant.payoff),
            'is_winner': self.participant.is_winner,
            'price': currency(self.participant.price),
            'other_price': currency(self.participant.other_participant().price),
            'equal_price': self.participant.price == self.participant.other_participant().price,
        }

def pages():
    return [
        Introduction,
        Compete,
        ResultsWaitPage,
        Results
    ]