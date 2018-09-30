'''
Created on 14 sep. 2018

@author: Sina
'''

class userinterface:
    occupied = []
    player1 = []
    player2 = []
    values={"a1":"0 ", "d1":"0 ", "g1":"0 ", 
            "b2":"0 ", "d2":"0 ", "f2":"0 ", 
            "c3":"0 ", "d3":"0 ", "e3":"0 ", 
            "a4":"0 ", "b4":"0 ", "c4":"0 ", "e4":"0 ","f4":"0 ", "g4":"0 ", 
            "c5":"0 ", "d5":"0 ", "e5":"0 ", 
            "b6":"0 ","d6":"0 ", "f6":"0 ", 
            "a7":"0 ", "d7":"0 ", "g7":"0 "}
    connections= {"a1": ("a4", "d1"), "d1": ("a1", "g1", "d2"), "g1":("d1", "g4"), 
            "b2":("b4", "d2"), "d2":("b2", "f2", "d1", "d3"), "f2":("d2", "f4"), 
            "c3":("c4", "d3"), "d3":("c3", "e3"), "e3":("d3", "e4"), 
            "a4":("a1", "b4", "a7"), "b4":("a4", "c4", "b2", "b6"), "c4":("b4","c3","c5"), 
            "e4":("e3", "e5"),"f4":("f2", "f6", "e4", "g4"), "g4":("g1", "g7"), 
            "c5":("c4", "d5"), "d5":("c5", "e5", "d6"), "e5":("e4", "d5"), 
            "b6":("b4", "d6"),"d6":("b6", "f6", "d5", "d7"), "f6":("d6", "f4"), 
            "a7":("a4", "d7"), "d7":("a7", "d6", "g7"), "g7":("d7", "g4")}   

    values_for_mill={'a1':0, 'd1':1, 'g1':0, 
                     'b2':1, 'd2':0, 'f2':1, 
                     'c3':0, 'd3':1, 'e3':0, 
                     'a4':1, 'b4':0, 'c4':1, 'e4':1, 'f4':0, 'g4':1, 
                     'c5':0, 'd5':1, 'e5':0, 
                     'b6':1, 'd6':0, 'f6':1, 
                     'a7':0, 'd7':1, 'g7':0}
    
          
    

    def make_move(self, pos, player):
        self.values[pos] = player
        self.print_board()
        print("\n")


    def move_stone(self, stone, newpos, oldpos):
        self.values[oldpos] = "0 " #doenst always seem to work
        self.values[newpos] = stone
    
    def contains(self, stone):
        if(stone in self.values.values()):
            return True
        else:
            return False    

    def legal_move(self, position): #checks if position is free
        legal_position = False
        
        if((position in self.values.keys()) and (self.values[position] == "0 ")):
            legal_position = True
        return(legal_position)

    
    def char_to_value(self,char):
        dict = {"a":1,"b":2, "c":3, "d":4, "e":5, "f":6, "g":7}
        for x in range(0,len(char)):
            if(char[x] == type(str)):
                char[x] = dict(char[x])
                
        
        return(char)
    
    def detect_fly_atempt(self,lvl,old_pos,new_pos):
        char_new = list(new_pos)
        char_old = list(old_pos)
        
        char_trans_new = char_to_value(char_new)
        char_trans_old = char_to_value(char_old)
        
        diff = [char_trans_new[0] - char_trans_old[0], char_trans_new[0] - char_trans_old[1], 
                char_trans_new[1] - char_trans_old[0], char_trans_new[1] - char_trans_old[1]]
    
        if(max(abs(diff)) > lvl - 1):
            fly_mode = True
        else:
            fly_mode = False
            
        return fly_mode
                
        '''
            if(char_new[0]==char_old[0] or char_new[1]==char_old[0] or char_new[0]==char_old[1] or char_new[1]==char_old[1]):
                #this is the condition for fly
         '''   
                
    def legal_move_2(self, stone, dest_position): #checks if position is free & next to the stone
        if(not(self.legal_move(dest_position))):
            return(False)
        positions = self.values
        oldpos = list(positions.keys())[list(positions.values()).index(stone)] #current position of stone
        connections = self.connections[oldpos]

        print("connections: " + connections[0] + connections[1])
        if(dest_position in connections):
            return True
        else:
            return False
        

        
    def black_white(self, stone): 
        if(stone in self.values.values()):
            for x in range(1,9):
                if(("W"+str(x))==stone):
                    result = "w"
                elif(("B"+str(x))==stone):
                    result = "b"
        else:
            result = "0"
        return(result)
          

    def check_mill(self, color, position): #return 0 if no mill, return 1 if mill
        mill_counter = 0

        if(position == 'a1'):
            if(self.values_for_mill['a1'] == self.values_for_mill['d1'] == self.values_for_mill['g1'] == color):
                mill_counter += 1
            if(self.values_for_mill['a1'] == self.values_for_mill['a4'] == self.values_for_mill['a7'] == color):
                mill_counter += 1
            return mill_counter
        elif(position == 'a4'):
            if(self.values_for_mill['a4'] == self.values_for_mill['b4'] == self.values_for_mill['c4'] == color):
                mill_counter += 1
            if(self.values_for_mill['a1'] == self.values_for_mill['a4'] == self.values_for_mill['a7'] == color):
                mill_counter += 1
            return mill_counter
        elif(position == 'a7'):
            if(self.values_for_mill['a7'] == self.values_for_mill['d7'] == self.values_for_mill['g7'] == color):
                mill_counter += 1
            if(self.values_for_mill['a1'] == self.values_for_mill['a4'] == self.values_for_mill['a7'] == color):
                mill_counter += 1
            return mill_counter
        elif(position == 'b2'):
            if(self.values_for_mill['b2'] == self.values_for_mill['d2'] == self.values_for_mill['f2'] == color):
                mill_counter += 1
            if(self.values_for_mill['b2'] == self.values_for_mill['b4'] == self.values_for_mill['b6'] == color):
                mill_counter += 1
            return mill_counter
        elif(position == 'b4'):
            if(self.values_for_mill['a4'] == self.values_for_mill['b4'] == self.values_for_mill['c4'] == color):
                mill_counter += 1
            if(self.values_for_mill['b2'] == self.values_for_mill['b4'] == self.values_for_mill['b6'] == color):
                mill_counter += 1
            return mill_counter
        elif(position == 'b6'):
            if(self.values_for_mill['b6'] == self.values_for_mill['d6'] == self.values_for_mill['f6'] == color):
                mill_counter += 1
            if(self.values_for_mill['b2'] == self.values_for_mill['b4'] == self.values_for_mill['b6'] == color):
                mill_counter += 1
            return mill_counter
        elif(position == 'c3'):
            if(self.values_for_mill['c3'] == self.values_for_mill['d3'] == self.values_for_mill['e3'] == color):
                mill_counter += 1
            if(self.values_for_mill['c3'] == self.values_for_mill['c4'] == self.values_for_mill['c5'] == color):
                mill_counter += 1
            return mill_counter
        elif(position == 'c4'):
            if(self.values_for_mill['a4'] == self.values_for_mill['b4'] == self.values_for_mill['c4'] == color):
                mill_counter += 1
            if(self.values_for_mill['c3'] == self.values_for_mill['c4'] == self.values_for_mill['c5'] == color):
                mill_counter += 1
            return mill_counter
        elif(position == 'c5'):
            if(self.values_for_mill['c5'] == self.values_for_mill['d5'] == self.values_for_mill['e5'] == color):
                mill_counter += 1
            if(self.values_for_mill['c3'] == self.values_for_mill['c4'] == self.values_for_mill['c5'] == color):
                mill_counter += 1
            return mill_counter
        elif(position == 'd1'):
            if(self.values_for_mill['a1'] == self.values_for_mill['d1'] == self.values_for_mill['g1'] == color):
                mill_counter += 1
            if(self.values_for_mill['d1'] == self.values_for_mill['d2'] == self.values_for_mill['d3'] == color):
                mill_counter += 1
            return mill_counter
        elif(position == 'd2'):
            if(self.values_for_mill['b2'] == self.values_for_mill['d2'] == self.values_for_mill['f2'] == color):
                mill_counter += 1
            if(self.values_for_mill['d1'] == self.values_for_mill['d2'] == self.values_for_mill['d3'] == color):
                mill_counter += 1
            return mill_counter
        elif(position == 'd3'):
            if(self.values_for_mill['c3'] == self.values_for_mill['d3'] == self.values_for_mill['e3'] == color):
                mill_counter += 1
            if(self.values_for_mill['d1'] == self.values_for_mill['d2'] == self.values_for_mill['d3'] == color):
                mill_counter += 1
            return mill_counter
        elif(position == 'd5'):
            if(self.values_for_mill['c5'] == self.values_for_mill['d5'] == self.values_for_mill['e5'] == color):
                mill_counter += 1
            if(self.values_for_mill['d5'] == self.values_for_mill['d6'] == self.values_for_mill['d7'] == color):
                mill_counter += 1
            return mill_counter
        elif(position == 'd6'):
            if(self.values_for_mill['b6'] == self.values_for_mill['d6'] == self.values_for_mill['f6'] == color):
                mill_counter += 1
            if(self.values_for_mill['d5'] == self.values_for_mill['d6'] == self.values_for_mill['d7'] == color):
                mill_counter += 1
            return mill_counter
        elif(position == 'd7'):
            if(self.values_for_mill['a7'] == self.values_for_mill['d7'] == self.values_for_mill['g7'] == color):
                mill_counter += 1
            if(self.values_for_mill['d5'] == self.values_for_mill['d6'] == self.values_for_mill['d7'] == color):
                mill_counter += 1
            return mill_counter
        elif(position == 'e3'):
            if(self.values_for_mill['c3'] == self.values_for_mill['d3'] == self.values_for_mill['e3'] == color):
                mill_counter += 1
            if(self.values_for_mill['e3'] == self.values_for_mill['e4'] == self.values_for_mill['e5'] == color):
                mill_counter += 1
            return mill_counter
        elif(position == 'e4'):
            if(self.values_for_mill['e4'] == self.values_for_mill['f4'] == self.values_for_mill['g4'] == color):
                mill_counter += 1
            if(self.values_for_mill['e3'] == self.values_for_mill['e4'] == self.values_for_mill['e5'] == color):
                mill_counter += 1
            return mill_counter
        elif(position == 'e5'):
            if(self.values_for_mill['c5'] == self.values_for_mill['d5'] == self.values_for_mill['e5'] == color):
                mill_counter += 1
            if(self.values_for_mill['e3'] == self.values_for_mill['e4'] == self.values_for_mill['e5'] == color):
                mill_counter += 1
            return mill_counter
        elif(position == 'f2'):
            if(self.values_for_mill['b2'] == self.values_for_mill['d2'] == self.values_for_mill['f2'] == color):
                mill_counter += 1
            if(self.values_for_mill['f2'] == self.values_for_mill['f4'] == self.values_for_mill['f6'] == color):
                mill_counter += 1
            return mill_counter
        elif(position == 'f4'):
            if(self.values_for_mill['e4'] == self.values_for_mill['f4'] == self.values_for_mill['g4'] == color):
                mill_counter += 1
            if(self.values_for_mill['f2'] == self.values_for_mill['f4'] == self.values_for_mill['f6'] == color):
                mill_counter += 1
            return mill_counter
        elif(position == 'f6'):
            if(self.values_for_mill['b6'] == self.values_for_mill['d6'] == self.values_for_mill['f6'] == color):
                mill_counter += 1
            if(self.values_for_mill['f2'] == self.values_for_mill['f4'] == self.values_for_mill['f6'] == color):
                mill_counter += 1
            return mill_counter
        elif(position == 'g1'):
            if(self.values_for_mill['a1'] == self.values_for_mill['d1'] == self.values_for_mill['g1'] == color):
                mill_counter += 1
            if(self.values_for_mill['g1'] == self.values_for_mill['g4'] == self.values_for_mill['g7'] == color):
                mill_counter += 1
            return mill_counter
        elif(position == 'g4'):
            if(self.values_for_mill['e4'] == self.values_for_mill['f4'] == self.values_for_mill['g4'] == color):
                mill_counter += 1
            if(self.values_for_mill['g1'] == self.values_for_mill['g4'] == self.values_for_mill['g7'] == color):
                mill_counter += 1
            return mill_counter
        elif(position == 'g7'):
            if(self.values_for_mill['a7'] == self.values_for_mill['d7'] == self.values_for_mill['g7'] == color):
                mill_counter += 1
            if(self.values_for_mill['g1'] == self.values_for_mill['g4'] == self.values_for_mill['g7'] == color):
                mill_counter += 1
            return mill_counter
        else:
            return 0



    def print_board(self):
            
            print("...a.........b........c.......d........e........f.........g")
            print("1.",self.values["a1"],".......................",self.values["d1"],".......................",self.values["g1"],)
            print("..",".","                         .","                          .")
            print(".",".","                          .","                          .")
            print("2.",".        ",self.values["b2"],".............",self.values["d2"],".............",self.values["f2"],"        .")
            print("..",".","        .                .","                .         .")
            print("..",".","        .                .","                .         .")
            print("..",".","        .                .","                .         .")
            print("3.",".","        .       ",self.values["c3"],"....",self.values["d3"],"....",self.values["e3"],"       .         .")
            print("..",".","        .        .         ","      .        .         .")
            print("..",".","        .        .         ","      .        .         .")
            print("4.",self.values["a4"],"......",self.values["b4"],".....",self.values["c4"],"            ",self.values["e4"],".....",self.values["f4"],"......",self.values["g4"])
            print("..",".","        .        .         ","      .        .         .")
            print("..",".","        .        .         ","      .        .         .")
            print("5.",".","        .       ",self.values["c5"],"....",self.values["d5"],"....",self.values["e5"],"       .         .")
            print("..",".","        .                .","                .         .")
            print("..",".","        .                .","                .         .")
            print("..",".","        .                .","                .         .")
            print("6.",".        ",self.values["b6"],".............",self.values["d6"],".............",self.values["f6"],"        .")
            print("..",".","                         .","                          .")
            print("..",".","                         .","                          .")
            print("7.",self.values["a7"],".......................",self.values["d7"],".......................",self.values["g7"])
 
    def print_board_move(self):
            print("a1.........................d1..........................g1")
            print("",".","                         .","                          .")
            print("",".","                         .","                          .")
            print("",".        b2...............d2.................f2        .")
            print("",".","        .                .","                .         .")
            print("",".","        .                .","                .         .")
            print("",".","        .                .","                .         .")
            print("",".","        .        c3......d3......e3        .         .")
            print("",".","        .        .         ","      .        .         .")
            print("",".","        .        .         ","      .        .         .")
            print("a4........b4.......c4                e4.......f4........g4")
            print("",".","        .        .         ","      .        .         .")
            print("",".","        .        .         ","      .        .         .")
            print("",".","        .        c5......d5......e5        .         .")
            print("",".","        .                .","                .         .")
            print("",".","        .                .","                .         .")
            print("",".","        .                .","                .         .")
            print("",".        b6...............d6.................f6        .")
            print("",".","                         .","                          .")
            print("",".","                         .","                          .")
            print ("a7.........................d7...........................g7")

    def mill_state(self,pos,player):    
        self.values_for_mill[pos] = player

    def remove_stone(self,pos):
        self.values[pos] = "0 "
        self.values_for_mill[pos] = 0
        self.print_board()
        print("\n")

