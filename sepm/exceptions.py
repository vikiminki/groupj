"""Game platform-related exceptions module."""

from sepm import PieceColor


class FoundMillError(Exception):
    """Exception raised when the mill is found."""

    pass


class BackToMenu(Exception):
    """Exception raised when the user wants to return to menu."""

    pass


class GameOver(Exception):
    """Exception raised when the game is over."""

    def __init__(self, winner):
        """Initiate a game over exception with a message and optionally a winner."""
        super().__init__(winner)
        self.winner = winner
