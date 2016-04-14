# -*- coding: utf-8 -*-
"""Models for Public Goods."""

# <standard imports>
from __future__ import division
from otree.db import models
from otree.constants import BaseConstants
from otree.models import BaseSubsession, BaseGroup, BasePlayer
from otree.common import Currency
# </standard imports>

doc = """
This is a one-period public goods game with 3 players. Assignment to groups is
random.
"""


source_code = "https://github.com/oTree-org/oTree/tree/master/public_goods"


bibliography = ()


links = {
    "Wikipedia": {
        "Public Goods Game": "https://en.wikipedia.org/wiki/Public_goods_game"
    }
}


keywords = ("Public Goods",)


class Constants(BaseConstants):
    """Constants for Public Goods."""

    name_in_url = 'public_goods'
    players_per_group = 3
    num_rounds = 1

    # Amount allocated to each player
    endowment = Currency(10)
    efficiency_factor = 1.8
    base_points = Currency(10)


class Subsession(BaseSubsession):
    """Subsession for Public Goods."""

    pass


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
        min=0, max=Constants.endowment,
        doc="""The amount contributed by the player""",
    )

    question = models.CurrencyField()

    contribution_back_0 = models.CurrencyField(
        min=0, max=Constants.endowment,
    )

    contribution_back_1 = models.CurrencyField(
        min=0, max=Constants.endowment,
    )

    contribution_back_2 = models.CurrencyField(
        min=0, max=Constants.endowment,
    )

    contribution_back_3 = models.CurrencyField(
        min=0, max=Constants.endowment,
    )

    contribution_back_4 = models.CurrencyField(
        min=0, max=Constants.endowment,
    )

    contribution_back_5 = models.CurrencyField(
        min=0, max=Constants.endowment,
    )

    contribution_back_6 = models.CurrencyField(
        min=0, max=Constants.endowment,
    )

    contribution_back_7 = models.CurrencyField(
        min=0, max=Constants.endowment,
    )

    contribution_back_8 = models.CurrencyField(
        min=0, max=Constants.endowment,
    )

    contribution_back_9 = models.CurrencyField(
        min=0, max=Constants.endowment,
    )

    contribution_back_10 = models.CurrencyField(
        min=0, max=Constants.endowment,
    )

    def vars_for_template(self):
        """Return variables available for template."""
        return {
            'contribution_back_0_label': 'If the other group members make an \
average contribution of 0:',
            'contribution_back_1_label': 'If the other group members make an \
average contribution of 1:',
            'contribution_back_2_label': 'If the other group members make an \
average contribution of 2:',
            'contribution_back_3_label': 'If the other group members make an \
average contribution of 3:',
            'contribution_back_4_label': 'If the other group members make an \
average contribution of 4:',
            'contribution_back_5_label': 'If the other group members make an \
average contribution of 5:',
            'contribution_back_6_label': 'If the other group members make an \
average contribution of 6:',
            'contribution_back_7_label': 'If the other group members make an \
average contribution of 7:',
            'contribution_back_8_label': 'If the other group members make an \
average contribution of 8:',
            'contribution_back_9_label': 'If the other group members make an \
average contribution of 9:',
            'contribution_back_10:_label': 'If the other group members make an \
average contribution of 10:',
        }
