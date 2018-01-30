class Board(object):
    """docstring for board."""
    def __init__(self):
        super(board, self).__init__()


        for y in range(1,16):
            for x in range(1,16):
                self.spaces.append(Space(x,y))

        self.isComplete = False
        self.turn = 0

    def getSpaces(self):
        return self.spaces
    def getIsComplete(self):
        return self.isComplete
    def whoseTurn(self):
        return self.turn
    def checkComplete(self):
        #If white stones has 5 in a row set isComplete to false
        if condition:

        #Else if black stones has 5 in a row set isComplete to false
        elif:

        #Else if the board is filled, the game is tied
        else:
            self.isComplete = False
        return self.isComplete

    def placeStone(player, xPos, yPos):
        index = xPos*yPos

        if not self.spaces[index].filled:
            self.spaces[index].fill(player)
        else:
            print ("Invalid move pace is occupied by: ", self.spaces[index].occupiedBy)


    def minimax():

        #get all potential next moves
        potentialPositions = getChildren(board)

        #variables to return the best move
        currentBest = potentialPositions[0]
        currentBestValue = float('-inf')

        #Go through all potential posistions with minimax
        for child in  potentialPositions:

            #create a copy of the boardstate with the position now filled
            copyBoard = board
            childPos = child.getPosition()

            for i in range(1,16):
                for j in range(1,16):
                    if copyBoard.getSpaces()[i][j].getPosition() == childPos
                        copyBoard.getSpaces()[i][j].fill(copyturn)
                        break

            #Get the max value of board state of the copied state
            tempMax = minMove(copyBoard)

            #if the found value is creater than current best value, it becomes new best value
            if(tempMax > currentBestValue):
                currentBestValue = tempMax
                currentBest = child

        #returns best move
        return currentBest



    def getChildren(board):
        #list of empty spaces
        children = []

        #finds all empty spaces and puts into children
        for i in range(1,16):
            for j in range(1,16):
                if(board.getSpaces()[i][j].getIsFilled() == false):
                    children.append(board.getSpaces()[i][j])

        return children



    def minMove(board):

        #check if game is done whether its a tie or someone wins
        board.checkComplete()
        #if game is complete, return the value of the gamestate
        #if opponent wins, the value will be small,
        #if player wins, value will be larger
        if board.getIsComplete() == true:
            return  eval(board)

        #get all potential next moves of board
        potentialPositions = getChildren(board)


        #variables to return the best move
        currentWorst = potentialPositions[0]
        currentWorstValue = float('inf')

        #Go through all potential posistions with minimax
        for child in  potentialPositions:

            #create a copy of the boardstate with the position now filled
            copyBoard = board
            childPos = child.getPosition()

            for i in range(1,16):
                for j in range(1,16):
                    if copyBoard.getSpaces()[i][j].getPosition() == childPos
                        copyBoard.getSpaces()[i][j].fill(copyturn)
                        break

            #Get the min value of board state of the copied state
            tempMin = MaxMove(copyBoard)

            #if the found value is creater than current best value, it becomes new best value
            if(tempMin < currentWorstValue):
                currentWorstValue = tempMin
                currentWorst = child

        #returns best move value
        return currentWorstValue



    def maxMove(board):

        #check if game is done whether its a tie or someone wins
        board.checkComplete()
        #if game is complete, return the value of the gamestate
        #if opponent wins, the value will be small,
        #if player wins, value will be larger
        if board.getIsComplete() == true:
            return  eval(board)

        #get all potential next moves of board
        potentialPositions = getChildren(board)


        #variables to return the best move
        currentBest = potentialPositions[0]
        currentBestValue = float('-inf')

        #Go through all potential posistions with minimax
        for child in  potentialPositions:

            #create a copy of the boardstate with the position now filled
            copyBoard = board
            childPos = child.getPosition()

            for i in range(1,16):
                for j in range(1,16):
                    if copyBoard.getSpaces()[i][j].getPosition() == childPos
                        copyBoard.getSpaces()[i][j].fill(copyBoard.whoseTurn())
                        break

            #Get the min value of board state of the copied state
            tempMax = MinMove(copyBoard)

            #if the found value is creater than current best value, it becomes new best value
            if(tempMax > currentBestValue):
                currentBestValue = tempMax
                currentBest = child

        #returns best move value
        return currentBestValue


    def eval(board):
        @# TODO: create an eval function

        value = None

        #find number of rows, columns, and diagonals with 5 black in a row and no white next to it
        num5Black = 0
        num4Black = 0
        num3Black = 0
        num2Black = 0
        num1black = 0

        #find number of rows, columns, and diagonals with 5 white in a row and not black  next to it
        num5White = 0
        num4White = 0
        num3White = 0
        num2White = 0
        num1White = 0

        checkHoriz(board)
        checkVert(board)
        checkDiag(board)

        if num5Black > 0 and board.whoseTurn() == 0:
            return float('inf')
        elif num5Black > 0 and board.whoseTurn() == 1:
            return float('-inf')
        elif num5White > 0 and board.whoseTurn() == 0:
            return float('-inf')
        elif num5White > 0 and board.whoseTurn() == 1:
            return float('inf')
        else:
            value = 123456789876543234567876543456 #eval function


        return value

    #check horizontal
    def checkHoriz(board):
        @# TODO:
        #define whose turn it is
        turn = board.whoseTurn()

        hcount2 = 0
        hcount3 = 0
        hcount4 = 0
        hcount5 = 0
        horizontalCount = 0

        #go through eat space and check which ones are viable
        for space in range(0,225):

            #look at spaces 0 right 4 left
            if (board.getSpaces()[space].getPosition()[0]-4)>0:
                left1=board.getSpaces()[space-1].getOccupiedBy()
                left2=board.getSpaces()[space-2].getOccupiedBy()
                left3=board.getSpaces()[space-3].getOccupiedBy()
                left4=board.getSpaces()[space-4].getOccupiedBy()

                tempCount =0
                #check to make sure all these spaces are either blank or the color of the player whose turn it is
                if ((left1 == turn or left1==2) and (left2 == turn or left2==2) and (left3 == turn or left3==2) and (left4 == turn or left4==2)):
                    #increase tempCount for the number of actual spaces filled with player's stone
                    if left1 ==turn:
                        tempCount+=1
                    if left2==turn:
                        tempCount+=1
                    if left3==turn:
                        tempCount+=1
                    if left4==turn:
                        tempCount+=1
                #Replace horisontalCount with tempcount if tempcount is larger
                if tempCount>horizontalCount:
                    horizontalCount = tempCount + 1

            #look at spaces 0 left 4 right
            if (15-board.getSpaces()[space].getPosition[0])>4:
                right1=board.getSpaces()[space+1].getOccupiedBy()
                right2=board.getSpaces()[space+2].getOccupiedBy()
                right3=board.getSpaces()[space+3].getOccupiedBy()
                right4=board.getSpaces()[space+4].getOccupiedBy()
                tempCount=0

                #check to make sure all these spaces are either blank or the color of the player whose turn it is
                if ((right1 == turn or right1==2) and (right2 == turn or left2==2) and (left3 == turn or left3==2) and (left4 == turn or left4==2)):
                    #increase tempCount for the number of actual spaces filled with player's stone
                    if right1 ==turn:
                        tempCount+=1
                    if right3==turn:
                        tempCount+=1
                    if right3==turn:
                        tempCount+=1
                    if right4==turn:
                        tempCount+=1
                #Replace horisontalCount with tempcount if tempcount is larger
                if tempCount>horizontalCount:
                    horizontalCount = tempCount + 1

            #look at spaces 3 left 1 right
            if (board.getSpaces()[space].getPosition()[0]-3)>0:
                left1=board.getSpaces()[space-1].getOccupiedBy()
                left2=board.getSpaces()[space-2].getOccupiedBy()
                left3=board.getSpaces()[space-3].getOccupiedBy()
                right1=board.getSpaces()[space+1].getOccupiedBy()

                tempCount =0
                #check to make sure all these spaces are either blank or the color of the player whose turn it is
                if ((left1 == turn or left1==2) and (left2 == turn or left2==2) and (left3 == turn or left3==2) and (right1 == turn or right1==2)):
                    #increase tempCount for the number of actual spaces filled with player's stone
                    if left1 ==turn:
                        tempCount+=1
                    if left2==turn:
                        tempCount+=1
                    if left3==turn:
                        tempCount+=1
                    if right1==turn:
                        tempCount+=1
                #Replace horisontalCount with tempcount if tempcount is larger
                if tempCount>horizontalCount:
                    horizontalCount = tempCount + 1


            #look at spaces 2 left 2 right
            if (board.getSpaces()[space].getPosition()[0]-2)>0:
                left1=board.getSpaces()[space-1].getOccupiedBy()
                left2=board.getSpaces()[space-2].getOccupiedBy()
                right1=board.getSpaces()[space+1].getOccupiedBy()
                right2=board.getSpaces()[space+2].getOccupiedBy()
                tempCount = 0
                #check to make sure all these spaces are either blank or the color of the player whose turn it is
                if ((left1 == turn or left1==2) and (left2 == turn or left2==2) and (right1 == turn or right1==2) and (right2 == turn or right2==2)):
                    #increase tempCount for the number of actual spaces filled with player's stone
                    if left1 ==turn:
                        tempCount+=1
                    if left2==turn:
                        tempCount+=1
                    if right1==turn:
                        tempCount+=1
                    if right2==turn:
                        tempCount+=1
                #Replace horisontalCount with tempcount if tempcount is larger
                if tempCount>horizontalCount:
                    horizontalCount = tempCount + 1


            #look at spaces 1 left 3 right
            if (board.getSpaces()[space].getPosition()[0]-1)>0:
                left1=board.getSpaces()[space-1].getOccupiedBy()
                right1=board.getSpaces()[space+1].getOccupiedBy()
                right2=board.getSpaces()[space+2].getOccupiedBy()
                right3=board.getSpaces()[space+3].getOccupiedBy()
                tempCount = 0

                #check to make sure all these spaces are either blank or the color of the player whose turn it is
                if ((left1 == turn or left1==2) and (right2 == turn or right2==2) and (right3 == turn or right3==2) and (right4 == turn or right4==2)):
                    #increase tempCount for the number of actual spaces filled with player's stone
                    if left1 ==turn:
                        tempCount+=1
                    if right1==turn:
                        tempCount+=1
                    if right2==turn:
                        tempCount+=1
                    if right3==turn:
                        tempCount+=1
                #Replace horisontalCount with tempcount if tempcount is larger
                if tempCount>horizontalCount:
                    horizontalCount = tempCount + 1

            #Increase specific count based on the best horizontalCount found
            if(horizontalCount == 2):
                hcount2++
            elif(horizontalCount == 3):
                hcount3++
            elif(horizontalCount == 4):
                hcount4++
            elif(horizontalCount == 5):
                hcount5++

        #returns the number of horizontal rows that have a chance of winning and have 2, 3, 4, or 5 columns
        return (hcount2, hcount3, hcount4, hcount5)
