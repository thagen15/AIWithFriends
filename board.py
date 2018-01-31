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
            if (15-board.getSpaces()[space].getPosition[0])>3:
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
            if (board.getSpaces()[space].getPosition()[0]-3)>0 and (15-board.getSpaces()[space].getPosition()[0])>0:
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
            if (board.getSpaces()[space].getPosition()[0]-2)>0 and (15-board.getSpaces()[space].getPosition()[0])>1:
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
            if (board.getSpaces()[space].getPosition()[0]-1)>0 and (15-board.getSpaces()[space].getPosition()[0])>2:
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

    #check vertical
    def checkVert(board):
        #define whose turn it is
        turn = board.whoseTurn()

        vcount2 = 0
        vcount3 = 0
        vcount4 = 0
        vcount5 = 0
        verticalCount = 0

        #go through eat space and check which ones are viable
        for space in range(0,225):

            #look at spaces 0 down 4 up
            if (board.getSpaces()[space].getPosition()[1]-4)>0:
                up1=board.getSpaces()[space-15].getOccupiedBy()
                up2=board.getSpaces()[space-30].getOccupiedBy()
                up3=board.getSpaces()[space-45].getOccupiedBy()
                up4=board.getSpaces()[space-60].getOccupiedBy()

                tempCount =0
                #check to make sure all these spaces are either blank or the color of the player whose turn it is
                if ((up1 == turn or up1==2) and (up2 == turn or up2==2) and (up3 == turn or up3==2) and (up4 == turn or up4==2)):
                    #increase tempCount for the number of actual spaces filled with player's stone
                    if up1 ==turn:
                        tempCount+=1
                    if up2==turn:
                        tempCount+=1
                    if up3==turn:
                        tempCount+=1
                    if up4==turn:
                        tempCount+=1
                #Replace verticalCount with tempcount if tempcount is larger
                if tempCount>verticalCount:
                    verticalCount = tempCount + 1

            #look at spaces 0 up 4 down
            if (15-board.getSpaces()[space].getPosition[1])>3:
                down1=board.getSpaces()[space+15].getOccupiedBy()
                down2=board.getSpaces()[space+30].getOccupiedBy()
                down3=board.getSpaces()[space+45].getOccupiedBy()
                down4=board.getSpaces()[space+60].getOccupiedBy()
                tempCount=0

                #check to make sure all these spaces are either blank or the color of the player whose turn it is
                if ((down1 == turn or down1==2) and (down2 == turn or down2==2) and (down3 == turn or down3==2) and (down4 == turn or down4==2)):
                    #increase tempCount for the number of actual spaces filled with player's stone
                    if down1 ==turn:
                        tempCount+=1
                    if down3==turn:
                        tempCount+=1
                    if down3==turn:
                        tempCount+=1
                    if down4==turn:
                        tempCount+=1
                #Replace verticalCount with tempcount if tempcount is larger
                if tempCount>verticalCount:
                    verticalCount = tempCount + 1

            #look at spaces 3 up 1 down
            if (board.getSpaces()[space].getPosition()[1]-3)>0 and (15-board.getSpaces()[space].getPosition[1])>0:
                up1=board.getSpaces()[space-15].getOccupiedBy()
                up2=board.getSpaces()[space-30].getOccupiedBy()
                up3=board.getSpaces()[space-45].getOccupiedBy()
                down1=board.getSpaces()[space+15].getOccupiedBy()

                tempCount =0
                #check to make sure all these spaces are either blank or the color of the player whose turn it is
                if ((up1 == turn or up1==2) and (up2 == turn or up2==2) and (up3 == turn or up3==2) and (down1 == turn or down1==2)):
                    #increase tempCount for the number of actual spaces filled with player's stone
                    if up1 ==turn:
                        tempCount+=1
                    if up2==turn:
                        tempCount+=1
                    if up3==turn:
                        tempCount+=1
                    if up1==turn:
                        tempCount+=1
                #Replace verticalCount with tempcount if tempcount is larger
                if tempCount>verticalCount:
                    verticalCount = tempCount + 1


            #look at spaces 2 up 2 down
            if (board.getSpaces()[space].getPosition()[1]-2)>0 and (15-board.getSpaces()[space].getPosition[1])>1:
                up1=board.getSpaces()[space-15].getOccupiedBy()
                up2=board.getSpaces()[space-30].getOccupiedBy()
                down1=board.getSpaces()[space+15].getOccupiedBy()
                down2=board.getSpaces()[space+30].getOccupiedBy()
                tempCount = 0
                #check to make sure all these spaces are either blank or the color of the player whose turn it is
                if ((up1 == turn or up1==2) and (up2 == turn or up2==2) and (down1 == turn or down1==2) and (down2 == turn or down2==2)):
                    #increase tempCount for the number of actual spaces filled with player's stone
                    if up1 ==turn:
                        tempCount+=1
                    if up2==turn:
                        tempCount+=1
                    if down1==turn:
                        tempCount+=1
                    if down2==turn:
                        tempCount+=1
                #Replace verticalCount with tempcount if tempcount is larger
                if tempCount>verticalCount:
                    verticalCount = tempCount + 1


            #look at spaces 1 up 3 down
            if (board.getSpaces()[space].getPosition()[1]-1)>0 and (15-board.getSpaces()[space].getPosition[1])>2:
                up1=board.getSpaces()[space-15].getOccupiedBy()
                down1=board.getSpaces()[space+15].getOccupiedBy()
                down2=board.getSpaces()[space+30].getOccupiedBy()
                down3=board.getSpaces()[space+45].getOccupiedBy()
                tempCount = 0

                #check to make sure all these spaces are either blank or the color of the player whose turn it is
                if ((up1 == turn or up1==2) and (down2 == turn or down2==2) and (down3 == turn or down3==2) and (down4 == turn or down4==2)):
                    #increase tempCount for the number of actual spaces filled with player's stone
                    if up1 ==turn:
                        tempCount+=1
                    if down1==turn:
                        tempCount+=1
                    if down2==turn:
                        tempCount+=1
                    if down3==turn:
                        tempCount+=1
                #Replace verticalCount with tempcount if tempcount is larger
                if tempCount>verticalCount:
                    verticalCount = tempCount + 1

            #Increase specific count based on the best verticalCount found
            if(verticalCount == 2):
                vcount2++
            elif(verticalCount == 3):
                vcount3++
            elif(verticalCount == 4):
                vcount4++
            elif(verticalCount == 5):
                vcount5++

        #returns the number of vertical rows that have a chance of winning and have 2, 3, 4, or 5 columns
        return (vcount2, vcount3, vcount4, vcount5)

    #check \ vertical
    def checkDiag1(board):
        #define whose turn it is
        turn = board.whoseTurn()

        dcount2 = 0
        dcount3 = 0
        dcount4 = 0
        dcount5 = 0
        diagonalCount = 0

        #go through eat space and check which ones are viable
        for space in range(0,225):

            #look at spaces 0 rightDown 4 leftUp
            if (board.getSpaces()[space].getPosition()[1]-4)>0:         @#TODO fix boarder cases
                leftUp1=board.getSpaces()[space-16].getOccupiedBy()
                leftUp2=board.getSpaces()[space-32].getOccupiedBy()
                leftUp3=board.getSpaces()[space-48].getOccupiedBy()
                leftUp4=board.getSpaces()[space-64].getOccupiedBy()

                tempCount =0
                #check to make sure all these spaces are either blank or the color of the player whose turn it is
                if ((leftUp1 == turn or leftUp1==2) and (leftUp2 == turn or leftUp2==2) and (leftUp3 == turn or leftUp3==2) and (leftUp4 == turn or leftUp4==2)):
                    #increase tempCount for the number of actual spaces filled with player's stone
                    if leftUp1 ==turn:
                        tempCount+=1
                    if leftUp2==turn:
                        tempCount+=1
                    if leftUp3==turn:
                        tempCount+=1
                    if leftUp4==turn:
                        tempCount+=1
                #Replace diagonalCount with tempcount if tempcount is larger
                if tempCount>diagonalCount:
                    diagonalCount = tempCount + 1

            #look at spaces 0 leftUp 4 rightDown
            if (15-board.getSpaces()[space].getPosition[1])>4:
                rightDown1=board.getSpaces()[space+16].getOccupiedBy()
                rightDown2=board.getSpaces()[space+32].getOccupiedBy()
                rightDown3=board.getSpaces()[space+48].getOccupiedBy()
                rightDown4=board.getSpaces()[space+64].getOccupiedBy()
                tempCount=0

                #check to make sure all these spaces are either blank or the color of the player whose turn it is
                if ((rightDown1 == turn or rightDown1==2) and (rightDown2 == turn or rightDown2==2) and (rightDown3 == turn or rightDown3==2) and (rightDown4 == turn or rightDown4==2)):
                    #increase tempCount for the number of actual spaces filled with player's stone
                    if rightDown1 ==turn:
                        tempCount+=1
                    if rightDown3==turn:
                        tempCount+=1
                    if rightDown3==turn:
                        tempCount+=1
                    if rightDown4==turn:
                        tempCount+=1
                #Replace diagonalCount with tempcount if tempcount is larger
                if tempCount>diagonalCount:
                    diagonalCount = tempCount + 1

            #look at spaces 3 leftUp 1 rightDown
            if (board.getSpaces()[space].getPosition()[1]-3)>0:
                leftUp1=board.getSpaces()[space-16].getOccupiedBy()
                leftUp2=board.getSpaces()[space-32].getOccupiedBy()
                leftUp3=board.getSpaces()[space-48].getOccupiedBy()
                rightDown1=board.getSpaces()[space+16].getOccupiedBy()

                tempCount =0
                #check to make sure all these spaces are either blank or the color of the player whose turn it is
                if ((leftUp1 == turn or leftUp1==2) and (leftUp2 == turn or leftUp2==2) and (leftUp3 == turn or leftUp3==2) and (rightDown1 == turn or rightDown1==2)):
                    #increase tempCount for the number of actual spaces filled with player's stone
                    if leftUp1 ==turn:
                        tempCount+=1
                    if leftUp2==turn:
                        tempCount+=1
                    if leftUp3==turn:
                        tempCount+=1
                    if rightDown1==turn:
                        tempCount+=1
                #Replace diagonalCount with tempcount if tempcount is larger
                if tempCount>diagonalCount:
                    diagonalCount = tempCount + 1


            #look at spaces 2 leftUp 2 rightDown
            if (board.getSpaces()[space].getPosition()[1]-2)>0:
                leftUp1=board.getSpaces()[space-16].getOccupiedBy()
                leftUp2=board.getSpaces()[space-32].getOccupiedBy()
                rightDown1=board.getSpaces()[space+16].getOccupiedBy()
                rightDown2=board.getSpaces()[space+32].getOccupiedBy()
                tempCount = 0
                #check to make sure all these spaces are either blank or the color of the player whose turn it is
                if ((leftUp1 == turn or leftUp1==2) and (leftUp2 == turn or leftUp2==2) and (rightDown1 == turn or rightDown1==2) and (rightDown2 == turn or rightDown2==2)):
                    #increase tempCount for the number of actual spaces filled with player's stone
                    if leftUp1 ==turn:
                        tempCount+=1
                    if leftUp2==turn:
                        tempCount+=1
                    if rightDown1==turn:
                        tempCount+=1
                    if rightDown2==turn:
                        tempCount+=1
                #Replace diagonalCount with tempcount if tempcount is larger
                if tempCount>diagonalCount:
                    diagonalCount = tempCount + 1


            #look at spaces 1 leftUp 3 rightDown
            if (board.getSpaces()[space].getPosition()[1]-1)>0:
                leftUp1=board.getSpaces()[space-16].getOccupiedBy()
                rightDown1=board.getSpaces()[space+16].getOccupiedBy()
                rightDown2=board.getSpaces()[space+32].getOccupiedBy()
                rightDown3=board.getSpaces()[space+48].getOccupiedBy()
                tempCount = 0

                #check to make sure all these spaces are either blank or the color of the player whose turn it is
                if ((leftUp1 == turn or leftUp1==2) and (rightDown2 == turn or rightDown2==2) and (rightDown3 == turn or rightDown3==2) and (rightDown4 == turn or rightDown4==2)):
                    #increase tempCount for the number of actual spaces filled with player's stone
                    if leftUp1 ==turn:
                        tempCount+=1
                    if rightDown1==turn:
                        tempCount+=1
                    if rightDown2==turn:
                        tempCount+=1
                    if rightDown3==turn:
                        tempCount+=1
                #Replace diagonalCount with tempcount if tempcount is larger
                if tempCount>diagonalCount:
                    diagonalCount = tempCount + 1

            #Increase specific count based on the best diagonalCount found
            if(diagonalCount == 2):
                dcount2++
            elif(diagonalCount == 3):
                dcount3++
            elif(diagonalCount == 4):
                dcount4++
            elif(diagonalCount == 5):
                dcount5++

        #returns the number of vertical rows that have a chance of winning and have 2, 3, 4, or 5 columns
        return (dcount2, dcount3, dcount4, dcount5)

    #check / diagonal
    def checkDiag2(board):