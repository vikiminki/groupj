from userinterface import userinterface

class game_manager:
    phase = 1
    player_one = {"name": "", "color": "black", "stones": 0}
    player_two = {"name": "", "color": "white", "stones": 0}
    turn = 1
    ui = userinterface()

    def init_game(self):
        print("So you want to play huh?")
        print("Press 1 or 2 to pick game mode")
        #we should catch exceptions in reasonable way
        choice = input("Play versus player (1) or play versus computer(2):")
        if choice == "2":
            print("Game mode not supported in this version")
        if choice == "1":
            player1 = input("Enter name for player 1:")
            player2 = input("Enter name for player 2:")
            self.player_one["name"] = player1
            self.player_two["name"] = player2
            print("Game starting up")
            print(player1 ,"is black, ", player2 , " is white.")
            if(self.phase == 1):
                self.place()
            else:
                self.move()

    def place(self):
        self.ui.print_board()
        print("\n")
        print("To place a stone type the position you want to place a stone in, f.e g7: \n")
        #self.ui.print_board_move()
        place = input("Make move: \n")
        if(self.ui.legal_move(place)):
            if(self.turn % 2 == 1):
                self.ui.make_move(place, "B"+ str(self.player_one["stones"] + 1))
                self.player_one["stones"] += 1
            else:
                self.ui.make_move(place, "W" + str(self.player_two["stones"] + 1))
                self.player_two["stones"] += 1
            self.turn += 1
            if((self.player_one["stones"] > 9) and (self.player_two["stones"] >9)):
                self.phase = 2
                print("Phase 2!")
            else:
                self.place()
        else:
            print("The move you are trying to make is not legal! Try again")
            self.place()
    
    #def move(self): 
        #check if phase 2 or 3
        #depending on which turn, player 1/2 picks which stone to move
        #is move legal? 
        #

    #def mill(self):
        #should be called after each move has taken place to check for mill?
        #return true if mill has occured


    #def end_game(self):
        #determines if the game is to end
        #player has zero stones/player cant move -> opponent wins
        #certain amount of turns have passed -> it's a tie 

    #def remove_stone(self):
        #gives player option to remove a stone after a mill

obj = game_manager()
obj.init_game()
