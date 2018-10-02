from userinterface import userinterface
from _operator import pos

class game_manager:
    phase = 1
    player_one = {"name": "", "color": "black", "stones": 0}
    player_two = {"name": "", "color": "white", "stones": 0}
    turn = 1
    mill_number = 0 #shang
    remove_check_mill_number = 0 #shang
    black_stones = 0 #shang
    white_stones = 0 #shang
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
        print("Enter Phase1 :")
        while(self.turn < 19):
            print("Now is " + str(self.turn) + " turn(s).")
            self.place()
            self.turn += 1
        print("Enter Phase2 :")
        while((self.player_one["stones"] >= 3) and (self.player_two["stones"] >= 3)):
            # if one of the player has only 3 stones, then he/she can use fly() function.
            if(self.player_one["stones"] == 3 or self.player_two["stones"] == 3):
                print("Now is " + str(self.turn) + " turn(s).")
                self.fly()
                self.turn += 1
            else:
                print("Now is " + str(self.turn) + " turn(s).")
                self.move()
                self.turn += 1
            ''' # end_of_game need to be fixed, so I block it first.
            if(self.end_of_game):
                print("End of game yo!")
                break
            '''

    def end_of_game(self):
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
        if(self.turn % 2 == 1):
            print("Its " + self.player_one["name"] +"'s turn! Please place a black stone.\n")
        else:
            print("Its " + self.player_two["name"] +"'s turn! Please place a white stone. \n")
        
        print("To place a stone type the position you want to place a stone in, f.e g7.")
        place = input("Place stone: \n")
        if(self.ui.legal_move(place)):
            if(self.turn % 2 == 1):
                #self.ui.make_move(place, "B"+ str(self.player_one["stones"] + 1))
                self.ui.make_move(place, "B"+ str(int((self.turn + 1) / 2)))
                self.ui.mill_state(place, "B") #shang add
                self.player_one["stones"] += 1
                self.black_stones += 1 #shang add                
            
            else:
                #self.ui.make_move(place, "W" + str(self.player_two["stones"] + 1))
                self.ui.make_move(place, "W"+ str(int((self.turn + 1) / 2)))
                self.ui.mill_state(place, "W") #shang add
                self.player_two["stones"] += 1
                self.white_stones += 1 #shang add

            self.mill(place)
        else:
            print("The move you are trying to make is not legal! Try again")
            self.place()
                        
    def move(self):
        result = "x"
        print("\n") 
        print("To move type the the stone you wish to move, e.g. B4")
        
        
        if(self.turn % 2 == 1):
            print("Its " + self.player_one["name"] +"'s turn! Please pick a black stone.\n")
            
            while(result == "x"):
                result = self.move_algorithm()
            
        else:
            print("Its " + self.player_two["name"] +"'s turn! Please pick a white stone. \n")
            
            while(result == "x"):
                 result = self.move_algorithm()
                 
        mydict = self.ui.values
        oldpos = list(mydict.keys())[list(mydict.values()).index(result[0])]    
        self.ui.move_stone(result[0], result[1], oldpos)

        if(self.turn % 2 == 1):
            self.ui.mill_state(result[1], "B") #shang add
        else:
            self.ui.mill_state(result[1], "W") #shang add
        self.ui.values_for_mill[oldpos] = 0 #shang add
        self.mill(result[1]) #shang add
            
    def mill(self, place):
        if(self.player_one["stones"] > 2 or self.player_two["stones"] > 2): #shang add

            if(self.turn % 2 == 1): # To tell Black or White player
                mill_number = self.ui.check_mill("B", place) # To check how many mill for Black
                if(mill_number != 0): # If there is any mill be created
                    print("You get " + str(mill_number) + " mill! And you can remove white stone(s) from board.")
                        
                    while(mill_number != 0): # To make sure every mill have been used to remove the stone(s)
                        pos = input("Enter the position of the stone you want to remove :")
                        if(pos in self.ui.values.keys()):
                            if(self.ui.values_for_mill[pos] == "W"): # Make sure you are not trying to remove your own stone
                                remove_check_mill_number = self.ui.check_mill("W", pos)
                                if(remove_check_mill_number == 0): # pos is not in a mill
                                    self.ui.remove_stone(pos)
                                    mill_number -= 1
                                    self.white_stones -= 1
                                    self.player_two["stones"] -= 1
                                elif(remove_check_mill_number == 1): # pos is in a mill
                                    if(self.white_stones < 4): # if less than 4 stones
                                        self.ui.remove_stone(pos)
                                        mill_number -= 1
                                        self.white_stones -= 1
                                        self.player_two["stones"] -= 1
                                    else:
                                        print("You need to remove the stone not in a mill first!")
                                else: # pos is in two mill
                                    if(self.white_stones < 6): # if less than 6 stones
                                        self.ui.remove_stone(pos)
                                        mill_number -= 1
                                        self.white_stones -= 1
                                        self.player_two["stones"] -= 1
                                    else:
                                        print("You need to remove the stone not in a mill first!")
                            else:
                                print("You are trying to remove your own stone, try again!")
                        else:
                            print("The move you are trying to make is not legal! Try again")
                            self.mill(place)
            else: # To tell Black or White player
                mill_number = self.ui.check_mill("W", place) # To check how many mill for White
                if(mill_number != 0):
                    print("You get " + str(mill_number) + " mill! And you can remove black stone(s) from board.")
                        
                    while(mill_number != 0):
                        pos = input("Enter the position of the stone you want to remove :")
                        if(pos in self.ui.values.keys()):
                            if(self.ui.values_for_mill[pos] == "B"):
                                remove_check_mill_number = self.ui.check_mill("B", pos)
                                if(remove_check_mill_number == 0): # pos is not in a mill
                                    self.ui.remove_stone(pos)
                                    mill_number -= 1
                                    self.black_stones -= 1
                                    self.player_one["stones"] -= 1
                                elif(remove_check_mill_number == 1):
                                    if(self.black_stones < 4):
                                        self.ui.remove_stone(pos)
                                        mill_number -= 1
                                        self.blcak_stones -= 1
                                        self.player_one["stones"] -= 1
                                    else:
                                        print("You need to remove the stone not in a mill first!")
                                else:
                                    if(self.black_stones < 6):
                                        self.ui.remove_stone(pos)
                                        mill_number -= 1
                                        self.black_stones -= 1
                                        self.player_one["stones"] -= 1
                                    else:
                                        print("You need to remove the stone not in a mill first!")
                            else:
                                print("You are trying to remove your own stone, try again!")
                        else:
                            print("The move you are trying to make is not legal! Try again")
                            self.mill(place)
           
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
        if(self.turn % 2 == 1): # black turn
            stone = input("Please select a stone that is black : ")
            color = self.ui.black_white(stone) # detect the color being choosed.
            
            #while(not(self.ui.black_white(stone) == color)):
            while(not("b" == color)):
                stone = input("Please select a stone that is black again : ")
                color = self.ui.black_white(stone)
                    
            #Checks if contains. contains gives boolean
            while(not(self.ui.contains(stone))):
                stone = input("Please select a stone that exists on the board : ")
                
            pos = input("Please select the position : ")
                
            while(not(self.ui.legal_move_2(stone, pos))):
                pos = input("Please, a valid position or type x to change the selected stone : ")
                if(pos == "x"):
                    return "x"        
            
            result = [stone, pos]            
            return(result)

        else: # white turn
            stone = input("Please select a stone that is white : ")
            color = self.ui.black_white(stone) # detect the color being choosed.
            
            #while(not(self.ui.black_white(stone) == color)):
            while(not("w" == color)):
                stone = input("Please select a stone that is white again : ")
                color = self.ui.black_white(stone)
                    
            #Checks if contains. contains gives boolean
            while(not(self.ui.contains(stone))):
                stone = input("Please select a stone that exists on the board : ")
                
            pos = input("Please select a position : ")
                
            while(not(self.ui.legal_move_2(stone, pos))):
                pos = input("Please, a valid position or type x to change the selected stone : ")
                if(pos == "x"):
                    return "x"        
            
            result = [stone, pos]            
            return(result)

    
    def fly(self):
        lvl = [6,4,2]
        listOfLevels = {"a1":lvl[0], "d1":lvl[0], "g1":lvl[0], "g4":lvl[0], "g7":lvl[0], "d7":lvl[0], "a7":lvl[0], "a4":lvl[0],
                       "b2":lvl[1], "d2":lvl[1], "f2":lvl[1], "f4":lvl[1], "f6":lvl[1], "d6":lvl[1], "b6":lvl[1], "b4":lvl[1],
                       "c3":lvl[2], "d3":lvl[2], "e3":lvl[2], "e4":lvl[2], "e5":lvl[2], "d5":lvl[2], "c5":lvl[2], "c4":lvl[2]}
        if(self.turn % 2 == 1): # black turn
            if(self.player_one["stones"] == 3):
                print("Black enter Phase3 : ")
                stone = input("Enter a black stone you want to move. (i.e. B4) : ")
                if(stone[0] == 'B'):
                    des = input("Enter the place you want to go. (i.e. f6) : ")
                    pos = list(self.ui.values.keys())[list(self.ui.values.values()).index(stone)] #current position of stone

                    if(self.fly_alg(pos, des) == True):
                        self.ui.move_stone(stone, des, pos)
                        self.ui.mill_state(des, "B") #shang add
                        self.ui.values_for_mill[pos] = 0 #shang add
                        self.mill(des) #shang add
                    else:
                        print("This move is illegal, please try again. \n")
                        self.fly()
                else:
                    print("Only black stone, please try again. \n")
                    self.fly()
            else:
                self.move()

        else: # white turn
            if(self.player_two["stones"] == 3):
                print("White enter Phase3 : ")
                stone = input("Enter a white stone you want to move. (i.e. W7) : ")
                if(stone[0] == 'W'):
                    des = input("Enter the place you want to go. (i.e. f6) : ")
                    pos = list(self.ui.values.keys())[list(self.ui.values.values()).index(stone)] #current position of stone

                    if(self.fly_alg(pos, des) == True):
                        self.ui.move_stone(stone, des, pos)
                        self.ui.mill_state(des, "W") #shang add
                        self.ui.values_for_mill[pos] = 0 #shang add
                        self.mill(des) #shang add
                    else:
                        print("This move is illegal, please try again. \n")
                        self.fly()
                else:
                    print("Only white stone, please try again. \n")
                    self.fly()
            else:
                self.move()

        #self.turn += 1
        #self.ui.print_board()
        '''        
        if(self.player_one["stones"] < 4): # if black has only 3 stones
            print("Fly has now been enabled for " +self.player_one["name"] )
        elif(self.player_two["stones"] < 4): # if white has only 3 stones
            print("Fly has now been enabled for " +self.player_one["name"])
        else: # both black and white have more than 3 stones
            exit()

        result = "x"
        print("\n") 
        print("To move type the the stone you wish to move, e.g. B4")
        
        if(self.turn % 2 == 1): # black turn
            print("Its " + self.player_one["name"] +"'s turn! Please pick a black stone.\n")
            stone = input("Please select a stone : ")
            
            while(not(self.ui.black_white(stone) == "b")): # black_white() return "w" or "b" or "0"
                stone = input("Please select a black stone : ")
            
            while(result == "x"):
                pos = self.ui.values.key(stone) # pos is the position of the stone you choose.
                des = input("Select where you want to move : ")

            ###################    
                
                if(self.ui.detect_fly_attempt(lvl[pos],pos,des)):
                    while(not(fly_alg(pos, des)) or not(self.ui.legal_move_2(stone,des))):
                        des = input("please select a valid destination, or type x to change stone")
                        if(des == "x"):
                            result = "x"
                    result = [stone, des]
                else:
                    result = self.move_algorithm()
                
            # now put stone using the place and remove the old one
        else: # white turn
            print("Its " + self.player_one["name"] +"'s turn! Please pick a white stone. \n")
            stone = input("Please select a stone : ")
            
            while(not(self.ui.black_white(stone) == "w")): # black_white() return "w" or "b" or "0"
                stone = input("Please select a white stone : ")
                
            while(result == "x"):
                pos = self.ui.values.key(stone)
                des = input("Select where you want to move : ")
                
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
        '''        
        
    def selection_process(self):
        print("Its " + self.player_one["name"] +"'s turn! Please pick a black stone.\n")
        stone = input("Please select a stone")
            
        while(self.ui.black_white(stone) == "b"):
            print("Its " + self.player_one["name"] +"'s turn! Please pick a black stone.\n")
            stone = input("Please select a stone")

    def fly_alg(self, pos, des): # pos => the stone you want to fly, des => destination
        if(pos in self.ui.values.keys()): # make sure pos is legal
            player_color = self.ui.values_for_mill[pos] # detect the color, return "B", "W", 0, 1

            if(self.turn % 2 == 1): # black turn
                if(player_color == "B"): # choose to move black stone
                    if(self.ui.values_for_mill[des] != "B" and self.ui.values_for_mill[des] != "W"): # make sure des is clear
                        if(des[0] == pos[0] or des[1] == pos[1]): # make sure on the line

                            if(des[0] == pos[0]): # column fly
                                if(des[0] != 'd'): # if not on 'd' column
                                    # make sure no stone between pos and des
                                    if(self.ui.values_for_mill[des[0] + str(4)] != "B" and self.ui.values_for_mill[des[0] + str(4)] != "W"):
                                        #if(abs(int(des[1]) - int(pos[1])) >= 2):
                                        if(abs(int(des[1]) - int(pos[1])) >= 1):
                                            # legal to fly
                                            return True
                                else: # if on 'd' column
                                    if(des[1] <= 3): # between d1 - d3
                                        if(self.ui.values_for_mill[d2] != "B" and self.ui.values_for_mill[d2] != "W"):
                                            #if(abs(int(des[1]) - int(pos[1])) == 2):
                                            if(abs(int(des[1]) - int(pos[1])) <= 2):
                                                # legal to fly
                                                return True
                                    else: # between d5 - d7
                                        if(self.ui.values_for_mill[d6] != "B" and self.ui.values_for_mill[d6] != "W"):
                                            #if(abs(int(des[1]) - int(pos[1])) == 2):
                                            if(abs(int(des[1]) - int(pos[1])) <= 2):
                                                # legal to fly
                                                return True
                            else: # row fly
                                if(des[1] != '4'): # if not on '4' row
                                    if(self.ui.values_for_mill['d' + des[1]] != "B" and self.ui.values_for_mill['d' + des[1]] != "W"):
                                        #if(abs(ord(des[0]) - ord(pos[0])) >= 2):
                                        if(abs(ord(des[0]) - ord(pos[0])) >= 1):
                                            # legal to fly
                                            return True
                                else: # if on '4' row
                                    if(ord(des[0]) <= 99): # between a4 - c4
                                        if(self.ui.values_for_mill[b4] != "B" and self.ui.values_for_mill[b4] != "W"):
                                            #if(abs(ord(des[0]) - ord(pos[0])) == 2):
                                            if(abs(ord(des[0]) - ord(pos[0])) <= 2):
                                                # legal to fly
                                                return True
                                    else: # between e4 - g4
                                        if(self.ui.values_for_mill[f4] != "B" and self.ui.values_for_mill[f4] != "W"):
                                            #if(abs(ord(des[0]) - ord(pos[0])) == 2):
                                            if(abs(ord(des[0]) - ord(pos[0])) <= 2):
                                                # legal to fly
                                                return True
                        else:
                            print("The destination you choose is illegal.")
                            return False
                    else:
                        print("There is stone between the you and the destination.")
                        return False
                else:
                    print("You need to choose a black stone.")
                    return False

            else: # white turn
                if(player_color == "W"): # choose to move white stone
                    if(self.ui.values_for_mill[des] != "B" and self.ui.values_for_mill[des] != "W"): # make sure des is clear
                        if(des[0] == pos[0] or des[1] == pos[1]): # make sure on the line

                            if(des[0] == pos[0]): # column fly
                                if(des[0] != 'd'): # if not on 'd' column
                                    # make sure no stone between pos and des
                                    if(self.ui.values_for_mill[des[0] + str(4)] != "B" and self.ui.values_for_mill[des[0] + str(4)] != "W"):
                                        if(abs(int(des[1]) - int(pos[1])) >= 1):
                                            # legal to fly
                                            return True
                                else: # if on 'd' column
                                    if(des[1] <= 3): # between d1 - d3
                                        if(self.ui.values_for_mill[d2] != "B" and self.ui.values_for_mill[d2] != "W"):
                                            if(abs(int(des[1]) - int(pos[1])) <= 2):
                                                # legal to fly
                                                return True
                                    else: # between d5 - d7
                                        if(self.ui.values_for_mill[d6] != "B" and self.ui.values_for_mill[d6] != "W"):
                                            if(abs(int(des[1]) - int(pos[1])) <= 2):
                                                # legal to fly
                                                return True
                            else: # row fly
                                if(des[1] != '4'): # if not on '4' row
                                    if(self.ui.values_for_mill['d' + des[1]] != "B" and self.ui.values_for_mill['d' + des[1]] != "W"):
                                        if(abs(ord(des[0]) - ord(pos[0])) >= 1):
                                            # legal to fly
                                            return True
                                else: # if on '4' row
                                    if(ord(des[0]) <= 99): # between a4 - c4
                                        if(self.ui.values_for_mill[b4] != "B" and self.ui.values_for_mill[b4] != "W"):
                                            if(abs(ord(des[0]) - ord(pos[0])) <= 2):
                                                # legal to fly
                                                return True
                                    else: # between e4 - g4
                                        if(self.ui.values_for_mill[f4] != "B" and self.ui.values_for_mill[f4] != "W"):
                                            if(abs(ord(des[0]) - ord(pos[0])) <= 2):
                                                # legal to fly
                                                return True
                        else:
                            print("The destination you choose is illegal.")
                            return False
                    else:
                        print("There is stone between the you and the destination.")
                        return False
                else:
                    print("You need to choose a black stone.")
                    return False
        #else:
        return False    


obj = game_manager()
obj.init_game()
