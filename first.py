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
        choice = input("Play versus player (1) or play versus computer(2) or run end of phase 1(4) or run end of phase 2 (3):")
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
            self.game_loop()
        
        if choice == "4":
            self.ui.values = {"a1":"B1", "d1":"W1", "g1":"B2", "e1":"W2", "b2":"W3", "d2":"B3", 
            "f2":"0 ", "c3":"0 ", "d3":"0 ", "e3":"0 ", "a4":"0 ", "b4":"W4", "c4":"B4", 
            "e4":"0 ", "f4":"B8", "g4":"B6", "c5":"W6", "d5":"B7",
            "e5":"0 ", "b6":"W8","d6":"W7", "f6":"0 ", "a7":"0 ", "d7":"W5", "g7":"B5"}
            self.turn = 16
            self.player_one["stones"] = 8
            self.player_two["stones"] = 8
            self.game_loop()

        if choice == "3":
            self.ui.values = {"a1":"B1", "d1":"W1", "g1":"0 ", "e1":"W2", "b2":"0 ", "d2":"0 ", 
            "f2":"B3", "c3":"0 ", "d3":"0 ", "e3":"0 ", "a4":"0 ", "b4":"W4", "c4":"B4", 
            "e4":"B9", "f4":"0 ", "g4":"B6", "c5":"0 ", "d5":"B7",
            "e5":"0 ", "b6":"W8","d6":"W7", "f6":"0 ", "a7":"W9", "d7":"W5", "g7":"0 "}
            self.player_one["stones"] = 9
            self.player_two["stones"] = 9
            self.turn = 34
            print("Turn 34, some turns into phase 2")
       
        else:
            print("Wrong input, try again")
            self.init_game()
    
    def game_loop(self):
        while(self.turn < 18):
            self.place()
        
        while((self.player_one["stones"] > 3) or (self.player_two["stones"] > 3)):
            self.move()
            if(self.end_of_game):
                print("End of game yo!")
                break

    def end_of_game(self):
        #if stones <2: return true
        #kolla alla stenars position
        #för varje sten: kollar connects'värden
        #om det finns något värde som är 0 -> return true
        #annars retrun false

        if((self.player_one["stones"] < 3) or (self.player_two["stones"] < 3)):
            print("A player has less than 3 stones left")
            return True
            
        keylist = []
        for x in range(1,9):
            for (key, value) in self.ui.values.items():
                if value == ("W" + str(x)):
                    keylist.append(key) #put every position where player has a stone in list
        
        for key in keylist: #for each position, check the positions connections
            for connect in self.ui.connections[key]: #for each connection
                if("0 " in self.ui.values[connect]): #check if value == "0 "
                    return True
        return False



    def place(self):
        self.ui.print_board()
        print("\n")
        self.turn += 1
        if(self.turn % 2 == 1):
            print("Its " + self.player_one["name"] +"'s turn! Please place a black stone.\n")
        else:
            print("Its " + self.player_two["name"] +"'s turn! Please place a white stone. \n")
        
        print("To place a stone type the position you want to place a stone in, f.e g7. \n")
        place = input("Place stone: \n")
        if(self.ui.legal_move(place)):
            if(self.turn % 2 == 1):
                self.ui.make_move(place, "B"+ str(self.player_one["stones"] + 1))
                self.player_one["stones"] += 1
            
            else:
                self.ui.make_move(place, "W" + str(self.player_two["stones"] + 1))
                self.player_two["stones"] += 1
            
           # if((self.player_one["stones"] > 8) and (self.player_two["stones"] > 8)):
               # self.phase = 2
                
            
            
            
    def move(self):
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
            
        while(not(self.ui.legal_move_2(stone,pos))):
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
