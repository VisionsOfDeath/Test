import random
from collections import defaultdict


class NotEnoughPlayersError(Exception):
    pass


class Organiser:
    TEAM_SIZE = 6

    def __init__(self):
        self.queues = defaultdict(lambda: set())

    def add(self, queue, player):
        self.queues[queue].add(player)

    def remove(self, queue, player):
        self.queues[queue].remove(player)

    def ready(self, queue):
        return len(self.queues[queue]) >= Organiser.TEAM_SIZE * 2

    def pop_teams(self, queue):
        if len(self.queues[queue]) < Organiser.TEAM_SIZE * 2:
            raise NotEnoughPlayersError('Not enough players!')

        candidates = list(self.queues[queue])
        random.shuffle(candidates)
        players = candidates[:Organiser.TEAM_SIZE * 2]
        team_one = players[Organiser.TEAM_SIZE:]
        team_two = players[:Organiser.TEAM_SIZE]
        for player in players:
            self.queues[queue].remove(player)
        return team_one, team_two
