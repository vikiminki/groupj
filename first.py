from userinterface import userinterface

class game_manager:
    phase = 1
    player_one = {"name": "", "color": "black", "stones": 0}
    player_two = {"name": "", "color": "white", "stones": 0}
    turn = 0
    ui = userinterface()

    def init_game(self):
        print("So you want to play huh?")
        print("Press 1 or 2 to pick game mode")
        #we should catch exceptions in reasonable way
        choice = input("Play versus player (1) or play versus computer(2) or run phase 2(3) or run end of phase 1(4):\n")
        if choice == "2":
            print("Game mode not supported in this version") 
        if choice == "1":
            player1 = input("Enter name for player 1:")
            player2 = input("Enter name for player 2:")
            self.player_one["name"] = player1
            self.player_two["name"] = player2
            print("Game starting up")
            print(player1 ,"is black, ", player2 , " is white.")
            print("\n")
            self.place()
            
        if choice == "3":
            self.ui.values = {"a1":"B1", "d1":"W1", "g1":"B2", "e1":"W2", "b2":"W3", "d2":"B3", 
            "f2":"0 ", "c3":"0 ", "d3":"0 ", "e3":"0 ", "a4":"0 ", "b4":"W4", "c4":"B4", 
            "e4":"W9", "f4":"B8", "g4":"B6", "c5":"W6", "d5":"B7",
            "e5":"B9", "b6":"W8","d6":"W7", "f6":"0 ", "a7":"0 ", "d7":"W5", "g7":"B5"}
            self.player_one["stones"] = 9
            self.player_two["stones"] = 9
            self.turn = 18
            print("Turn 19, first turn of phase 2 initiated" )
            self.move()
        if choice == "4":
            self.ui.values = {"a1":"B1", "d1":"W1", "g1":"B2", "e1":"W2", "b2":"W3", "d2":"B3", 
            "f2":"0 ", "c3":"0 ", "d3":"0 ", "e3":"0 ", "a4":"0 ", "b4":"W4", "c4":"B4", 
            "e4":"W9", "f4":"B8", "g4":"B6", "c5":"W6", "d5":"B7",
            "e5":"B9", "b6":"W8","d6":"W7", "f6":"0 ", "a7":"0 ", "d7":"W5", "g7":"B5"}
            self.player_one["stones"] = 8
            self.player_two["stones"] = 8
            self.turn = 16
            print("Turn 16, 2 turns away from phase 2 initiated")
            self.place()
        else:
            print("Wrong input, try again")
            self.init_game()



    def place(self):
        self.ui.print_board()
        print("\n")
        self.turn += 1
 
        if(self.turn % 2 == 1):
            print("Its " + self.player_one["name"] +"'s turn! Please place a black stone.\n")
        else:
            print("Its " + self.player_one["name"] +"'s turn! Please place a white stone. \n")
        
        print("To place a stone type the position you want to place a stone in, f.e g7. \n")
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
            if((self.player_one["stones"] > 8) and (self.player_two["stones"] > 8)): #dont seem to be working
                self.phase = 2
                print("Phase 2!")
                self.move()
            else:
                self.place()
        else:
            print("The move you are trying to make is not legal! Try again")
            self.place()


    def move(self):
        self.turn += 1
        self.ui.print_board()
        print("\n") 
        print("To move type the the stone you wish to move, e.g. B4")

        if(self.turn % 2 == 1):
            print("Its " + self.player_one["name"] +"'s turn! Please pick a black stone.\n")
        else:
            print("Its " + self.player_one["name"] +"'s turn! Please pick a white stone. \n")
        stone = self.stone_exists()

        stone_color = self.ui.black_white(stone)
        mydict = self.ui.values
        oldpos = list(mydict.keys())[list(mydict.values()).index(stone)]
        pos = ""
        print("\n")
        if(self.turn % 2 == 1): #black's turn
            while(not(stone_color == "b")):
                print("Select one of your stones")
                stone = self.stone_exists()
                stone_color = self.ui.black_white(stone)
                pos = input("Select position you wish to move stone to: \n")
                while(not(self.ui.legal_move(pos))):
                    
                    print("Not a legal move, try again or type x to pick another stone")
                    pos = input("Enter another position or x: \n")
                    if pos == "x":
                        stone_color = "w"
                        break
            if(not(pos in self.ui.values.keys())):
                pos = input("Select position you wish to move stone to: \n")
                while(not(self.ui.legal_move(pos))):
                    print("Not a legal move, try again or type x to pick another stone")
                    pos = input("Enter another position or x: \n")
                    if pos == "x":
                        stone_color = "w"
        else: #white's turn
            while(not(stone_color == "w")):
                print("Select one of your stones")
                stone = self.stone_exists()
                stone_color = self.ui.black_white(stone)
                pos = input("Select position you wish to move stone to: \n")
                while(not(self.ui.legal_move(pos))):
                    print("Not a legal move, try again or type x to pick another stone")
                    pos = input("Enter another position or x: \n")
                    if pos == "x":
                        stone_color = "b"
                        break
        if(not(pos in self.ui.values.keys())):
                pos = input("Select position you wish to move stone to: \n")
                while(not(self.ui.legal_move(pos))):
                    print("Not a legal move, try again or type x to pick another stone")
                    pos = input("Enter another position or x: \n")
                    if pos == "x":
                        stone_color = "b"

        print("\n")
        self.ui.move_stone(stone, pos, oldpos)
        print("turn: "+ self.turn)
        self.move()

   # def move_is_legal
    #while(not(self.ui.legal_move(pos))):
     #               print("Not a legal move, try again or type x to pick another stone")
      #              pos = input("Enter another position or x: \n")
       #             if pos == "x":
        #                stone_color = "w"
         #           print("5")
    
                    


    def stone_exists(self): 
        print("\n")
        stone = input("Pick a stone to move:")
        while(not(stone in self.ui.values.values())):
            stone = input("Not a valid stone to pick! Try again")
        return stone


            
    #def end_game(self):
        #determines if the game is to end
        #player has zero stones/player cant move -> opponent wins
        #certain amount of turns have passed -> it's a tie 



obj = game_manager()
obj.init_game()
