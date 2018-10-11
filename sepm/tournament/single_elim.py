"""Single elimination tournament module."""

import math

from sepm.tournament import Tournament
from sepm.tournament.bracket import SingleEliminationBracket
from sepm.tournament.match import Match


class SingleEliminiationTournament(Tournament):
    """Single eliminataion tournament class."""

    def __init__(self, create_game, play_game):
        """Initialize a new single elimination tournament."""
        super().__init__(create_game, play_game)

    def build_schedule(self):
        """Build the tournament schedule."""
        num_players = len(self.players)
        if num_players < 2:
            raise Exception('Tournament must have at least two players')

        rounds = {}
        schedule = []
        players = self.players.copy()[::-1]
        num_rounds = int(math.ceil(math.log(num_players, 2)))
        match_id = sum(2**r for r in range(num_rounds))

        for r in range(num_rounds):
            round = num_rounds - r
            parent_round = round + 1
            rounds[round] = []
            m_id = 0

            def add_matches(num_matches, has_player1, has_player2):
                nonlocal match_id, m_id, players

                for i in range(num_matches):
                    player1 = players.pop() if has_player1 else None
                    player2 = players.pop() if has_player2 else None

                    if round == num_rounds:
                        match_name = 'Final'
                    elif round == num_rounds - 1:
                        match_name = 'Semifinal %d' % (m_id + 1)
                    else:
                        if round > 1:
                            match_name = 'Match %d' % match_id
                        else:
                            display_id = num_matches - match_id + 1
                            match_name = 'Match %d' % display_id
                    match = Match(match_name, self, round)
                    if parent_round <= num_rounds:
                        match.parent = rounds[parent_round][m_id // 2]

                    match.player1 = self.compare_color_stats(player1, player2)
                    match.player2 = self.opposite_player(match.player1, player1, player2)
                    self.update_stats(match.player1, match.player2)
                    rounds[round].append(match)
                    schedule.insert(0, match)
                    match_id -= 1
                    m_id += 1

            if r+1 == num_rounds:
                empty_matches = 2**num_rounds - num_players
                full_matches = 2**(num_rounds-1) - empty_matches

                m_id = 0
                # Add matches with two players
                add_matches(full_matches, True, True)
                # Add placeholder match with one player
                add_matches(empty_matches, True, False)
            else:
                # Add later stage matches
                m_id = 0
                add_matches(2**r, False, False)

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
        """Print the tournament bracket."""
        bracket = SingleEliminationBracket(self)
        print(bracket.render())
