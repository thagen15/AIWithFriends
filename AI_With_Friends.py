import os.path
from board import Board
from space import Space
import time
if __name__ == '__main__':
    board = Board()
    #White is 1, Black is 2
    color = 0
    opponent = 1

    teamName = 'AI_With_Friends'

    #While the end of game file isn't there
    while not os.path.isfile('end_game') : #main python file to run our code from
        while os.path.isfile(teamName+'.go'):
            #is our prompt file in the path
            #ensure we are not writing and checking to fast
            time.sleep(.5)
            if os.path.isfile(teamName+'.go'): #main python file to run our code from
                #read the move.txt file and update the board
                file = open("move_file", "r")
                move = str(file.read()).split()
                file.close()

                #if the file is empty, this is the first move of the game so we are the white stones
                if move == []:
                    color = 0
                    opponent = 1

                    board.placeStone(color,8,8)


                    file = open("move_file", "w")
                    file.write(teamName+' h 8')
                    file.close()


                #Otherwise, a move has been made. Process the latest move and update our board

                else:
                    board.nextTurn()
                    print(opponent)
                    print(move[1])
                    #print ord(move[1])-96

                    print(move[2])
                    board.placeStone(opponent, ord(move[1])-96, move[2])

                    #Check if it is the first turn to see if we want to steal the first move
                    if board.isFirstTurn:
                        board.nextTurn()
                        print('here')
                        print (ord(move[1])-96)
                        print(move[2])

                        #If it is in between F6 and J10 steal the space
                        if (6 <= (ord(move[1])-96) and (ord(move[1])-96)  <= 10) and (6 <= int(move[2]) and int(move[2])<= 10):
                            board.placeStone(color, ord(move[1])-96, move[2])
                            file = open("move_file", "w")
                            file.write(teamName+' '+move[1]+' '+str(move[2]))
                            file.close()

                        else:
                            optimalMove = board.minimax().getPosition()
                            print (optimalMove)
                            board.placeStone(color, optimalMove[0],optimalMove[1])
                            letter = chr(optimalMove[0]+64)
                            #lastly write to the file
                            file = open("move_file", "w")
                            file.write(teamName+' '+letter+' '+str(optimalMove[1]))
                            file.close()

                    #move is split by spaces into 3 things, groupName Column Row

                    else:
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
