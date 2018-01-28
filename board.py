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
                        copyBoard.getSpaces()[i][j].fill(copyBoard.whoseTurn())
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
                        copyBoard.getSpaces()[i][j].fill(copyBoard.whoseTurn())
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

        #find number of rows, columns, and diagonals with 5 black in a row
        num5Black = 0
        num4Black = 0
        num3Black = 0
        num2Black = 0
        num1black = 0

        #find number of rows, columns, and diagonals with 5 white in a row
        num5White = 0
        num4White = 0
        num3White = 0
        num2White = 0
        num1White = 0


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