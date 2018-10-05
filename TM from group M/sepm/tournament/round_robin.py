"""Round robin tournament module."""

import math
from itertools import zip_longest

from sepm.tournament import Tournament
from sepm.tournament.match import Match


def round_robin_scheduler(values):
    """Generator to create matchups between the given values."""
    if len(values) % 2 != 0:
        values.append(None)
    n = len(values)
    rounds = n - 1
    row1 = values[:n // 2]
    row2 = values[n:n//2-1:-1]

    for _ in range(1, rounds+1):
        matchups = list(zip_longest(row1, row2))
        row1.insert(1, row2.pop(0))
        row2.append(row1.pop())
        yield matchups


class RoundRobinTournament(Tournament):
    """Round robin tournament class."""

    def __init__(self, create_game, play_game):
        """Initialize a new Round-robin tournament."""
        super().__init__(create_game, play_game)
        self.points = {}

    def build_schedule(self):
        """Build the tournament schedule."""
        rounds = {}
        schedule = []
        matchups = round_robin_scheduler(self.players)
        match_id = 1
        for round, matches in enumerate(matchups):
            round += 1
            rounds[round] = []
            for player1, player2 in matches:
                match = Match('Match %d' % match_id, self, round)
                match.player1 = player1
                match.player2 = player2
                match_id += 1
                rounds[round].append(match)
                schedule.append(match)
        self.rounds = rounds
        self.schedule = schedule
        self.current_id = 0

    def next_match(self):
        """Get the next match."""
        try:
            match = self.schedule[self.current_id]
            self.current_id += 1
            return match
        except IndexError:
            return None

    def print_standings(self):
        """Print the current standings."""
        score = sorted(self.points.items(), key=lambda x: x[1], reverse=True)
        for name, points in score:
            print('{} - {} point(s)'.format(name, points))

    def add_points(self, player, points):
        """Add points to player."""
        if isinstance(player, tuple):
            name = player[0]
        else:
            name = player.name
        if name not in self.points:
            self.points[name] = 0
        print('added {} point(s) to {}'.format(points, name))
        self.points[name] += points

    def match_finished(self, match):
        """Called when a match is finished."""
        # Only give points if two players were in the match
        if match.is_full:
            result = match.result
            if result.is_draw:
                self.add_points(match.player1, 0.5)
                self.add_points(match.player2, 0.5)
            else:
                self.add_points(result.winner, 1.0)
