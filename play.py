from sepm.tournament.manager import TournamentManager
from first import game_manager


def create_game(player1, player2):
    return game_manager()



def play_game(game, match):
    game.init_game()
    winner = match.player1 if game.winner == 1 else match.player2
    match.finished(winner = winner)




tm = TournamentManager(create_game, play_game)
tm.show_menu()




