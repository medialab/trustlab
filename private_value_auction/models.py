# -*- coding: utf-8 -*-
"""Documentation at https://github.com/wickens/django-ptree-docs/wiki"""

from ptree.db import models
import ptree.models
from ptree.common import currency
import random

doc = """
In Private Value Auction Game. There are two participants anonymously paired. Each of the participants will submit a
bid for a prize being sold in an auction. The winner is the participant with the highest bid value.

<p>Source code <a href="https://github.com/wickens/ptree_library/tree/master/private_value_auction">here</a></p>
"""


class Subsession(ptree.models.BaseSubsession):

    name_in_url = 'private_value_auction'

    def choose_winner(self):
        highest_bid = max(p.bid_amount for p in self.participants())
        # could be a tie
        participants_with_highest_bid = [p for p in self.participants() if p.bid_amount == highest_bid]
        random_highest_bidder = random.choice(participants_with_highest_bid)
        random_highest_bidder.is_winner = True


class Treatment(ptree.models.BaseTreatment):
    subsession = models.ForeignKey(Subsession)

    price_value = models.PositiveIntegerField(
        null=True,
        doc="""
        Price value of the prize being sold in the auction
        """
    )


class Match(ptree.models.BaseMatch):

    treatment = models.ForeignKey(Treatment)
    subsession = models.ForeignKey(Subsession)

    participants_per_match = 1

    def bid_choices(self):
        """Range of allowed bid values"""
        return range(0, self.treatment.price_value + 1, 5)

    def get_bid_field_choices(self):
        """A tuple of allowed bid values"""
        return tuple([(i, currency(i)) for i in self.bid_choices()])


class Participant(ptree.models.BaseParticipant):

    match = models.ForeignKey(Match, null = True)
    treatment = models.ForeignKey(Treatment, null = True)
    subsession = models.ForeignKey(Subsession)

    bid_amount = models.PositiveIntegerField(
        null=True,
        doc="""
        Amount bidded by each participant
        """
    )
    is_winner = models.BooleanField(
        default=False,
        doc="""
        Indicates whether the participant is the winner or not
        """
    )

    def other_participant(self):
        """Returns other participant in match"""
        return self.other_participants_in_match()[0]

    def set_payoff(self):
        if self.is_winner:
            self.payoff = self.treatment.price_value - self.bid_amount
        else:
            self.payoff = 0


def treatments():

    return [Treatment.create(price_value=200)]