from sepm.tournament.manager import TournamentManager


def create_game(*players):
    """
    Helper function that starts a new game.

    :param players: Array of players as 2 tuples (name, ai_difficulty)
    :return: A 3-tuple with the created game object, player1 and player2
    """
    # Create game, player1 and player2 then return (game, player1, player2)
    pass


def play_game(game, match):
    """
    Play the game and update the match result with ``match.finished(...)``.

    :param game: Game object previously created in create_game
    :param match: Current match object
    """
    # Run the game
    # Call match.finished(...) to notify the match is over and save the results
    pass


if __name__ == '__main__':
    tm = TournamentManager(create_game, play_game)
    tm.show_menu()
