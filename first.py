from userinterface import user_interface

class game_manager:
    phase = 1
    state = []
    player_one = 9
    player_two = 9

    def __init__(self, phase):
        self.phase = phase

    def change_phase(self):
        print self.phase
        self.phase = 2
        print self.phase
    
    def init_game(self):
                
        print "So you want to play huh?"
        print "Press 1 or 2 to pick game mode"
        choice = input("Play versus player (1) or play versus computer(2):")
        if(choice == 2):
            print "Game mode not supported in this version"
        if(choice == 1):
            player1 = raw_input("Enter name for player 1:")
            player2 = raw_input("Enter name for player 2:")
            self.init_game()
            self.init_move_options(player1,player2)
            #"load board"
            ui.print_board()
            print "Game starting up"
    
    def init_move_options(self):
        move = move_options()
        move.give_options()

obj = game_manager(1)
obj.init_game()
