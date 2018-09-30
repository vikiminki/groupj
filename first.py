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
        self.turn += 1
        self.ui.print_board()
        
        result = "x"
        print("\n") 
        print("To move type the the stone you wish to move, e.g. B4")
        
        
        if(self.turn % 2 == 1):
            print("Its " + self.player_one["name"] +"'s turn! Please pick a black stone.\n")
            
            while(result == "x"):
                result = self.move_algorithm()
            
        else:
            print("Its " + self.player_one["name"] +"'s turn! Please pick a white stone. \n")
            
            while(result == "x"):
                 result = self.move_algorithm()
            
        mydict = self.ui.values
        oldpos = list(mydict.keys())[list(mydict.values()).index(result[0])]    
        self.ui.move_stone(result[0], result[1], oldpos)
            
            
            
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
    
    
    
    def fly(self):
        lvl = [6,4,2]
        listOfLevels = {"a1":lvl[0], "d1":lvl[0], "g1":lvl[0], "g4":lvl[0], "g7":lvl[0], "d7":lvl[0], "a7":lvl[0], "a4":lvl[0],
                       "b2":lvl[1], "d2":lvl[1], "f2":lvl[1], "f4":lvl[1], "f6":lvl[1], "d6":lvl[1], "b6":lvl[1], "b4":lvl[1],
                       "c3":lvl[2], "d3":lvl[2], "e3":lvl[2], "e4":lvl[2], "e5":lvl[2], "d5":lvl[2], "c5":lvl[2], "c4":lvl[2]}
        
        self.turn += 1
        self.ui.print_board()
        
        if(self.player_one["stones"] < 4):
            print("Fly has now been enabled for " +self.player_one["name"] )
        elif(self.player_two["stones"] < 4):
            print("Fly has now been enabled for " +self.player_one["name"])

        result = "x"
        print("\n") 
        print("To move type the the stone you wish to move, e.g. B4")
        
        if(self.turn % 2 == 1):
            print("Its " + self.player_one["name"] +"'s turn! Please pick a black stone.\n")
            stone = input("Please select a stone")
            
            while(not(self.ui.black_white(stone) == "b")):
                stone = input("Please select a stone")
            
            while(result == "x"):
                pos = self.ui.values.key(stone)
                des = input("Select where you want to move")
                
                if(self.ui.detect_fly_attempt(lvl[pos],pos,des)):
                    while(not(fly_alg(pos, des)) or not(self.ui.legal_move_2(stone,des))):
                        des = input("please select a valid destination, or type x to change stone")
                        if(des == "x"):
                            result = "x"
                    result = [stone, des]
                else:
                    result = self.move_algorithm()
                
            # now put stone using the place and remove the old one
        else:
            print("Its " + self.player_one["name"] +"'s turn! Please pick a white stone. \n")
            stone = input("Please select a ston")
            
            while(not(self.ui.black_white(stone) == "w")):
                stone = input("Please select a stone")
                
            while(result == "x"):
                pos = self.ui.values.key(stone)
                des = input("Select where you want to move")
                
                if(self.ui.detect_fly_attempt(lvl[pos],pos,des)):
                    while(not(fly_alg(pos, des)) or not(self.ui.legal_move_2(stone,des))):
                        des = input("please select a valid destination, or type x to change stone")
                        if(des == "x"):
                            result = "x"
                    result = [stone, des]
                else:
                    result = self.move_algorithm()
         
           
        mydict = self.ui.values
        oldpos = list(mydict.keys())[list(mydict.values()).index(result[0])]
        self.ui.move_stone(result[0], result[1], oldpos)
        
        
    def selection_process(self):
        print("Its " + self.player_one["name"] +"'s turn! Please pick a black stone.\n")
        stone = input("Please select a stone")
            
        while(self.ui.black_white(stone) == "b"):
            print("Its " + self.player_one["name"] +"'s turn! Please pick a black stone.\n")
            stone = input("Please select a stone")
            
        
            
                
                
        
    def fly_alg(self, pos, des): # pos => the stone you want to fly, des => destination
        if(pos in self.ui.values.keys()): # make sure pos is legal
            player_color = self.ui.values_for_mill[pos] # detect the color
            if(self.turn % 2 == 1): # black turn
                if(player_color == "B"): # choose to move black stone
                    if(self.ui.values_for_mill[des] != "B" and self.ui.values_for_mill[des] != "W"): # make sure des is clear
                        if(des[0] == pos[0] or des[1] == pos[1]): # make sure on the line
                            if(des[0] == pos[0]): # column fly
                                if(des[0] != 'd'): # if not on 'd' column
                                    # make sure no stone between pos and des
                                    if(self.ui.values_for_mill[des[0] + str(4)] != "B" and self.ui.values_for_mill[des[0] + str(4)] != "W"):
                                        if(abs(int(des[1]) - int(pos[1])) >= 2):
                                            # legal to fly
                                            return True
                                else: # if on 'd' column
                                    if(des[1] <= 3): # between d1 - d3
                                        if(self.ui.values_for_mill[d2] != "B" and self.ui.values_for_mill[d2] != "W"):
                                            if(abs(int(des[1]) - int(pos[1])) == 2):
                                                # legal to fly
                                                return True
                                    else: # between d5 - d7
                                        if(self.ui.values_for_mill[d6] != "B" and self.ui.values_for_mill[d6] != "W"):
                                            if(abs(int(des[1]) - int(pos[1])) == 2):
                                                # legal to fly
                                                return True
                            else: # row fly
                                if(des[1] != '4'): # if not on '4' row
                                    if(self.ui.values_for_mill[d + des[1]] != "B" and self.ui.values_for_mill[d + des[1]] != "W"):
                                        if(abs(ord(des[0]) - ord(pos[0])) >= 2):
                                            # legal to fly
                                            return True
                                else: # if on '4' row
                                    if(ord(des[0]) <= 99): # between a4 - c4
                                        if(self.ui.values_for_mill[b4] != "B" and self.ui.values_for_mill[b4] != "W"):
                                            if(abs(ord(des[0]) - ord(pos[0])) == 2):
                                                # legal to fly
                                                return True
                                    else: # between e4 - g4
                                        if(self.ui.values_for_mill[f4] != "B" and self.ui.values_for_mill[f4] != "W"):
                                            if(abs(ord(des[0]) - ord(pos[0])) == 2):
                                                # legal to fly
                                                return True        
            else: # white turn
                if(player_color == "W"): # choose to move white stone
                    if(self.ui.values_for_mill[des] != "B" and self.ui.values_for_mill[des] != "W"): # make sure des is clear
                        if(des[0] == pos[0] or des[1] == pos[1]): # make sure on the line
                            if(des[0] == pos[0]): # column fly
                                if(des[0] != 'd'): # if not on 'd' column
                                    # make sure no stone between pos and des
                                    if(self.ui.values_for_mill[des[0] + str(4)] != "B" and self.ui.values_for_mill[des[0] + str(4)] != "W"):
                                        if(abs(int(des[1]) - int(pos[1])) >= 2):
                                            # legal to fly
                                            return True
                                else: # if on 'd' column
                                    if(des[1] <= 3): # between d1 - d3
                                        if(self.ui.values_for_mill[d2] != "B" and self.ui.values_for_mill[d2] != "W"):
                                            if(abs(int(des[1]) - int(pos[1])) == 2):
                                                # legal to fly
                                                return True
                                    else: # between d5 - d7
                                        if(self.ui.values_for_mill[d6] != "B" and self.ui.values_for_mill[d6] != "W"):
                                            if(abs(int(des[1]) - int(pos[1])) == 2):
                                                # legal to fly
                                                return True
                            else: # row fly
                                if(des[1] != '4'): # if not on '4' row
                                    if(self.ui.values_for_mill[d + des[1]] != "B" and self.ui.values_for_mill[d + des[1]] != "W"):
                                        if(abs(ord(des[0]) - ord(pos[0])) >= 2):
                                            # legal to fly
                                            return True
                                else: # if on '4' row
                                    if(ord(des[0]) <= 99): # between a4 - c4
                                        if(self.ui.values_for_mill[b4] != "B" and self.ui.values_for_mill[b4] != "W"):
                                            if(abs(ord(des[0]) - ord(pos[0])) == 2):
                                                # legal to fly
                                                return True
                                    else: # between e4 - g4
                                        if(self.ui.values_for_mill[f4] != "B" and self.ui.values_for_mill[f4] != "W"):
                                            if(abs(ord(des[0]) - ord(pos[0])) == 2):
                                                # legal to fly
                                                return True
        #else:
        return False    


obj = game_manager()
obj.init_game()
