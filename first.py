from userinterface import userinterface
#from _operator import pos

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
    winner = None

    def init_game(self):
        print("So you want to play huh?")
        #print("Press 1 or 2 to pick game mode")
        #we should catch exceptions in reasonable way
        choice = input("Play versus player(1) or play versus computer(2) or jumo to phase 2(3) or jump to phase 3(4):")
        if choice == "2":
            print("Game mode not supported in this version.")
            self.init_game()

        elif choice == "1":
            player1 = input("Enter name for player 1: ")
            player2 = input("Enter name for player 2: ")
            self.player_one["name"] = player1
            self.player_two["name"] = player2
            print("Game starting up ...")
            print(player1 ,"is black, ", player2 , " is white.")
            print("\n")
            self.game_loop()
        
        elif choice == "4": # Phase 3
            self.ui.values={"a1":"B1", "d1":"0 ", "g1":"0 ", 
                    "b2":"B5", "d2":"0 ", "f2":"W5", 
                    "c3":"0 ", "d3":"0 ", "e3":"0 ", 
                    "a4":"0 ", "b4":"B2", "c4":"0 ", "e4":"0 ","f4":"0 ", "g4":"0 ", 
                    "c5":"0 ", "d5":"0 ", "e5":"0 ", 
                    "b6":"B6", "d6":"0 ", "f6":"W6", 
                    "a7":"B3", "d7":"0 ", "g7":"W4"}
            self.ui.values_for_mill={'a1':"B", 'd1':1, 'g1':0, 
                             'b2':"B", 'd2':0, 'f2':"W", 
                             'c3':0, 'd3':1, 'e3':0, 
                             'a4':1, 'b4':"B", 'c4':1, 'e4':1, 'f4':0, 'g4':1, 
                             'c5':0, 'd5':1, 'e5':0, 
                             'b6':"B", 'd6':0, 'f6':"W", 
                             'a7':"B", 'd7':1, 'g7':"W"}
            self.turn = 28
            self.player_one["stones"] = 5
            self.player_two["stones"] = 3
            self.player_one["name"] = "Player_1"
            self.player_two["name"] = "Player_2"
            self.game_loop()

        elif choice == "3": # Phase 2
            self.ui.values={"a1":"B1", "d1":"B9", "g1":"W1", 
                    "b2":"B5", "d2":"0 ", "f2":"W5", 
                    "c3":"B7", "d3":"0 ", "e3":"W7", 
                    "a4":"B2", "b4":"0 ", "c4":"0 ", "e4":"0 ","f4":"0 ", "g4":"W3", 
                    "c5":"B8", "d5":"0 ", "e5":"W8", 
                    "b6":"B6", "d6":"0 ", "f6":"W6", 
                    "a7":"B3", "d7":"W9", "g7":"W4"}
            self.ui.values_for_mill={'a1':"B", 'd1':"B", 'g1':"W", 
                             'b2':"B", 'd2':0, 'f2':"W", 
                             'c3':"B", 'd3':1, 'e3':"W", 
                             'a4':"B", 'b4':0, 'c4':1, 'e4':1, 'f4':0, 'g4':"W", 
                             'c5':"B", 'd5':1, 'e5':"W", 
                             'b6':"B", 'd6':0, 'f6':"W", 
                             'a7':"B", 'd7':"W", 'g7':"W"}
            self.player_one["stones"] = 8
            self.player_two["stones"] = 8
            self.player_one["name"] = "Player_1"
            self.player_two["name"] = "Player_2"
            self.turn = 19
            self.game_loop()
       
        else:
            print("Wrong input, try again.")
            self.init_game()

    def game_loop(self):        
        while(self.turn < 19):
            print("Game in Phase 1 :")
            self.place()
            self.turn += 1

        while((self.player_one["stones"] >= 3) and (self.player_two["stones"] >= 3)):
            # if one of the player has only 3 stones, then he/she can use fly() function.
            if(self.player_one["stones"] == 3 or self.player_two["stones"] == 3):
                self.fly()
                self.turn += 1
            else:
                print("Game in Phase 2 :")
                self.move()
                self.turn += 1
            if(self.end_of_game()):
                break
        if(self.player_one["stones"] < 3):
            print(self.player_one["name"] + " have only 2 stones! " + self.player_two["name"] + " WIN !!")
            print("End of game yo!")
            self.winner = 2

        elif(self.player_two["stones"] < 3):
            print(self.player_two["name"] + " have only 2 stones! " + self.player_one["name"] + " WIN !!")
            print("End of game yo!")
            self.winner = 1

    def end_of_game(self):
        black_way_to_go = 0
        white_way_to_go = 0

        for x in range(0, 24):
            m_color = list(self.ui.values_for_mill.values())[x]

            if(m_color == "W"):
                m_pos = list(self.ui.values_for_mill.keys())[x]
                length = len(self.ui.connections[m_pos])

                for y in range(0, length):
                    scan_pos = self.ui.connections[m_pos][y]

                    if(self.ui.values_for_mill[scan_pos] == 0 or self.ui.values_for_mill[scan_pos] == 1):
                        white_way_to_go += 1
            else:
                m_pos = list(self.ui.values_for_mill.keys())[x]
                length = len(self.ui.connections[m_pos])

                for y in range(0, length):
                    scan_pos = self.ui.connections[m_pos][y]

                    if(self.ui.values_for_mill[scan_pos] == 0 or self.ui.values_for_mill[scan_pos] == 1):
                        black_way_to_go += 1

        if(black_way_to_go == 0):
            print("BLACK can not move any more! " + self.player_two["name"] + " WIN !!")
            self.winner = 2
            return True
        elif(white_way_to_go == 0):
            print("WHITE can not move any more! " + self.player_one["name"] + " WIN !!")
            self.winner = 1
            return True
        else:
            return False
        '''    
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
        '''
    def place(self):
        self.ui.print_board()
        print("\n")
        print("Now is " + str(self.turn) + " turn(s).")
        if(self.turn % 2 == 1):
            print("Its " + self.player_one["name"] +"'s turn! Please place a BLACK stone.\n")
        else:
            print("Its " + self.player_two["name"] +"'s turn! Please place a WHITE stone. \n")
        
        print("Enter the position you want to place a stone in, f.e g7.")
        place = input("Position : ")
        if(self.ui.legal_move(place)):
            if(self.turn % 2 == 1):
                self.ui.make_move(place, "B"+ str(int((self.turn + 1) / 2)))
                self.ui.mill_state(place, "B") #shang add
                self.player_one["stones"] += 1
                self.black_stones += 1 #shang add                
            
            else:
                self.ui.make_move(place, "W"+ str(int((self.turn + 1) / 2)))
                self.ui.mill_state(place, "W") #shang add
                self.player_two["stones"] += 1
                self.white_stones += 1 #shang add

            self.mill(place)
        else:
            print("The move you are trying to make is not legal! Try again!")
            self.place()
                        
    def move(self):
        self.ui.print_board()
        print("\n")
        result = "x"
        print("Now is " + str(self.turn) + " turn(s). \n")
        print("To move type the the stone you wish to move, e.g. B4")
        
        
        if(self.turn % 2 == 1):
            print("Its " + self.player_one["name"] +"'s turn! Please pick a BlACK stone.\n")
            
            while(result == "x"):
                result = self.move_algorithm()
            
        else:
            print("Its " + self.player_two["name"] +"'s turn! Please pick a WHITE stone. \n")
            
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

    def move_algorithm(self): # return [stone, pos]
        if(self.turn % 2 == 1): # black turn
            stone = input("Please select a stone that is BLACK : ")
            color = self.ui.black_white(stone) # detect the color being choosed.
            
            #while(not(self.ui.black_white(stone) == color)):
            while(not("b" == color)):
                stone = input("Please select a stone that is BLACK again : ")
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
            stone = input("Please select a stone that is WHITE : ")
            color = self.ui.black_white(stone) # detect the color being choosed.
            
            #while(not(self.ui.black_white(stone) == color)):
            while(not("w" == color)):
                stone = input("Please select a stone that is WHITE again : ")
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
            
    def mill(self, place):
        if(self.player_one["stones"] > 2 or self.player_two["stones"] > 2): #shang add

            if(self.turn % 2 == 1): # To tell Black or White player
                mill_number = self.ui.check_mill("B", place) # To check how many mill for Black
                if(mill_number != 0): # If there is any mill be created
                    print("You get " + str(mill_number) + " mill! And you can remove WHITE stone(s) from board.\n")
                        
                    while(mill_number != 0): # To make sure every mill have been used to remove the stone(s)
                        pos = input("Enter the position of the stone you want to remove :")
                        if(pos in self.ui.values.keys()):
                            if(self.ui.values_for_mill[pos] == "W"): # Make sure you are not trying to remove your own stone
                                remove_check_mill_number = self.ui.check_mill("W", pos)

                                switch = 0
                                if(remove_check_mill_number == 0): # pos is not in a mill
                                    self.ui.remove_stone(pos)
                                    mill_number -= 1
                                    self.white_stones -= 1
                                    self.player_two["stones"] -= 1

                                else: # pos is in mill
                                    for x in range(0,24):
                                        m_color = list(self.ui.values_for_mill.values())[x]
                                        if(m_color == "W"):
                                            m_pos = list(self.ui.values_for_mill.keys())[x]
                                            check = self.ui.check_mill("W", m_pos)
                                            if(check == 0):
                                                switch += 1
                                    if(switch > 0):
                                        print("You need to remove the stone not in a mill first!")
                                        self.mill(pos)
                                    else:
                                        self.ui.remove_stone(pos)
                                        mill_number -= 1
                                        self.white_stones -= 1
                                        self.player_two["stones"] -= 1                                    
                            else:
                                print("You are trying to remove your own stone, try again!")
                        else:
                            print("The move you are trying to make is not legal! Try again!")
            else: # To tell Black or White player
                mill_number = self.ui.check_mill("W", place) # To check how many mill for White
                if(mill_number != 0):
                    print("You get " + str(mill_number) + " mill! And you can remove BLACK stone(s) from board.\n")
                        
                    while(mill_number != 0):
                        pos = input("Enter the position of the stone you want to remove :")
                        if(pos in self.ui.values.keys()):
                            if(self.ui.values_for_mill[pos] == "B"):
                                remove_check_mill_number = self.ui.check_mill("B", pos)

                                switch = 0
                                if(remove_check_mill_number == 0): # pos is not in a mill
                                    self.ui.remove_stone(pos)
                                    mill_number -= 1
                                    self.black_stones -= 1
                                    self.player_one["stones"] -= 1

                                else: # pos is in mill
                                    for x in range(0,24):
                                        m_color = list(self.ui.values_for_mill.values())[x]
                                        if(m_color == "B"):
                                            m_pos = list(self.ui.values_for_mill.keys())[x]
                                            check = self.ui.check_mill("B", m_pos)
                                            if(check == 0):
                                                switch += 1 
                                    if(switch > 0):
                                        print("You need to remove the stone not in a mill first!")
                                        self.mill(pos)
                                    else:
                                        self.ui.remove_stone(pos)
                                        mill_number -= 1
                                        self.black_stones -= 1
                                        self.player_one["stones"] -= 1
                            else:
                                print("You are trying to remove your own stone, try again!")
                        else:
                            print("The move you are trying to make is not legal! Try again!")

    def fly(self):
        self.ui.print_board()
        print("\n")
        lvl = [6,4,2]
        listOfLevels = {"a1":lvl[0], "d1":lvl[0], "g1":lvl[0], "g4":lvl[0], "g7":lvl[0], "d7":lvl[0], "a7":lvl[0], "a4":lvl[0],
                       "b2":lvl[1], "d2":lvl[1], "f2":lvl[1], "f4":lvl[1], "f6":lvl[1], "d6":lvl[1], "b6":lvl[1], "b4":lvl[1],
                       "c3":lvl[2], "d3":lvl[2], "e3":lvl[2], "e4":lvl[2], "e5":lvl[2], "d5":lvl[2], "c5":lvl[2], "c4":lvl[2]}
        
        if(self.turn % 2 == 1): # black turn
            if(self.player_one["stones"] == 3):
                print("Now is " + str(self.turn) + " turn(s).")
                print("Black enter Phase3 : ")
                stone = input("Enter a BLACK stone you want to move. (i.e. B4) : ")                
                if(stone[0] == 'B' and self.ui.contains(stone)):
                    pos = list(self.ui.values.keys())[list(self.ui.values.values()).index(stone)] #current position of stone
                    des = input("Enter the place you want to go. (i.e. f6) : ")
                    if(des in self.ui.values.keys()):                    
                        if(self.fly_alg(pos, des) == True):
                            self.ui.move_stone(stone, des, pos)
                            self.ui.mill_state(des, "B") #shang add
                            self.ui.values_for_mill[pos] = 0 #shang add
                            self.mill(des) #shang add
                        else:
                            print("This move is illegal, please try again. \n")
                            self.fly()
                    else:
                        print("Choose the position on the board, please try again. \n")
                        self.fly()                                            
                else:
                    print("You can only move BLACK stone, please try again. \n")
                    self.fly()
            else:
                self.move()

        else: # white turn
            if(self.player_two["stones"] == 3):
                print("Now is " + str(self.turn) + " turn(s).")
                print("White enter Phase3 : ")
                stone = input("Enter a WHITE stone you want to move. (i.e. W7) : ")
                if(stone[0] == 'W' and self.ui.contains(stone)):
                    pos = list(self.ui.values.keys())[list(self.ui.values.values()).index(stone)] #current position of stone
                    des = input("Enter the place you want to go. (i.e. f6) : ")
                    if(des in self.ui.values.keys()):                    
                        if(self.fly_alg(pos, des) == True):
                            self.ui.move_stone(stone, des, pos)
                            self.ui.mill_state(des, "W") #shang add
                            self.ui.values_for_mill[pos] = 0 #shang add
                            self.mill(des) #shang add
                        else:
                            print("This move is illegal, please try again. \n")
                            self.fly()
                    else:
                        print("Choose the position on the board, please try again. \n")
                        self.fly()
                else:
                    print("You can only move WHITE stone, please try again. \n")
                    self.fly()
            else:
                self.move()

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
                                    elif(pos == des[0] + str(4)):
                                        return True
                                    else:
                                        print("There is a stone between you and destination. Try again!\n")
                                        self.fly()
                                else: # if on 'd' column
                                    if(int(des[1]) <= 3): # between d1 - d3
                                        if(self.ui.values_for_mill['d2'] != "B" and self.ui.values_for_mill['d2'] != "W"):
                                            #if(abs(int(des[1]) - int(pos[1])) == 2):
                                            if(abs(int(des[1]) - int(pos[1])) <= 2):
                                                # legal to fly6
                                                return True
                                        elif(pos == 'd2'):
                                            return True
                                        else:
                                            print("There is a stone between you and destination. Try again!\n")
                                            self.fly()
                                    else: # between d5 - d7
                                        if(self.ui.values_for_mill['d6'] != "B" and self.ui.values_for_mill['d6'] != "W"):
                                            #if(abs(int(des[1]) - int(pos[1])) == 2):
                                            if(abs(int(des[1]) - int(pos[1])) <= 2):
                                                # legal to fly
                                                return True
                                        elif(pos == 'd6'):
                                            return True
                                        else:
                                            print("There is a stone between you and destination. Try again!\n")
                                            self.fly()
                            else: # row fly
                                if(des[1] != '4'): # if not on '4' row
                                    if(self.ui.values_for_mill['d' + des[1]] != "B" and self.ui.values_for_mill['d' + des[1]] != "W"):
                                        #if(abs(ord(des[0]) - ord(pos[0])) >= 2):
                                        if(abs(ord(des[0]) - ord(pos[0])) >= 1):
                                            # legal to fly
                                            return True
                                    elif('d' + des[1]):
                                        return True
                                    else:
                                        print("There is a stone between you and destination. Try again!\n")
                                        self.fly()
                                else: # if on '4' row
                                    if(ord(des[0]) <= 99): # between a4 - c4
                                        if(self.ui.values_for_mill['b4'] != "B" and self.ui.values_for_mill['b4'] != "W"):
                                            #if(abs(ord(des[0]) - ord(pos[0])) == 2):
                                            if(abs(ord(des[0]) - ord(pos[0])) <= 2):
                                                # legal to fly
                                                return True
                                        elif(pos == 'b4'):
                                            return True
                                        else:
                                            print("There is a stone between you and destination. Try again!\n")
                                            self.fly()
                                    else: # between e4 - g4
                                        if(self.ui.values_for_mill['f4'] != "B" and self.ui.values_for_mill['f4'] != "W"):
                                            #if(abs(ord(des[0]) - ord(pos[0])) == 2):
                                            if(abs(ord(des[0]) - ord(pos[0])) <= 2):
                                                # legal to fly
                                                return True
                                        elif(pos == 'f4'):
                                            return True
                                        else:
                                            print("There is a stone between you and destination. Try again!\n")
                                            self.fly()
                        else:
                            print("The destination you choose is illegal.")
                            return False
                    else:
                        print("Please choose a clean position.")
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
                                    elif(pos == des[0] + str(4)):
                                        return True
                                    else:
                                        print("There is a stone between you and destination. Try again!")
                                        self.fly()
                                else: # if on 'd' column
                                    if(int(des[1]) <= 3): # between d1 - d3
                                        if(self.ui.values_for_mill['d2'] != "B" and self.ui.values_for_mill['d2'] != "W"):
                                            if(abs(int(des[1]) - int(pos[1])) <= 2):
                                                # legal to fly
                                                return True
                                        elif(pos == 'd2'):
                                            return True
                                        else:
                                            print("There is a stone between you and destination. Try again!")
                                            self.fly()
                                    else: # between d5 - d7
                                        if(self.ui.values_for_mill['d6'] != "B" and self.ui.values_for_mill['d6'] != "W"):
                                            if(abs(int(des[1]) - int(pos[1])) <= 2):
                                                # legal to fly
                                                return True
                                        elif(pos == 'd6'):
                                            return True
                                        else:
                                            print("There is a stone between you and destination. Try again!")
                                            self.fly()
                            else: # row fly
                                if(des[1] != '4'): # if not on '4' row
                                    if(self.ui.values_for_mill['d' + des[1]] != "B" and self.ui.values_for_mill['d' + des[1]] != "W"):
                                        if(abs(ord(des[0]) - ord(pos[0])) >= 1):
                                            # legal to fly
                                            return True
                                    elif(pos == 'd' + des[1]):
                                        return True
                                    else:
                                        print("There is a stone between you and destination. Try again!")
                                        self.fly()
                                else: # if on '4' row
                                    if(ord(des[0]) <= 99): # between a4 - c4
                                        if(self.ui.values_for_mill['b4'] != "B" and self.ui.values_for_mill['b4'] != "W"):
                                            if(abs(ord(des[0]) - ord(pos[0])) <= 2):
                                                # legal to fly
                                                return True
                                        elif(pos == 'b4'):
                                            return True
                                        else:
                                            print("There is a stone between you and destination. Try again!")
                                            self.fly()
                                    else: # between e4 - g4
                                        if(self.ui.values_for_mill['f4'] != "B" and self.ui.values_for_mill['f4'] != "W"):
                                            if(abs(ord(des[0]) - ord(pos[0])) <= 2):
                                                # legal to fly
                                                return True
                                        elif(pos == 'f4'):
                                            return True
                                        else:
                                            print("There is a stone between you and destination. Try again!")
                                            self.fly()
                        else:
                            print("The destination you choose is illegal.")
                            return False
                    else:
                        print("Please choose a clean position.")
                        return False
                else:
                    print("You need to choose a black stone.")
                    return False
        #else:
        return False

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

#obj = game_manager()
#obj.init_game()
#print("winner: %d" %obj.winner)
