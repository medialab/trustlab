# -*- coding: utf-8 -*-$
"""Views for Survey."""
from __future__ import division
from ._builtin import Page
from . import models
from django.utils.translation import ugettext_lazy as _


def vars_for_all_templates(self):
    """Return variables for all templates."""
    return {
        'q_1_7_label': _("I‘d like to ask you how much you trust people from \
various groups. Could you tell me for each of these groups how much you \
trust them? Please tell me on a scale of 0 to 10, where 0 means that you \
don't trust them at all and 10 means that you fully trust them."),
        'q_1_7_label_1': _('Your family'),
        'q_1_7_label_2': _('People in your neighborhood'),
        'q_1_7_label_3': _('People you know personally'),
        'q_1_7_label_4': _('People you meet for the first time'),
        'q_1_7_label_5': _('People of another religion'),
        'q_1_7_label_6': _('People of another nationality'),
        'q_2_1_label': _("I‘d like to ask you how much you trust different \
public institutions. How much trust do you have in the following to act \
in the best interest of society? Please tell me on a scale of 0 to 10, \
where 0 means that you don't trust them at all and 10 means \
that you fully trust them."),
        'q_2_1_label_1': _('Your government'),
        'q_2_1_label_2': _('The police'),
        'q_2_1_label_3': _('The media'),
        'q_2_2_label': _("Do you agree with the following statements?"),
        'q_2_2_label_1': _('Public institutions deliver public services in the \
best possible way'),
        'q_2_2_label_2': _('Public institutions pursue long term objectives'),
        'q_2_2_label_3': _('People working in public institutions \
behave according to ethical standards aimed at avoiding corruption'),
        'q_2_2_label_4': _('Public institutions are transparent'),
        'q_2_2_label_5': _('Public institutions treat all citizens \
fairly regardless of their gender, race, age or economic condition equally'),
    }


class TrustAndTrustingBehaviour1(Page):
    """Page for Trust And Trusting Behaviour."""

    form_model = models.Player
    form_fields = ['q_1_1', 'total_time']
    template_name = 'survey/TrustAndTrustingBehaviour1.html'


class TrustAndTrustingBehaviour2(Page):
    """Page for Trust And Trusting Behaviour."""

    form_model = models.Player
    form_fields = ['q_1_2']
    template_name = 'survey/TrustAndTrustingBehaviour2.html'


class TrustAndTrustingBehaviour3(Page):
    """Page for Trust And Trusting Behaviour."""

    form_model = models.Player
    form_fields = ['q_1_3']
    template_name = 'survey/TrustAndTrustingBehaviour3.html'


class TrustAndTrustingBehaviour4(Page):
    """Page for Trust And Trusting Behaviour."""

    form_model = models.Player
    form_fields = ['q_1_4']
    template_name = 'survey/TrustAndTrustingBehaviour4.html'


class TrustAndTrustingBehaviour5(Page):
    """Page for Trust And Trusting Behaviour."""

    form_model = models.Player
    form_fields = ['q_1_5']
    template_name = 'survey/TrustAndTrustingBehaviour5.html'


class TrustAndTrustingBehaviour6(Page):
    """Page for Trust And Trusting Behaviour."""

    form_model = models.Player
    form_fields = ['q_1_6']
    template_name = 'survey/TrustAndTrustingBehaviour6.html'


class TrustAndTrustingBehaviour7(Page):
    """Page for Trust And Trusting Behaviour."""

    form_model = models.Player
    form_fields = [
        'q_1_7_1', 'q_1_7_2', 'q_1_7_3', 'q_1_7_4', 'q_1_7_5', 'q_1_7_6'
    ]
    template_name = 'survey/TrustAndTrustingBehaviour7.html'


class TrustAndTrustingBehaviour8(Page):
    """Page for Trust And Trusting Behaviour."""

    form_model = models.Player
    form_fields = ['q_1_8']
    template_name = 'survey/TrustAndTrustingBehaviour8.html'


class TrustAndTrustingBehaviour9(Page):
    """Page for Trust And Trusting Behaviour."""

    form_model = models.Player
    form_fields = ['q_1_9']
    template_name = 'survey/TrustAndTrustingBehaviour9.html'


class TrustInInstitution1(Page):
    """Page for Trust In Institution."""

    form_model = models.Player
    form_fields = ['q_2_1_1', 'q_2_1_2', 'q_2_1_3']
    template_name = 'survey/TrustInInstitution1.html'


