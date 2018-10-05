"""Tournament base module."""

import random

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

            if match.player1 and match.player2:
                match.game, match.player1, match.player2 = self.create_game(
                    match.player1,
                    match.player2
                )
            else:
                match.finished(match.player1, 9, 0)
            yield match
            match = self.next_match()

    def add_player(self, name, ai_difficulty=None):
        """
        Add a player to the tournament.

        :param name: Name of the player
        :param ai_difficulty: AI difficulty as a string (easy/medium/hard)
        """
        self.players.append((name, ai_difficulty))

    def match_finished(self, match):
        """Called when a match is finished."""
        pass
