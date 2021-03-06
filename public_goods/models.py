# -*- coding: utf-8 -*-
"""Models for Public Goods."""

# <standard imports>
from __future__ import division
from otree.db import models
from otree.constants import BaseConstants
from otree.models import BaseSubsession, BaseGroup, BasePlayer
from otree.common import Currency
from django.utils.translation import get_language
# </standard imports>

doc = """
This is a one-period public goods game with 3 players. Assignment to groups is
random. Trustlab's version uses the Strategic Method.
"""


source_code = "https://github.com/oTree-org/oTree/tree/master/public_goods"


bibliography = ()


links = {
    "Wikipedia": {
        "Public Goods Game": "https://en.wikipedia.org/wiki/Public_goods_game"
    }
}


keywords = ("Public Goods",)

allocated_amount = get_language() == 'ko' and 12000 or 10


class Constants(BaseConstants):
    """Constants for Public Goods."""

    name_in_url = 'public_goods'
    players_per_group = None
    num_rounds = 1

    # Amount allocated to each player
    endowment = Currency(10)
    efficiency_factor = 1.6
    base_points = Currency(10)


class Subsession(BaseSubsession):
    """Subsession for Public Goods."""

    def before_session_starts(self):
        """Set treatment of the game (see settings.py) as global var."""
        if 'treatment' in self.session.config:
            self.session.vars['treatment'] = self.session.config['treatment']
        self.session.vars['lang'] = get_language()


class Group(BaseGroup):
    """Group for Public Goods."""

    total_contribution = models.CurrencyField()

    individual_share = models.CurrencyField()

    def set_payoffs(self):
        """Set payoffs (used by test bot)."""
        self.total_contribution = (
            sum([p.contribution for p in self.get_players()])
        )
        self.individual_share = (
            self.total_contribution *
            Constants.efficiency_factor / Constants.players_per_group
        )
        for p in self.get_players():
            p.payoff = (
                (Constants.endowment - p.contribution) +
                self.individual_share + Constants.base_points
            )


class Player(BasePlayer):
    """Player for Public Goods."""

    contribution = models.CurrencyField(
        min=0, max=allocated_amount,
        doc="""The amount contributed by the player""",
    )

    question = models.CurrencyField()

    contribution_back_0 = models.CurrencyField(
        min=0, max=allocated_amount,
    )

    contribution_back_1 = models.CurrencyField(
        min=0, max=allocated_amount,
    )

    contribution_back_2 = models.CurrencyField(
        min=0, max=allocated_amount,
    )

    contribution_back_3 = models.CurrencyField(
        min=0, max=allocated_amount,
    )

    contribution_back_4 = models.CurrencyField(
        min=0, max=allocated_amount,
    )

    contribution_back_5 = models.CurrencyField(
        min=0, max=allocated_amount,
    )

    contribution_back_6 = models.CurrencyField(
        min=0, max=allocated_amount,
    )

    contribution_back_7 = models.CurrencyField(
        min=0, max=allocated_amount,
    )

    contribution_back_8 = models.CurrencyField(
        min=0, max=allocated_amount,
    )

    contribution_back_9 = models.CurrencyField(
        min=0, max=allocated_amount,
    )

    contribution_back_10 = models.CurrencyField(
        min=0, max=allocated_amount,
    )
