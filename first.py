from userinterface import userinterface
from _operator import pos

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
        choice = input("Play versus player (1) or play versus computer(2) or run phase 2(3) or run end of phase 1 (4):")
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
            if(self.phase == 1):
                self.place()
            self.move()
        if choice == "3":
            self.ui.values = {"a1":"B1", "d1":"W1", "g1":"B2", "e1":"W2", "b2":"W3", "d2":"B3", 
            "f2":"0 ", "c3":"0 ", "d3":"0 ", "e3":"0 ", "a4":"0 ", "b4":"W4", "c4":"B4", 
            "e4":"W9", "f4":"B8", "g4":"B6", "c5":"W6", "d5":"B7",
            "e5":"B9", "b6":"W8","d6":"W7", "f6":"0 ", "a7":"0 ", "d7":"W5", "g7":"B5"}
            self.move()

        if choice == "4":
            self.ui.values = {"a1":"B1", "d1":"W1", "g1":"B2", "e1":"W2", "b2":"W3", "d2":"B3", 
            "f2":"0 ", "c3":"0 ", "d3":"0 ", "e3":"0 ", "a4":"0 ", "b4":"W4", "c4":"B4", 
            "e4":"0 ", "f4":"B8", "g4":"B6", "c5":"W6", "d5":"B7",
            "e5":"0 ", "b6":"W8","d6":"W7", "f6":"0 ", "a7":"0 ", "d7":"W5", "g7":"B5"}
            self.player_one["stones"] = 8
            self.player_two["stones"] = 8
            self.turn = 16
            print("Turn 16, 2 turns away from phase 2 initiated")
            self.place()
            self.move()
        
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
                self.ui.check_mill() #takes 2 arguments: color and position
            
            else:
                self.ui.make_move(place, "W" + str(self.player_two["stones"] + 1))
                self.player_two["stones"] += 1
                self.ui.check_mill() #takes 2 arguments: color and position
            
            if((self.player_one["stones"] > 8) and (self.player_two["stones"] > 8)):
                self.phase = 2
                return()
                #self.move()
            else:
                self.place()
        else:
            print("The move you are trying to make is not legal! Try again")
            self.place()
            
            
            
    def move(self):
        #kolla med victoria om det här verkligen ska va i början
        self.turn += 1
        self.ui.print_board()
        
        result = "x"
        print("\n") 
        print("To move type the the stone you wish to move, e.g. B4")
        
        
        if(self.turn % 2 == 1):
            print("Its " + self.player_one["name"] +"'s turn! Please pick a black stone.\n")
            
            while(result == "x"):
                result = self.move_algorithm()
                print(result)
            # now put stone using the place and remove the old one
            mydict = self.ui.values
            oldpos = list(mydict.keys())[list(mydict.values()).index(result[0])]
            
            self.ui.move_stone(result[0], result[1], oldpos)
            
        else:
            print("Its " + self.player_one["name"] +"'s turn! Please pick a white stone. \n")
            
            while(result == "x"):
                 result = self.move_algorithm()
            
            mydict = self.ui.values
            oldpos = list(mydict.keys())[list(mydict.values()).index(result[0])]
            
            self.ui.move_stone(result[0], result[1], oldpos)
            
            
            '''
            while(not(self.ui.black_white == "b"))
                stone = input("Please select a stone that is black")
                color = self.ui.black_white
            #Checks if contains. contains gives boolean
            while(not(ui.contains(ui,stone))):
                stone = input("Please select a stone that exists on the board")
            
            pos = input("Please select a position")
            
            while(not(ui.legal_move(ui,pos))):
                pos = input("Please, a valid position or type x to change the selected stone")
                if(pos == "x"):
                    break
                    #like this for now, add the shit tomorrow
                    #tip for tomorrow try picking everything from comment and use recursion
            
            #now move the stone victoria knows how to do this
               
            
        if(self.turn % 2 == 1):
        else:
            print("Its " + self.player_one["name"] +"'s turn! Please pick a white stone. \n")
        
        while(not(self.ui.black_white == "w"))
        stone = input("Please select a stone")
        color = self.ui.black_white
        #Checks if contains. contains gives boolean
        while(not(ui.contains(ui,stone))):
            stone = input("Please select a stone")
            
        if(self.turn % 2 == 1):
          '''  
            
            
            
            
    def move_algorithm(self):
        stone = input("Please select a stone that is black")
        color = self.ui.black_white(stone)
        
        while(not(self.ui.black_white(stone) == color)):
                stone = input("Please select a stone that is black")
                color = self.ui.black_white(stone)
                
        #Checks if contains. contains gives boolean
        while(not(self.ui.contains(stone))):
            stone = input("Please select a stone that exists on the board")
            
        pos = input("Please select a position")
            
        while(not(self.ui.legal_move(pos))):
            pos = input("Please, a valid position or type x to change the selected stone")
            if(pos == "x"):
                return"x"        
        
        result = [stone,pos]
        
        return(result)  
    

'''
    def move(self):
        self.turn += 1
        self.ui.print_board()
        print("\n") 
        print("To move type the the stone you wish to move, e.g. B4")

        if(self.turn % 2 == 1):
            print("Its " + self.player_one["name"] +"'s turn! Please pick a black stone.\n")
        else:
            print("Its " + self.player_one["name"] +"'s turn! Please pick a white stone. \n")
        
        stone = self.stone_exists() #pick stone
        print("stone first assign: "+ stone)
        stone_color = self.ui.black_white(stone) 
        print("\n")
        if(self.turn % 2 == 1): #black's turn 
            pos_and_stone = self.move_is_legal(stone, "", "b")  
            pos = pos_and_stone[0]
            stone = pos_and_stone[1]
            print("stone again : " + stone)
        else: #white's turn
            pos_and_stone = self.move_is_legal(stone, "", "w") 
            pos = pos_and_stone[0]
            stone = pos_and_stone[1]
            print("stone again : " + stone)
        
        mydict = self.ui.values
        oldpos = list(mydict.keys())[list(mydict.values()).index(stone)] 


        print("\n")
        self.ui.move_stone(stone, pos, oldpos)
        #check mill
        print("turn: "+ str(self.turn))
        self.move()


    def move_is_legal(self, stone, pos, color): #returns a position and stone to move
        #stone_color = self.ui.black_white(stone) 
        while(not(stone_color == color)):
            print("Select one of your stones, not your opponents! \n")
            stone = self.stone_exists()
            print("3 stone: " + stone)
            stone_color = self.ui.black_white(stone)
        pos = input("Select position you wish to move stone to: \n")
        print("pos: " + pos)   
        while(not(self.ui.legal_move(pos))):
            if(not(pos in self.ui.values.keys())):
                print("Position does not exist")
            pos = input("Not legal move. Enter another position or x to pick new stone: \n")
            if(pos == "x"): 
                break
                print("hej")
                stone = self.stone_exists()
                self.move_is_legal(stone, "", color)
                    
        if(not (pos == "x")): 
            print("returning: " + pos + stone)
            return [pos, stone] 
        


    def stone_exists(self): #returns stone when input has entered a stone that exists
        print("\n")
        stone = input("Pick a stone to move:")
        while(not(stone in self.ui.values.values())):
            stone = input("Not a valid stone to pick! Try again")
        return stone
'''


            
    #def end_game(self):
        #determines if the game is to end
        #player has zero stones/player cant move -> opponent wins
        #certain amount of turns have passed -> it's a tie 



obj = game_manager()
obj.init_game()
