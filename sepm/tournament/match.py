"""Tournament match module."""

def player_name(player):
    """Get the player name."""
    if hasattr(player, 'name'):
        return player.name
    elif isinstance(player, Match):
        match = player
        if match.is_over:
            return player_name(match.result.winner)
        else:
            return player.id
    else:
        return player


class MatchResult(object):
    """Match result class."""

    def __init__(self, match, winner, winner_stones, loser_stones, stats):
        """
        Initiate a new match result.

        :param match: Match this result belongs to
        :param winner: Winning player
        :param winner_stones: # of stones for the winner
        :param loser_stones: # of stones for the loser
        :param stats: Game statistics
        """
        self.match = match
        self.winner = winner
        self.loser = None
        if winner is not None:
            if winner == match.player1:
                self.loser = match.player2
            else:
                self.loser = match.player1
        self.winner_stones = winner_stones
        self.loser_stones = loser_stones
        self.stats = stats

    @property
    def is_draw(self):
        """Check if the match was a draw."""
        return self.winner is None

    def __repr__(self):
        """Representation of MatchResult object."""
        return 'MatchResult(match="{}" winner="{}", result="{}-{}")'.format(
            self.match.id, self.winner, self.winner_stones, self.loser_stones
        )


class Match(object):
    """Match class."""

    def __init__(self, id, tournament, round):
        """Initialize a new match."""
        self.id = id
        self.tournament = tournament
        self.round = round
        self.game = None
        self._parent = None
        self.player1 = None
        self.player2 = None
        self.result = None

    @property
    def parent(self):
        """Get the parent match."""
        return self._parent

    @parent.setter
    def parent(self, match):
        """Set the parent match."""
        if match.player1 is None:
            match.player1 = self
        elif match.player2 is None:
            match.player2 = self
        self._parent = match

    @property
    def is_over(self):
        """Check if the match is over."""
        return self.result is not None

    @property
    def is_full(self):
        """Check if the match is full (two players)."""
        return self.player1 is not None and self.player2 is not None

    def start(self):
        """Start a match."""
        if self.game is not None:
            self.tournament.play_game(self.game, self)

        return self.result

    def finished(self, winner, winner_stones=0, loser_stones=0, stats={}):
        """Match is over, save the results."""
        if self.parent:
            if self.parent.player1 == self:
                self.parent.player1 = winner
            elif self.parent.player2 == self:
                self.parent.player2 = winner
        res = MatchResult(self, winner, winner_stones, loser_stones, stats)
        self.result = res
        self.tournament.match_finished(self)

    def __repr__(self):
        """Representation of a match object."""
        items = {key: getattr(self, key)
                 for key in dir(self) if not key.startswith('_')}
        return 'Match(id={id})'.format(**items)

    def __str__(self):
        """String representation of a match."""
        s = '{player1} vs. {player2}'.format(
            player1=player_name(self.player1),
            player2=player_name(self.player2),
            round=self.round
        )

        if self.is_over:
            if self.result.is_draw:
                s += ' (draw)'
            else:
                s += ' ({} won)'.format(player_name(self.result.winner))
        return s
