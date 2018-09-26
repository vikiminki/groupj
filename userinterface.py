'''
Created on 14 sep. 2018

@author: Sina
'''

class userinterface:
    occupied = []
    player1 = []
    player2 = []
    values={"a1":"0 ", "d1":"0 ", "g1":"0 ", "e1":"0 ", "b2":"0 ", "d2":"0 ", "f2":"0 ", 
            "c3":"0 ", "d3":"0 ", "e3":"0 ", "a4":"0 ", "b4":"0 ", "c4":"0 ", "e4":"0 ",
            "f4":"0 ", "g4":"0 ", "c5":"0 ", "d5":"0 ",
            "e5":"0 ", "b6":"0 ","d6":"0 ", "f6":"0 ", "a7":"0 ", "d7":"0 ", "g7":"0 "}
    #values={"a1":"a1", "d1":"d1", "g1":"g1", "e1":"e1", "b2":"b2", "d2":"d2", "f2":"f2", 
    #        "c3":"c3", "d3":"d3", "e3":"e3", "a4":"a4", "b4":"b4", "c4":"c4", "e4":"e4",
    #        "f4":"f4", "g4":"g4", "c5":"c5", "d5":"d5",
    #        "e5":"e5", "b6":"b6","d6":"d6", "f6":"f6", "a7":"a7", "d7":"d7", "g7":"g7"}





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
    
    def make_move(self, pos, player):
        self.values[pos] = player
        self.print_board()
        print("\n")

    def legal_move(self, position):
        #should also work for moving stones
        legal_position = False
        if(self.values[position] == "0 "):
            legal_position = True
        return(legal_position)

           


