"""Tournament base module."""

import random
from collections import namedtuple

from sepm import PieceColor as Color
from sepm.tournament.match import Match


class Tournament(object):
    """Tournament base class."""

    def __init__(self, create_game, play_game):
        """Initialize a new tournament."""
        self.create_game = create_game
        self.play_game = play_game

        self.schedule = []
        self.players = []
        self.statistics = {}

    def start(self, randomize_players=False):
        """Start the tournament."""
        if randomize_players:
            self.players = random.sample(self.players, len(self.players))

        self.build_schedule()

    def build_schedule(self):
        """Build the tournament schedule."""
        raise NotImplementedError('Abstract build_schedule()')

    def print_standings(self):
        """Print the tournament standings."""
        pass

    def print_schedule(self):
        """Print the tournament schedule."""
        prev_round = None
        for match in self.schedule:
            if match.round != prev_round:
                print('=== Round {} ==='.format(match.round))
                prev_round = match.round
            if match.is_full:
                print(match)

    def next_match(self):
        """Get the next match."""
        raise NotImplementedError('Abstract next_match()')

    def matches(self):
        """Play and iterate over all matches."""
        match = self.next_match()
        while match is not None:
            if isinstance(match.player1, Match):
                match.player1 = match.player1.result.winner
            if isinstance(match.player2, Match):
                match.player2 = match.player2.result.winner

            match.game = self.create_game(
                match.player1,
                match.player2
            )
            if not match.is_full:
                match.finished(match.player1, 9, 0)
            yield match
            match = self.next_match()

    def add_player(self, name, ai_difficulty=None):
        """
        Add a player to the tournament.

        :param name: Name of the player
        :param ai_difficulty: AI difficulty as a string (easy/medium/hard)
        """
        player = namedtuple('Player', ['name', 'color', 'ai_difficulty'])
        player.name = name
        player.ai_difficulty = ai_difficulty
        self.players.append(player)

    def match_finished(self, match):
        """Called when a match is finished."""
        pass

    def update_stats(self, player1, player2):
        """Updates the tournament statistics."""
        if player1 is None or player2 is None:
            pass
        else:
            self.statistics[player1][Color.Black] += 1
            self.statistics[player2][Color.White] += 1

    def compare_color_stats(self, player1, player2):
        """Checks which player should start the game."""
        if len(self.statistics) == 0:
            self.statistics[player1] = {Color.Black: 0, Color.White: 0}
            self.statistics[player2] = {Color.Black: 0, Color.White: 0}
            return player1

        player1_start_count = self.get_count_stats(player1)
        player2_start_count = self.get_count_stats(player2)

        if player1_start_count[Color.Black] > player2_start_count[Color.Black]:
            return player2
        elif player1_start_count[Color.White] < player2_start_count[Color.White]:
            return player2
        else:
            return player1

    def get_count_stats(self, player):
        """Returns a dictionary with statistics belonging to the player."""
        try:
            player_start_count = {
                Color.Black: self.statistics[player][Color.Black],
                Color.White: self.statistics[player][Color.White],
            }
        except KeyError:
            self.statistics[player] = {Color.Black: 0, Color.White: 0}
            player_start_count = self.statistics[player]

        return player_start_count

    def opposite_player(self, myplayer, player1, player2):
        """Returns opposite player."""
        if myplayer is player1:
            return player2
        else:
            return player1
