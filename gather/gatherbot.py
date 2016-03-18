import logging
from lib.bot import Bot


logger = logging.getLogger(__name__)


class GatherBot(Bot):
    TEAM_SIZE = 5

    def __init__(self):
        super().__init__()

        self.players = set()

    async def announce_players(self, channel):
        await self.say(
            channel,
            'Currently signed in players: {0}.'.format(
                ', '.join([p.name for p in self.players])
            )
        )
