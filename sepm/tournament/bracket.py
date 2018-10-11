"""Bracket module responsible for rendering a bracket."""

from sepm.tournament.match import Match, player_name


def str_insert(text, replacement, index):
    """Insert a string inside another string."""
    length = len(replacement)
    start = text[:index]
    end = text[index+length:]
    return start + replacement + end


class ConsoleScreen():
    """Console screen with coordinates."""

    def __init__(self):
        """Initialize a new console screen."""
        self.screen = {}

    def put(self, texts, x, y):
        """Put text or several rows of text on the screen."""
        if isinstance(texts, str):
            texts = texts.split('\n')

        for i, text in enumerate(texts):
            row = y + i
            if row not in self.screen:
                self.screen[row] = ''
            old_text = self.screen[row]
            if len(old_text) < x:
                old_text += ' ' * x
            self.screen[row] = str_insert(old_text, text, x)

    def __str__(self):
        """String representation of the console screen."""
        lines = []
        rows = self.screen.keys()
        row_count = len(rows) if rows else 0
        if row_count > 0:
            row_count = max(rows)
        for row in range(row_count + 1):
            if row in self.screen:
                lines.append(self.screen[row])
            else:
                lines.append('')
        return '\n'.join(lines)


class Bracket():
    """Bracket class responsible for rendering a bracket."""

    def __init__(self, tournament):
        """Initialize a new bracket."""
        self.tournament = tournament
        self.screen = ConsoleScreen()
        self.build()

    def build(self):
        """Abstract method to build the bracket."""
        raise NotImplementedError()

    def render(self):
        """Return the bracket as a string."""
        return str(self.screen)


class SingleEliminationBracket(Bracket):
    """Single elimination bracket."""

    WIDTH = 16
    PLAYER_WIDTH = WIDTH - 1
    NAME_WIDTH = PLAYER_WIDTH - 4

    def player(self, name, first_player=True, centered=True):
        """Create a string showing the player name."""
        if name is None:
            name = 'None'
        if len(name) > self.NAME_WIDTH:
            name = name[:self.NAME_WIDTH-2] + '..'
        name = ' %s ' % name
        if centered:
            start_index = name.center(self.PLAYER_WIDTH).index(name)
        else:
            start_index = 1
        text = str_insert('─' * self.PLAYER_WIDTH, name, start_index)
        if first_player is None:
            text += '─'
        elif first_player:
            text += '┐'
        else:
            text += '┘'
        return text

    def match(self, player1, player2, round):
        """Create a string showing the two players."""
        empty_row = ' ' * self.PLAYER_WIDTH + '│'

        rows = []
        rows.append(self.player(player1, first_player=True))
        rows.extend([empty_row] * (2**round - 1))
        rows.append(self.player(player2, first_player=False))
        return rows

    def build(self):
        """Build the single elimination tournament bracket."""
        max_rounds = max(self.tournament.rounds.keys())
        for round, matches in self.tournament.rounds.items():
            x = (round - 1) * self.WIDTH
            y = 2**(round-1) - 1
            diff = 2**(round+1)
            for match in matches:
                player1 = player_name(match.player1)
                player2 = player_name(match.player2)
                text = self.match(player1, player2, round)
                self.screen.put(text, x, y)
                y += diff

        # Render winner
        final = self.tournament.rounds[max_rounds][0]
        player = self.player(
            player_name(final),
            first_player=None
        )
        self.screen.put(player, max_rounds * self.WIDTH, 2**max_rounds-1)
