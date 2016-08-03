class Organiser:
    def __init__(self, players=None):
        if players:
            self.players = players
        else:
            self.players = []

    def add(self, player):
        new_players = self.players.copy()
        new_players.append(player)
        return Organiser(new_players)

    def remove(self, player):
        new_players = self.players.copy()
        new_players.remove(player)
        return Organiser(new_players)
