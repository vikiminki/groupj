"""Tournament Manager module."""

import sys
import textwrap

from sepm.exceptions import BackToMenu
from sepm.tournament.menus import ask_input, ask_players
from sepm.tournament.round_robin import RoundRobinTournament
from sepm.tournament.single_elim import SingleEliminiationTournament


class TournamentManager(object):
    """Tournament manager class."""

    def __init__(self, create_game, play_game):
        """Initialize a new tournament manager."""
        self.create_game = create_game
        self.play_game = play_game
        self.tournament = None

    def start(self):
        """Start the tournament manager."""
        if self.tournament is None:
            raise Exception(
                'Failed to start tournament - no tournament chosen!'
            )

        # Add players
        for name, ai_difficulty in self.players:
            self.tournament.add_player(name, ai_difficulty)

        self.tournament.start(randomize_players=True)

        print('Tournament schedule:\n')
        self.tournament.print_schedule()

        prev_round = None
        for match in self.tournament.matches():
            if match.round != prev_round:
                prev_round = match.round
                print('\nStandings:')
                self.tournament.print_standings()
            match.start()

        print('Match results:')
        self.tournament.print_schedule()

        print('Final standings:')
        self.tournament.print_standings()

    def show_menu(self):
        """Show the main menu."""
        menu = textwrap.dedent('''
            Tournament Manager
                1) New local game
                2) New round-robin tournament
                3) New single elimination tournament
                q) Quit''')

        while True:
            try:
                answer = ask_input(menu)
                if answer == '1':
                    self.local_game_menu()
                elif answer == '2':
                    self.round_robin_menu()
                elif answer == '3':
                    self.single_elim_menu()
                elif answer == 'q':
                    self.quit()
                else:
                    print('The input {} is not valid! Try again'.format(answer))

            except BackToMenu:
                pass

    def local_game_menu(self):
        """Create a new local game between humans and/or AIs."""
        self.players = ask_players(2)
        self.tournament = SingleEliminiationTournament(
            self.create_game,
            self.play_game
        )
        self.start()

    def round_robin_menu(self):
        """Create a new round-robin tournament."""
        self.players = ask_players()
        self.tournament = RoundRobinTournament(
            self.create_game,
            self.play_game
        )
        self.start()

    def single_elim_menu(self):
        """Create a new single elimination tournament."""
        self.players = ask_players()
        self.tournament = SingleEliminiationTournament(
            self.create_game,
            self.play_game
        )
        self.start()

    def quit(self):
        """Quit the TM."""
        print('\nBye!')
        exit(0)
