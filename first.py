from userinterface import userinterface

class game_manager:
    phase = 1
    state = []
    player_one = 9
    player_two = 9

    def change_phase(self, new_phase):
        self.phase = new_phase
    
    def init_game(self):
        print "So you want to play huh?"
        print "Press 1 or 2 to pick game mode"
        choice = input("Play versus player (1) or play versus computer(2):")
        if(choice == 2):
            print "Game mode not supported in this version"
        if(choice == 1):
            player1 = raw_input("Enter name for player 1:")
            player2 = raw_input("Enter name for player 2:")
            #"load board"
            print "Game starting up"
            ui = userinterface()
            ui.print_board()

    def init_move_options(self, player1, player2):
        move = move_options()
        move.give_options()

obj = game_manager()
obj.init_game()
