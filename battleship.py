######################################################
# Name: Elijah Jordan                                #
#                                                    #
# Assignment: Make a  game of tic tac toe            #
#                                                    #
# Bonus: None right now                              #
# Log: Sep 29/26                                     #              
# Bugs: needs documentation and sometime check       #
# winner dosent work                                 #
# Sources:Some google for single lines               #
######################################################

def main(): #main which controlls everything else
       board1 = [["10", "11", "12", "13", "14"],
                ["15", "16", "17", "18", "19"],
                ["20", "21", "22", "23", "24"],
                ["25", "26", "27", "28", "29"],
                ["30", "31", "32", "33", "34"]]
       defense1 = [["10", "11", "12", "13", "14"],
                       ["15", "16", "17", "18", "19"],
                       ["20", "21", "22", "23", "24"],
                       ["25", "26", "27", "28", "29"],
                       ["30", "31", "32", "33", "34"]]
       board2 = [["10", "11", "12", "13", "14"],
                       ["15", "16", "17", "18", "19"],
                       ["20", "21", "22", "23", "24"],
                       ["25", "26", "27", "28", "29"],
                       ["30", "31", "32", "33", "34"]]
       defense2 = [["10", "11", "12", "13", "14"],
                              ["15", "16", "17", "18", "19"],
                              ["20", "21", "22", "23", "24"],
                              ["25", "26", "27", "28", "29"],
                              ["30", "31", "32", "33", "34"]]
       display_board1(board1)
       placeboat(board1,defense1)
       display_board(defense1)
       display_board2(board2)
       placeattack(board2,board1)
       


def placeboat(board1,defense1): #the player for the x turn
       h = 5
       while h >= 0:
              inputp_1 = input("place a ship")
              for row in range(5):
                     for column in range(5):
                            if board1[row][column] == inputp_1:
                                   board1[row][column] = "🚢"
                                   defense1[row][column] = "1"
                                   display_board1(board1)
                                   h -= 1
                            

def placeattack(board2,board1): #the player for the x turn
       h = 5
       while h >= 0:
              inputp_1 = input("place your attack")
              for row in range(5):
                     for column in range(5):
                            if board2[row][column] == inputp_1:
                                   board2[row][column] = "❌"
                                   if board1[row][column] == "🚢":
                                          board2[row][column] = "❎"      
                                   display_board2(board2)
                                   h -= 1
                           
                                   
def display_board1(board1): #displays board
       for row in range(5): #checks row
              print(" " +  " | ".join(board1[row]))
              if row < 4:
                     print("----+----+----+----+----")

def display_board(defense1): #displays board
       for row in range(5): #checks row
              print(" " +  " | ".join(defense1[row]))
              if row < 4:
                     print("----+----+----+----+----")

def display_board2(board2): #displays board
       for row in range(5): #checks row
              print(" " +  " | ".join(board2[row]))
              if row < 4:
                     print("----+----+----+----+----")

main()