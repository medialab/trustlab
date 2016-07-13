# -*- coding: utf-8 -*-
"""Views for Trust game."""

from __future__ import division
from ._builtin import Page
from . import models
from .models import Constants
from django.utils.translation import ugettext_lazy as _


def vars_for_all_templates(self):
    """Provide global template variables."""
    return {
        'instructions': 'trust/Instructions.html',
        'total_q': 1,
        'lang': self.session.vars['lang']
    }


class ExperimentIntroduction(Page):
    """
    Page introducing the entire experiment.

    Assumes this is the first test.
    """

    pass


class GamesIntroduction(Page):
    """Page introducing the games. Assumes this is the first test."""

    pass


class Introduction(Page):
    """Page introducing the Trust game."""

    template_name = 'global/Introduction.html'
    form_model = models.Player
    form_fields = ['total_time']

    def vars_for_template(self):
        """Local variables for the template."""
        return {'amount_allocated': Constants.amount_allocated}


class Simulation(Page):
    """Simulation page."""

    template_name = 'trust/Simulation.html'

    def vars_for_template(self):
        max = {'fr': 10, 'kr': 10000}
        return {
            'max': max[self.session.vars['lang']]
        }


class Send(Page):
    """Page where Player 1 sends money."""

    form_model = models.Player
    form_fields = ['sent_amount']

    def vars_for_template(self):
        """Return variables for use in template."""
        return {
            'fr': {
                'amount_allocated': Constants.amount_allocated,
                'sent_amount_label': _(u'Please enter a number from 0 to 10')
            },
            'kr': {
                'amount_allocated': Constants.amount_allocated,
                'sent_amount_label': _(u'Please enter a number from 0 to 10.000')
            }
        }

    def is_displayed(self):
        """Display rule stating 'Send' is displayed for Player 1 only."""
        return self.player.treatment()[:1] == 'A'


class SendBack(Page):
    """Page where Player 2 sends mony in return for possible P1 grants."""

    form_model = models.Player
    form_fields = [
        'sent_back_amount_0',
        'sent_back_amount_1',
        'sent_back_amount_2',
        'sent_back_amount_3',
        'sent_back_amount_4',
        'sent_back_amount_5',
        'sent_back_amount_6',
        'sent_back_amount_7',
        'sent_back_amount_8',
        'sent_back_amount_9',
        'sent_back_amount_10',
    ]

    def vars_for_template(self):
        """Return variables for use in template."""
        return {
            'fr': {
                'sent_back_amount_0_label': _(
                    u'If Participant A sends you 0€ (you receive 0€ × 3 = 0€)'
                ),
                'sent_back_amount_1_label': _(
                    u'If Participant A sends you 1€ (you receive 1€ × 3 = 3€)'
                ),
                'sent_back_amount_2_label': _(
                    u'If Participant A sends you 2€ (you receive 2€ × 3 = 6€)'
                ),
                'sent_back_amount_3_label': _(
                    u'If Participant A sends you 3€ (you receive 3€ × 3 = 9€)'
                ),
                'sent_back_amount_4_label': _(
                    u'If Participant A sends you 4€ (you receive 4€ × 3 = 12€)'
                ),
                'sent_back_amount_5_label': _(
                    u'If Participant A sends you 5€ (you receive 5€ × 3 = 15€)'
                ),
                'sent_back_amount_6_label': _(
                    u'If Participant A sends you 6€ (you receive 6€ × 3 = 18€)'
                ),
                'sent_back_amount_7_label': _(
                    u'If Participant A sends you 7€ (you receive 7€ × 3 = 21€)'
                ),
                'sent_back_amount_8_label': _(
                    u'If Participant A sends you 8€ (you receive 8€ × 3 = 24€)'
                ),
                'sent_back_amount_9_label': _(
                    u'If Participant A sends you 9€ (you receive 9€ × 3 = 27€)'
                ),
                'sent_back_amount_10_label': _(
                    u'If Participant A sends you 10€ (you receive 10€ ×3 = 30€)'
                ),
            },

            'kr': {
                'sent_back_amount_0_label': _(
                    u'If Participant A sends you 0 Won (you receive 0 Won × 3 = 0 Won)'
                ),
                'sent_back_amount_1_label': _(
                    u'If Participant A sends you 1.000 Won (you receive 1.000 Won × 3 = 3.000 Won)'
                ),
                'sent_back_amount_2_label': _(
                    u'If Participant A sends you 2 Won (you receive 2.000 Won × 3 = 6.000 Won)'
                ),
                'sent_back_amount_3_label': _(
                    u'If Participant A sends you 3.000 Won (you receive 3.000 Won × 3 = 9.000 Won)'
                ),
                'sent_back_amount_4_label': _(
                    u'If Participant A sends you 4.000 Won (you receive 4.000 Won × 3 = 12.000 Won)'
                ),
                'sent_back_amount_5_label': _(
                    u'If Participant A sends you 5.000 Won (you receive 5.000 Won × 3 = 15.000 Won)'
                ),
                'sent_back_amount_6_label': _(
                    u'If Participant A sends you 6.000 Won (you receive 6.000 Won × 3 = 18.000 Won)'
                ),
                'sent_back_amount_7_label': _(
                    u'If Participant A sends you 7.000 Won (you receive 7.000 Won × 3 = 21.000 Won)'
                ),
                'sent_back_amount_8_label': _(
                    u'If Participant A sends you 8.000 Won (you receive 8.000 Won × 3 = 24.000 Won)'
                ),
                'sent_back_amount_9_label': _(
                    u'If Participant A sends you 9.000 Won (you receive 9.000 Won × 3 = 27.000 Won)'
                ),
                'sent_back_amount_10_label': _(
                    u'If Participant A sends you 10.000 Won (you receive 10.000 Won ×3 = 30.000 Won)'
                ),
            }
        }

    def is_displayed(self):
        """Display rule stating 'SendBack' appears for Player B only."""
        return self.player.treatment()[:1] == 'B'


class EndGame(Page):
    """End of the game."""

    form_model = models.Player
    form_fields = ['total_time']

    def vars_for_template(self):
        """Make data available in template."""
        return {'start_time': self.player.total_time}


page_sequence = [
    ExperimentIntroduction,
    GamesIntroduction,
    Introduction,
    Simulation,
    Send,
    SendBack,
    EndGame
]
