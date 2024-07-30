import quota as pages
from . import *
c = cu

class PlayerBot(Bot):
    def play_round(self):
        yield InformedConsent, dict(consent=True)
        if self.player.consent == True and self.player.quota_full == 1:
            yield Quotierung
        if self.player.consent == True and self.player.quota_full == 0:
            yield Willkommen