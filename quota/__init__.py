
from otree.api import *
c = cu

doc = 'quota=5'
class C(BaseConstants):
    NAME_IN_URL = 'quota'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
class Subsession(BaseSubsession):
    pass
def creating_session(subsession: Subsession):
    session = subsession.session
    if subsession.round_number == 1:
        subsession.session.num_participants_finished = 0
class Group(BaseGroup):
    pass
class Player(BasePlayer):
    quota_full = models.IntegerField(initial=0)
class MyPage1(Page):
    form_model = 'player'
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        participant.quota_full = player.quota_full
class MyPage2(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        session = player.session
        participant = player.participant
        return session.num_participants_finished >= 5
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        player.quota_full = 1
        participant.quota_full = player.quota_full
class MyPage3(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        return player.quota_full == 0
class MyPage4(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        return player.quota_full == 0
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        session = player.session
        subsession = player.subsession
        participant = player.participant
        player.subsession.session.num_participants_finished = player.subsession.session.num_participants_finished + 1
page_sequence = [MyPage1, MyPage2, MyPage3, MyPage4]