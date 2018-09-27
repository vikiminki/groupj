from userinterface import userinterface

class game_manager:
    phase = 1
    player_one = {"name": "", "color": "black", "stones": 1}
    player_two = {"name": "", "color": "white", "stones": 1}
    turn = 1
    ui = userinterface()

    def init_game(self):
        print("So you want to play huh?")
        print("Press 1 or 2 to pick game mode")
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
        while(not(place in self.ui.values)):
            print("Syntax error, please select valid position!")
            place = input("Make move: \n")
            
        while(not(self.ui.legal_move(place))):
            print("Illegal move, the position is taken!")
            place = input("Make new move: \n")
        if(self.turn % 2 == 1):
            self.ui.make_move(place, "B"+ str(self.player_one["stones"]))
            self.player_one["stones"] += 1
        else:
            self.ui.make_move(place, "W" + str(self.player_two["stones"]))
            self.player_two["stones"] += 1
        self.turn += 1
        if((self.player_one["stones"] > 9) and (self.player_two["stones"] >9)):
            self.phase = 2
            print("Phase 2!")
        else:
            self.place()
     
            
            
    
    def move(self):
        self.ui.print_board()
        print("\n")
        print("To move type the chose the stone you wish to move, e.g. B4")
        stone = input("Chose stone: \n")
        while(not(place in self.ui.values)):
            print("Syntax error, please select valid stone!")
            stone = input("Chose stone: \n")
        if(self.turn % 2 == 1):
            while(not(self.ui.black_white() == "w")):
                print("Select one of your stones")
                stone = input("Chose stone \n")
            input("Select position you wish to move stone to: \n")
        
        

obj = game_manager()
obj.init_game()
