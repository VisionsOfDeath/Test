from collections import defaultdict


class Queue:
    TEAM_SIZE = 5

    def __init__(self, players=None):
        if players:
            self.players = players
        else:
            self.players = []

    def add(self, player):
        new_players = self.players.copy()
        new_players.append(player)

        return Queue(new_players)

    def remove(self, player):
        new_players = self.players.copy()
        new_players.remove(player)
        return Queue(new_players)

    def __iter__(self):
        return self.players.__iter__()


class Organiser:
    def __init__(self, default_factory=None):
        if not default_factory:
            default_factory = lambda: Queue()  # noqa
        self.queues = defaultdict(default_factory)

    def add(self, queue, player):
        self.queues[queue] = self.queues[queue].add(player)

    def remove(self, queue, player):
        self.queues[queue] = self.queues[queue].remove(player)
