"""SEPM base module with helper functions and classes."""

import re

from enum import Enum


RE_NODE = re.compile(r'([a-g])(\d)', re.IGNORECASE)
RE_INV_NODE = re.compile(r'(\d)([a-g])', re.IGNORECASE)


def check_valid_pos(position):
    """Check if a position is a valid board position."""
    pos = position.strip()
    if len(pos) > 2:
        return False

    m = RE_NODE.search(pos)
    if m:
        return pos
    else:
        m = RE_INV_NODE.search(position)
        if m:
            return '{}{}'.format(m.group(2), m.group(1))
    return False


class Phase(Enum):
    """Player phases."""

    placing = 'Placing pieces'
    moving = 'Moving pieces'
    flying = 'Flying'


class PieceColor(Enum):
    """Piece colors."""

    Empty = ''
    Black = 'B'
    White = 'W'


class GamePiece:
    """Game piece class."""

    def __init__(self, color):
        """Initialize a new game piece object."""
        self._color = color

    @property
    def color(self):
        """Getter for the piece color."""
        return self._color

    def __str__(self):
        """String representation of a game piece."""
        return self._color.value
