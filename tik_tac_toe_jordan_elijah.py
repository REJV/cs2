"""
Board [[1,2,3,
       [4,5,6],
       [7, 8, 9}










MAKING TIKTAKTOE

FIRST FUNCTION TO MAKE
PRINT BOARD


SECOND FUNCTION
have to choose between x and o

THIRD

have to choose a slot

Fourth 

if no x or o, therefor you can place there

FITTH FUNCTION
CHECK IF WINNER YET

IF board [0,2] == x''
	board [1,1] == x''
	board [2,0] == x''

return true

else 
return false


if true

Ask would you like to play again
if yes
reset count




	
"""
def main():
       counter = 1
       board = [["1", "2", "3",],
              ["4", "5", "6"],
              ["7", "8", "9"]]
       game_loop(board)
def display_board(board):
       for row in range(3):
              for column in range(3):
                     print (board[row][column], end=" ")
              print("")

def checkdraw(display_board)

def playx(board):
       inputp_1 = input("X TURN | where would you like to play (choose your number)")
       for row in range(3):
              for column in range(3):
                     if board[row][column] == inputp_1:
                            board[row][column] = "x"

       return(board)   
def playo(board):
       inputp_2 = input("O TURN | where would you like to play (choose your number)")
       for row in range(3):
              for column in range(3):
                     if board[row][column] == inputp_2:
                            board[row][column] = "o"

       return(board)   
def game_loop(board):  
       counter = 0
       while counter <= 9:
              display_board(board)
              playx(board)
              counter = counter +1
              display_board(board)
              playo(board)
              counter = counter +1
       
main()