class TrustInInstitution2(Page):
    """Page for Trust In Institution."""

    form_model = models.Player
    form_fields = ['q_2_2_1', 'q_2_2_2', 'q_2_2_3']
    template_name = 'survey/TrustInInstitution2.html'


class Demographics1(Page):
    """Page for Demographics."""

    form_model = models.Player
    form_fields = ['q_birthdate']
    template_name = 'survey/Demographics1.html'


class Demographics2(Page):
    """Page for Demographics."""

    form_model = models.Player
    form_fields = ['q_gender']
    template_name = 'survey/Demographics2.html'


class Demographics3(Page):
    """Page for Demographics."""

    form_model = models.Player
    form_fields = ['q_household']
    template_name = 'survey/Demographics3.html'


class Demographics4(Page):
    """Page for Demographics."""

    form_model = models.Player
    form_fields = ['q_country']
    template_name = 'survey/Demographics4.html'


class Demographics5(Page):
    """Page for Demographics."""

    form_model = models.Player
    form_fields = ['q_country_year']
    template_name = 'survey/Demographics5.html'


class Demographics6(Page):
    """Page for Demographics."""

    form_model = models.Player
    form_fields = ['q_country_citizenship']
    template_name = 'survey/Demographics6.html'


class Demographics7(Page):
    """Page for Demographics."""

    form_model = models.Player
    form_fields = ['q_education']
    template_name = 'survey/Demographics7.html'


class Demographics8(Page):
    """Page for Demographics."""

    form_model = models.Player
    form_fields = ['q_situation']
    template_name = 'survey/Demographics8.html'


class Demographics9(Page):
    """Page for Demographics."""

    form_model = models.Player
    form_fields = ['q_work_sector']
    template_name = 'survey/Demographics9.html'


class Demographics10(Page):
    """Page for Demographics."""

    form_model = models.Player
    form_fields = ['q_trust']
    template_name = 'survey/Demographics10.html'


class Demographics11(Page):
    """Page for Demographics."""

    form_model = models.Player
    form_fields = ['q_income_sources']
    template_name = 'survey/Demographics11.html'


class Demographics12(Page):
    """Page for Demographics."""

    form_model = models.Player
    form_fields = ['q_income_total']
    template_name = 'survey/Demographics12.html'


class Demographics13(Page):
    """Page for Demographics."""

    form_model = models.Player
    form_fields = ['q_religion', 'q_jewish']
    template_name = 'survey/Demographics13.html'


class WrapUp1(Page):
    """Survey wrap-up page."""

    form_model = models.Player
    form_fields = ['q_4_1']
    template_name = 'survey/WrapUp1.html'


class WrapUp2(Page):
    """Survey wrap-up page."""

    form_model = models.Player
    form_fields = ['q_4_2']
    template_name = 'survey/WrapUp2.html'


class WrapUp3(Page):
    """Survey wrap-up page."""

    form_model = models.Player
    form_fields = ['q_4_3']
    template_name = 'survey/WrapUp3.html'


class WrapUp4(Page):
    """Survey wrap-up page."""

    form_model = models.Player
    form_fields = ['q_4_4']
    template_name = 'survey/WrapUp4.html'


class WrapUp5(Page):
    """Survey wrap-up page."""

    form_model = models.Player
    form_fields = ['q_4_5']
    template_name = 'survey/WrapUp5.html'


class EndGame(Page):
    """End game page."""

    form_model = models.Player
    form_fields = ['total_time']

    def vars_for_template(self):
        """Make data available in template."""
        return {'start_time': self.player.total_time}


page_sequence = [
    TrustAndTrustingBehaviour1,
    TrustAndTrustingBehaviour2,
    TrustAndTrustingBehaviour3,
    TrustAndTrustingBehaviour4,
    TrustAndTrustingBehaviour5,
    TrustAndTrustingBehaviour6,
    TrustAndTrustingBehaviour7,
    TrustAndTrustingBehaviour8,
    TrustAndTrustingBehaviour9,
    TrustInInstitution1,
    TrustInInstitution2,
    Demographics1,
    Demographics2,
    Demographics3,
    Demographics4,
    Demographics5,
    Demographics6,
    Demographics7,
    Demographics8,
    Demographics9,
    Demographics10,
    Demographics11,
    Demographics12,
    Demographics13,
    WrapUp1,
    WrapUp2,
    WrapUp3,
    WrapUp4,
    WrapUp5,
    EndGame
]
