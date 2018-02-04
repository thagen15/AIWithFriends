import os.path
from board import Board
from space import Space
import time
if __name__ == '__main__':
    board = Board()
    #White is 1, Black is 2
    color = 1
    opponent = 0

    teamName = 'AI_With_Friends'

    #While the end of game file isn't there
    while not os.path.isfile('end_game'): #main python file to run our code from

        while not os.path.isfile(teamName+'.go'):
            go = 9
        #is our prompt file in the path
        #ensure we are not writing and checking to fast
        time.sleep(.1)
        if os.path.isfile(teamName+'.go'): #main python file to run our code from
            #read the move.txt file and update the board
            file = open("move_file", "r")
            move = str(file.read()).split()
            file.close()
            #if the file is empty, this is the first move of the game so we are the white stones
            if move == []:
                color = 0
                opponent = 1

                board.placeStone(color,7,7)
                file = open("move_file", "w")
                file.write(teamName+' h 8')
                file.close()

            #Otherwise, a move has been made. Process the latest move and update our board
            else:
                #move is split by spaces into 3 things, groupName Column Row
                print(opponent)
                print(move[1])
                #print ord(move[1])-96

                print(move[2])
                board.placeStone(opponent, ord(move[1])-96, move[2])

                board.nextTurn()
                #Process the board and do magic things to do best move
                optimalMove = board.minimax().getPosition()
                print (optimalMove)
                board.placeStone(color, optimalMove[0],optimalMove[1])
                letter = chr(optimalMove[0]+64)
                #lastly write to the file
                file = open("move_file", "w")
                file.write(teamName+' '+letter+' '+str(optimalMove[1]))
                file.close()