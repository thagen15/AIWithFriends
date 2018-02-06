import os.path
from board import Board
from space import Space
if __name__ == '__main__':
    board = Board()
    #White is 1, Black is 2
    color = 1
    opponent = 0

    teamName = 'AI_With_Friends'

    #While the end of game file isn't there
    while not os.path.isfile('endgame.txt'): #main python file to run our code from


        #is our prompt file in the path
        #ensure we are not writing and checking to fast
        time.sleep(.1)
        if os.path.isfile(teamName+'.go'): #main python file to run our code from
            #read the move.txt file and update the board
            file = open("move_file.txt", "r")
            move = str(file.read()).split()
            file.close()
            #if the file is empty, this is the first move of the game so we are the white stones
            if move == []:
                color = 0
                opponent = 1

            #Otherwise, a move has been made. Process the latest move and update our board
            else:
                #move is split by spaces into 3 things, groupName Column Row
                print(opponent)
                print(move[1])
                print(move[2])
                board.placeStone(opponent, move[1], move[2])

                board.nextTurn()
                #Process the board and do magic things to do best move
                optimalMove = board.minimax().getPosition()
                print (optimalMove)
                board.placeStone(color, optimalMove[0],optimalMove[1])
                #lastly write to the file
                file = open("move_file.txt", "w")
                file.write(teamName+' '+str(optimalMove[0])+' '+str(optimalMove[1]))
                file.close()
