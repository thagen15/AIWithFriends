from space import Space
import copy
import time

class Board():
    """docstring for board."""
    def __init__(self):
        self.spaces = []

        for y in range(1,16):
            for x in range(1,16):
                self.spaces.append(Space(x,y))

        print(len(self.getSpaces()))

        self.isFirstTurn = True
        self.isComplete = False
        self.turn = 0

    def getSpaces(self):
        return self.spaces
    def getIsComplete(self):
        return self.isComplete
    def whoseTurn(self):
        return self.turn
    def nextTurn(self):
        self.turn = abs(self.whoseTurn()-1)

    # def checkComplete(self):
    #     #If white stones has 5 in a row set isComplete to false
    #     if condition:
    #
    #     #Else if black stones has 5 in a row set isComplete to false
    #     elif:
    #
    #     #Else if the board is filled, the game is tied
    #     else:
    #         self.isComplete = False
    #     return self.isComplete

    def placeStone(self, player, xPos, yPos):
        if self.isFirstTurn and player ==0:
            self.isFirstTurn = False
        index = (int(yPos)-1)*15 + (int(xPos)-1)
        # if not self.spaces[index].isFilled:
        self.spaces[index].fill(player)
        # else:
        #     print ('Invalid move space is occupied by: ', self.spaces[index].occupiedBy)



    def getChildren(self):
        #list of empty spaces
        children = []
        #finds all empty spaces and puts into children
        # for i in range(1,16):
        #     for j in range(1,16):
        #
        #print(self.whoseTurn())
        children = self.getChains()
        # counter = 0
        # if children:
        #     for chainSpace in children:
        #         print("chains ", counter, " x: ", chainSpace.getPosition()[0], " y: ", chainSpace.getPosition()[1])
        #         counter +=1

        if not children:
            for tile in self.getSpaces():
                # if(self.getSpaces()[i*j].getIsFilled() == False):
                #print i*j

                upLeft = -1
                up = -1
                upRight = -1
                left = -1
                right = -1
                downLeft = -1
                down = -1
                downRight = -1
                check = False


                if children:
                    for chainSpace in children:
                        if(chainSpace.getPosition() == tile.getPosition()):
                            check = True

                if(check != True):
                    if not tile.getIsFilled():

                        currentPosX = tile.getPosition()[0]
                        currentPosY = tile.getPosition()[1]
                        currentPos = ((tile.getPosition()[1]-1)*15) + (tile.getPosition()[0]-1)
                        if(currentPosX -1 > 0 and currentPosY -1 > 0):
                            upLeft = currentPos -16
                        if(currentPosY -1 > 0):
                            up = currentPos - 15
                        if(15-currentPosX > 0 and currentPosY -1 > 0):
                            upRight = currentPos - 14
                        if(currentPosX -1 > 0):
                            left = currentPos -1
                        if(15-currentPosX > 0):
                            right = currentPos + 1
                        if(currentPosX -1 > 0 and 15 - currentPosY > 0):
                            downLeft = currentPos + 14
                        if(15 - currentPosY > 0):
                            down = currentPos + 15
                        if(15-currentPosX > 0 and 15 - currentPosY > 0):
                            downRight = currentPos + 16


                        if(upLeft != -1):
                            if(self.getSpaces()[upLeft].getOccupiedBy() != 2):
                                children.append(tile)
                        if(up != -1):
                            if (self.getSpaces()[up].getOccupiedBy() != 2):
                                children.append(tile)
                        if (upRight != -1):
                            if (self.getSpaces()[upRight].getOccupiedBy() != 2):
                                children.append(tile)
                        if (left != -1):
                            if (self.getSpaces()[left].getOccupiedBy() != 2):
                                children.append(tile)
                        if (right != -1):
                            if (self.getSpaces()[right].getOccupiedBy() != 2):
                                children.append(tile)
                        if (downLeft != -1):
                            if (self.getSpaces()[downLeft].getOccupiedBy() != 2):
                                children.append(tile)
                        if (down != -1):
                            if (self.getSpaces()[down].getOccupiedBy() != 2):
                                children.append(tile)
                        if (downRight != -1):
                            if (self.getSpaces()[downRight].getOccupiedBy() != 2):
                                children.append(tile)
        # print children
        return children

    def minimax(self):
        global startTime
        startTime = time.time()
        #get all potential next moves
        potentialPositions = self.getChildren()

        counter = 0
        for potential in potentialPositions:
            print(counter, " x: ", potential.getPosition()[0], " y: ", potential.getPosition()[1])
            counter += 1

        #variables to return the best move
        currentBest = potentialPositions[0]
        currentBestValue = float('-inf')

        #Go through all potential posistions with minimax
        for child in  potentialPositions:

            #create a copy of the selfstate with the position now filled
            copyself = copy.deepcopy(self)
            childPos = child.getPosition()


            for copySpace in copyself.getSpaces():
                if copySpace.getPosition() == childPos:
                    copySpace.fill(copyself.whoseTurn())
                    break

            copyself.nextTurn()
            #Get the max value of self state of the copied state
            tempMax = copyself.minMove(0, currentBestValue)
            # global startTime
            if time.time() - startTime > 8:
                break
            print(tempMax)
            #if the found value is creater than current best value, it becomes new best value
            if(tempMax > currentBestValue):
                currentBestValue = tempMax
                currentBest = child
            print("x = ", currentBest.getPosition()[0], " y = ", currentBest.getPosition()[1])

        #returns best move
        return currentBest




    def minMove(self, branch, alpha):
        #print "here1"
        #check if game is done whether its a tie or someone wins
        # self.checkComplete()
        #if game is complete, return the value of the gamestate
        #if opponent wins, the value will be small,
        #if player wins, value will be larger
        # if self.getIsComplete() == true:
        #     return  evaluation(self)
        global startTime
        if time.time()-startTime>8:
            return float('-inf')

        if branch == 2:
            #print self.evaluation()
            return self.evaluation()

        #get all potential next moves of self
        potentialPositions = self.getChildren()


        #variables to return the best move
        currentWorst = potentialPositions[0]
        currentWorstValue = float('inf')

        #Go through all potential posistions with minimax
        for child in  potentialPositions:

            #create a copy of the selfstate with the position now filled
            copyself = copy.deepcopy(self)
            childPos = child.getPosition()

            for copySpace in copyself.getSpaces():
                if copySpace.getPosition() == childPos:
                    copySpace.fill(copyself.whoseTurn())
                    break

            #Get the min value of self state of the copied state

            copyself.nextTurn()
            tempMin = copyself.maxMove(branch+1, currentWorstValue)
            if(tempMin < alpha):
                currentWorstValue = alpha
                break
            if time.time() - startTime > 8:
                break
            #if the found value is creater than current best value, it becomes new best value
            if(tempMin < currentWorstValue):
                currentWorstValue = tempMin
                currentWorst = child

        #returns best move value
        return currentWorstValue



    def maxMove(self, branch, alpha):

        #check if game is done whether its a tie or someone wins
        # self.checkComplete()
        #if game is complete, return the value of the gamestate
        #if opponent wins, the value will be small,
        #if player wins, value will be larger
        # if self.getIsComplete()
            #create a copy of the selfstate with the position now filled == true:
        #     return  evaluation(self)

        global startTime
        if time.time() - startTime > 8:
            return float('inf')
        if branch == 2:
            return self.evaluation()

        #print "here2"
        #get all potential next moves of self
        potentialPositions = self.getChildren()


        #variables to return the best move

        currentBest = potentialPositions[0]
        currentBestValue = float('-inf')

        #Go through all potential posistions with minimax
        for child in  potentialPositions:

            #create a copy of the selfstate with the position now filled
            copyself = copy.deepcopy(self)
            childPos = child.getPosition()

            for copySpace in copyself.getSpaces():
                if copySpace.getPosition() == childPos:
                    copySpace.fill(copyself.whoseTurn())
                    break

            #Get the min value of self state of the copied state
            tempMax = copyself.minMove(branch+1, currentBestValue)
            if(tempMax > alpha):
                currentBestValue = alpha
                break
            # global startTime
            if time.time() - startTime > 8:
                break
            #if the found value is creater than current best value, it becomes new best value
            if(tempMax > currentBestValue):
                currentBestValue = tempMax
                currentBest = child

        #returns best move value
        return currentBestValue


    def evaluation(self):

        value = None

        #find number of rows, columns, and diagonals with 5 black in a row and no white next to it
        num5Black = 0
        num4Black = 0
        num3Black = 0
        num2Black = 0
        num1Black = 0

        #find number of rows, columns, and diagonals with 5 white in a row and not black  next to it
        num5White = 0
        num4White = 0
        num3White = 0
        num2White = 0
        num1White = 0

        b1, b2, b3, b4, b5 = self.checkHoriz(0)
        num1Black += b1
        num2Black += b2
        num3Black += b3
        num4Black += b4
        num5Black += b5
        b1, b2, b3, b4, b5 = self.checkVert(0)
        num1Black += b1
        num2Black += b2
        num3Black += b3
        num4Black += b4
        num5Black += b5
        b1, b2, b3, b4, b5 = self.checkDiag1(0)
        num1Black += b1
        num2Black += b2
        num3Black += b3
        num4Black += b4
        num5Black += b5
        b1,  b2, b3, b4, b5 = self.checkDiag2(0)
        num1Black += b1
        num2Black += b2
        num3Black += b3
        num4Black += b4
        num5Black += b5

        w1, w2, w3, w4, w5 = self.checkHoriz(1)
        num1White += w1
        num2White += w2
        num3White += w3
        num4White += w4
        num5White += w5
        w1, w2, w3, w4, w5 = self.checkVert(1)
        num1White += w1
        num2White += w2
        num3White += w3
        num4White += w4
        num5White += w5
        w1, w2, w3, w4, w5 = self.checkDiag1(1)
        num1White += w1
        num2White += w2
        num3White += w3
        num4White += w4
        num5White += w5
        w1, w2, w3, w4, w5 = self.checkDiag2(1)
        num1White += w1
        num2White += w2
        num3White += w3
        num4White += w4
        num5White += w5



        if num5Black > 0 and self.whoseTurn() == 0:
            return float('inf')
        elif num5Black > 0 and self.whoseTurn() == 1:
            return float('inf')
        elif num5White > 0 and self.whoseTurn() == 0:
            return float('inf')
        elif num5White > 0 and self.whoseTurn() == 1:
            return float('inf')
        else:
            value = (1000000000 * num4Black + 1000000 * num3Black + 1000 * num2Black + num1Black) - (1000000000 * num4White + 1000000 * num3White + 1000 * num2White + num1White) #evaluation function


        return value

    #check horizontal
    def checkHoriz(self, turn):

        hcount1 = 0
        hcount2 = 0
        hcount3 = 0
        hcount4 = 0
        hcount5 = 0
        horizontalCount = 0

        #go through eat space and check which ones are viable
        for space in range(0,225):
            if(self.getSpaces()[space].getOccupiedBy() == turn):

                #look at spaces 0 right 4 left
                if (self.getSpaces()[space].getPosition()[0]-4)>0:
                    left1=self.getSpaces()[space-1].getOccupiedBy()
                    left2=self.getSpaces()[space-2].getOccupiedBy()
                    left3=self.getSpaces()[space-3].getOccupiedBy()
                    left4=self.getSpaces()[space-4].getOccupiedBy()

                    tempCount =0
                    #check to make sure all these spaces are either blank or the color of the player whose turn it is
                    if ((left1 == turn or left1==2) and (left2 == turn or left2==2) and (left3 == turn or left3==2) and (left4 == turn or left4==2)):
                        #increase tempCount for the number of actual spaces filled with player's stone
                        tempCount += 1
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
                        horizontalCount = tempCount

                #look at spaces 0 left 4 right
                if (15-self.getSpaces()[space].getPosition()[0])>3:
                    right1=self.getSpaces()[space+1].getOccupiedBy()
                    right2=self.getSpaces()[space+2].getOccupiedBy()
                    right3=self.getSpaces()[space+3].getOccupiedBy()
                    right4=self.getSpaces()[space+4].getOccupiedBy()
                    tempCount=0

                    #check to make sure all these spaces are either blank or the color of the player whose turn it is
                    if ((right1 == turn or right1==2) and (right2 == turn or right2==2) and (right3 == turn or right3==2) and (right4 == turn or right4==2)):
                        #increase tempCount for the number of actual spaces filled with player's stone
                        tempCount += 1
                        if right1 ==turn:
                            tempCount+=1
                        if right2==turn:
                            tempCount+=1
                        if right3==turn:
                            tempCount+=1
                        if right4==turn:
                            tempCount+=1
                    #Replace horisontalCount with tempcount if tempcount is larger
                    if tempCount>horizontalCount:
                        horizontalCount = tempCount

                #look at spaces 3 left 1 right
                if (self.getSpaces()[space].getPosition()[0]-3)>0 and (15-self.getSpaces()[space].getPosition()[0])>0:
                    left1=self.getSpaces()[space-1].getOccupiedBy()
                    left2=self.getSpaces()[space-2].getOccupiedBy()
                    left3=self.getSpaces()[space-3].getOccupiedBy()
                    right1=self.getSpaces()[space+1].getOccupiedBy()

                    tempCount =0
                    #check to make sure all these spaces are either blank or the color of the player whose turn it is
                    if ((left1 == turn or left1==2) and (left2 == turn or left2==2) and (left3 == turn or left3==2) and (right1 == turn or right1==2)):
                        #increase tempCount for the number of actual spaces filled with player's stone
                        tempCount += 1
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
                        horizontalCount = tempCount


                #look at spaces 2 left 2 right
                if (self.getSpaces()[space].getPosition()[0]-2)>0 and (15-self.getSpaces()[space].getPosition()[0])>1:
                    left1=self.getSpaces()[space-1].getOccupiedBy()
                    left2=self.getSpaces()[space-2].getOccupiedBy()
                    right1=self.getSpaces()[space+1].getOccupiedBy()
                    right2=self.getSpaces()[space+2].getOccupiedBy()
                    tempCount = 0
                    #check to make sure all these spaces are either blank or the color of the player whose turn it is
                    if ((left1 == turn or left1==2) and (left2 == turn or left2==2) and (right1 == turn or right1==2) and (right2 == turn or right2==2)):
                        #increase tempCount for the number of actual spaces filled with player's stone
                        tempCount += 1
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
                        horizontalCount = tempCount


                #look at spaces 1 left 3 right
                if (self.getSpaces()[space].getPosition()[0]-1)>0 and (15-self.getSpaces()[space].getPosition()[0])>2:
                    left1=self.getSpaces()[space-1].getOccupiedBy()
                    right1=self.getSpaces()[space+1].getOccupiedBy()
                    right2=self.getSpaces()[space+2].getOccupiedBy()
                    right3=self.getSpaces()[space+3].getOccupiedBy()
                    tempCount = 0

                    #check to make sure all these spaces are either blank or the color of the player whose turn it is
                    if ((left1 == turn or left1==2) and (right1 == turn or right1==2) and (right2 == turn or right2==2) and (right3 == turn or right3==2)):
                        #increase tempCount for the number of actual spaces filled with player's stone
                        tempCount += 1
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
                        horizontalCount = tempCount

                #Increase specific count based on the best horizontalCount found
                if(horizontalCount == 1):
                    hcount1+=1
                elif(horizontalCount == 2):
                    hcount2+=1
                elif(horizontalCount == 3):
                    hcount3+=1
                elif(horizontalCount == 4):
                    hcount4+=1
                elif(horizontalCount == 5):
                    hcount5+=1

        #returns the number of horizontal rows that have a chance of winning and have 2, 3, 4, or 5 columns
        return (hcount1, hcount2, hcount3, hcount4, hcount5)

    #check vertical
    def checkVert(self, turn):

        vcount1 = 0
        vcount2 = 0
        vcount3 = 0
        vcount4 = 0
        vcount5 = 0
        verticalCount = 0

        #go through eat space and check which ones are viable
        for space in range(0,225):
            if (self.getSpaces()[space].getOccupiedBy() == turn):
                #look at spaces 0 down 4 up
                if (self.getSpaces()[space].getPosition()[1]-4)>0:
                    up1=self.getSpaces()[space-15].getOccupiedBy()
                    up2=self.getSpaces()[space-30].getOccupiedBy()
                    up3=self.getSpaces()[space-45].getOccupiedBy()
                    up4=self.getSpaces()[space-60].getOccupiedBy()

                    tempCount =0
                    #check to make sure all these spaces are either blank or the color of the player whose turn it is
                    if ((up1 == turn or up1==2) and (up2 == turn or up2==2) and (up3 == turn or up3==2) and (up4 == turn or up4==2)):
                        #increase tempCount for the number of actual spaces filled with player's stone
                        tempCount += 1
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
                        verticalCount = tempCount

                #look at spaces 0 up 4 down
                if (15-self.getSpaces()[space].getPosition()[1])>3:
                    down1=self.getSpaces()[space+15].getOccupiedBy()
                    down2=self.getSpaces()[space+30].getOccupiedBy()
                    down3=self.getSpaces()[space+45].getOccupiedBy()
                    down4=self.getSpaces()[space+60].getOccupiedBy()
                    tempCount=0

                    #check to make sure all these spaces are either blank or the color of the player whose turn it is
                    if ((down1 == turn or down1==2) and (down2 == turn or down2==2) and (down3 == turn or down3==2) and (down4 == turn or down4==2)):
                        #increase tempCount for the number of actual spaces filled with player's stone
                        tempCount += 1
                        if down1 ==turn:
                            tempCount+=1
                        if down2==turn:
                            tempCount+=1
                        if down3==turn:
                            tempCount+=1
                        if down4==turn:
                            tempCount+=1
                    #Replace verticalCount with tempcount if tempcount is larger
                    if tempCount>verticalCount:
                        verticalCount = tempCount

                #look at spaces 3 up 1 down
                if (self.getSpaces()[space].getPosition()[1]-3)>0 and (15-self.getSpaces()[space].getPosition()[1])>0:
                    up1=self.getSpaces()[space-15].getOccupiedBy()
                    up2=self.getSpaces()[space-30].getOccupiedBy()
                    up3=self.getSpaces()[space-45].getOccupiedBy()
                    down1=self.getSpaces()[space+15].getOccupiedBy()

                    tempCount =0
                    #check to make sure all these spaces are either blank or the color of the player whose turn it is
                    if ((up1 == turn or up1==2) and (up2 == turn or up2==2) and (up3 == turn or up3==2) and (down1 == turn or down1==2)):
                        #increase tempCount for the number of actual spaces filled with player's stone
                        tempCount += 1
                        if up1 ==turn:
                            tempCount+=1
                        if up2==turn:
                            tempCount+=1
                        if up3==turn:
                            tempCount+=1
                        if down1==turn:
                            tempCount+=1
                    #Replace verticalCount with tempcount if tempcount is larger
                    if tempCount>verticalCount:
                        verticalCount = tempCount


                #look at spaces 2 up 2 down
                if (self.getSpaces()[space].getPosition()[1]-2)>0 and (15-self.getSpaces()[space].getPosition()[1])>1:
                    up1=self.getSpaces()[space-15].getOccupiedBy()
                    up2=self.getSpaces()[space-30].getOccupiedBy()
                    down1=self.getSpaces()[space+15].getOccupiedBy()
                    down2=self.getSpaces()[space+30].getOccupiedBy()
                    tempCount = 0
                    #check to make sure all these spaces are either blank or the color of the player whose turn it is
                    if ((up1 == turn or up1==2) and (up2 == turn or up2==2) and (down1 == turn or down1==2) and (down2 == turn or down2==2)):
                        #increase tempCount for the number of actual spaces filled with player's stone
                        tempCount += 1
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
                        verticalCount = tempCount


                #look at spaces 1 up 3 down
                if (self.getSpaces()[space].getPosition()[1]-1)>0 and (15-self.getSpaces()[space].getPosition()[1])>2:
                    up1=self.getSpaces()[space-15].getOccupiedBy()
                    down1=self.getSpaces()[space+15].getOccupiedBy()
                    down2=self.getSpaces()[space+30].getOccupiedBy()
                    down3=self.getSpaces()[space+45].getOccupiedBy()
                    tempCount = 0

                    #check to make sure all these spaces are either blank or the color of the player whose turn it is
                    if ((up1 == turn or up1==2) and (down1 == turn or down1==2) and (down2 == turn or down2==2) and (down3 == turn or down3==2)):
                        #increase tempCount for the number of actual spaces filled with player's stone
                        tempCount += 1
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
                        verticalCount = tempCount

                #Increase specific count based on the best verticalCount found
                if(verticalCount == 1):
                    vcount1+=1
                elif(verticalCount == 2):
                    vcount2+=1
                elif(verticalCount == 3):
                    vcount3+=1
                elif(verticalCount == 4):
                    vcount4+=1
                elif(verticalCount == 5):
                    vcount5+=1

        #returns the number of vertical rows that have a chance of winning and have 2, 3, 4, or 5 columns
        return (vcount1, vcount2, vcount3, vcount4, vcount5)

    #check \ vertical
    def checkDiag1(self, turn):

        dcount1 = 0
        dcount2 = 0
        dcount3 = 0
        dcount4 = 0
        dcount5 = 0
        diagonalCount = 0

        #go through eat space and check which ones are viable
        for space in range(0,225):
            if (self.getSpaces()[space].getOccupiedBy() == turn):
                #look at spaces 0 rightDown 4 leftUp
                if (self.getSpaces()[space].getPosition()[0]-4)>0 and (self.getSpaces()[space].getPosition()[1]-4)>0:
                    leftUp1=self.getSpaces()[space-16].getOccupiedBy()
                    leftUp2=self.getSpaces()[space-32].getOccupiedBy()
                    leftUp3=self.getSpaces()[space-48].getOccupiedBy()
                    leftUp4=self.getSpaces()[space-64].getOccupiedBy()

                    tempCount =0
                    #check to make sure all these spaces are either blank or the color of the player whose turn it is
                    if ((leftUp1 == turn or leftUp1==2) and (leftUp2 == turn or leftUp2==2) and (leftUp3 == turn or leftUp3==2) and (leftUp4 == turn or leftUp4==2)):
                        #increase tempCount for the number of actual spaces filled with player's stone
                        tempCount += 1
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
                        diagonalCount = tempCount

                #look at spaces 0 leftUp 4 rightDown
                if (15-self.getSpaces()[space].getPosition()[0])>4 and (15-self.getSpaces()[space].getPosition()[1])>4:
                    rightDown1=self.getSpaces()[space+16].getOccupiedBy()
                    rightDown2=self.getSpaces()[space+32].getOccupiedBy()
                    rightDown3=self.getSpaces()[space+48].getOccupiedBy()
                    rightDown4=self.getSpaces()[space+64].getOccupiedBy()
                    tempCount=0

                    #check to make sure all these spaces are either blank or the color of the player whose turn it is
                    if ((rightDown1 == turn or rightDown1==2) and (rightDown2 == turn or rightDown2==2) and (rightDown3 == turn or rightDown3==2) and (rightDown4 == turn or rightDown4==2)):
                        #increase tempCount for the number of actual spaces filled with player's stone
                        tempCount += 1
                        if rightDown1 ==turn:
                            tempCount+=1
                        if rightDown2==turn:
                            tempCount+=1
                        if rightDown3==turn:
                            tempCount+=1
                        if rightDown4==turn:
                            tempCount+=1
                    #Replace diagonalCount with tempcount if tempcount is larger
                    if tempCount>diagonalCount:
                        diagonalCount = tempCount

                #look at spaces 3 leftUp 1 rightDown
                if (self.getSpaces()[space].getPosition()[0]-3)>0 and (self.getSpaces()[space].getPosition()[1]-3)>0 and (15-self.getSpaces()[space].getPosition()[0])>0 and (15-self.getSpaces()[space].getPosition()[1])>0:
                    leftUp1=self.getSpaces()[space-16].getOccupiedBy()
                    leftUp2=self.getSpaces()[space-32].getOccupiedBy()
                    leftUp3=self.getSpaces()[space-48].getOccupiedBy()
                    rightDown1=self.getSpaces()[space+16].getOccupiedBy()

                    tempCount =0
                    #check to make sure all these spaces are either blank or the color of the player whose turn it is
                    if ((leftUp1 == turn or leftUp1==2) and (leftUp2 == turn or leftUp2==2) and (leftUp3 == turn or leftUp3==2) and (rightDown1 == turn or rightDown1==2)):
                        #increase tempCount for the number of actual spaces filled with player's stone
                        tempCount += 1
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
                        diagonalCount = tempCount


                #look at spaces 2 leftUp 2 rightDown
                if (self.getSpaces()[space].getPosition()[0]-2)>0 and (self.getSpaces()[space].getPosition()[1]-2)>0 and (15-self.getSpaces()[space].getPosition()[0])>1 and (15-self.getSpaces()[space].getPosition()[1])>1:
                    leftUp1=self.getSpaces()[space-16].getOccupiedBy()
                    leftUp2=self.getSpaces()[space-32].getOccupiedBy()
                    rightDown1=self.getSpaces()[space+16].getOccupiedBy()
                    rightDown2=self.getSpaces()[space+32].getOccupiedBy()
                    tempCount = 0
                    #check to make sure all these spaces are either blank or the color of the player whose turn it is
                    if ((leftUp1 == turn or leftUp1==2) and (leftUp2 == turn or leftUp2==2) and (rightDown1 == turn or rightDown1==2) and (rightDown2 == turn or rightDown2==2)):
                        #increase tempCount for the number of actual spaces filled with player's stone
                        tempCount += 1
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
                        diagonalCount = tempCount


                #look at spaces 1 leftUp 3 rightDown
                if (self.getSpaces()[space].getPosition()[0]-1)>0 and (self.getSpaces()[space].getPosition()[1]-1)>0 and (15-self.getSpaces()[space].getPosition()[0])>2 and (15-self.getSpaces()[space].getPosition()[1])>2:
                    leftUp1=self.getSpaces()[space-16].getOccupiedBy()
                    rightDown1=self.getSpaces()[space+16].getOccupiedBy()
                    rightDown2=self.getSpaces()[space+32].getOccupiedBy()
                    rightDown3=self.getSpaces()[space+48].getOccupiedBy()
                    tempCount = 0

                    #check to make sure all these spaces are either blank or the color of the player whose turn it is
                    if ((leftUp1 == turn or leftUp1==2) and (rightDown1 == turn or rightDown1==2) and (rightDown2 == turn or rightDown2==2) and (rightDown3 == turn or rightDown3==2)):
                        #increase tempCount for the number of actual spaces filled with player's stone
                        tempCount += 1
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
                        diagonalCount = tempCount

                #Increase specific count based on the best diagonalCount found
                if(diagonalCount == 1):
                    dcount1+=1
                elif(diagonalCount == 2):
                    dcount2+=1
                elif(diagonalCount == 3):
                    dcount3+=1
                elif(diagonalCount == 4):
                    dcount4+=1
                elif(diagonalCount == 5):
                    dcount5+=1

        #returns the number of vertical rows that have a chance of winning and have 2, 3, 4, or 5 columns
        return (dcount1, dcount2, dcount3, dcount4, dcount5)

    #check / diagonal
    def checkDiag2(self, turn):

        dcount1 = 0
        dcount2 = 0
        dcount3 = 0
        dcount4 = 0
        dcount5 = 0
        diagonalCount = 0

        #go through eat space and check which ones are viable
        for space in range(0,225):
            if (self.getSpaces()[space].getOccupiedBy() == turn):
                #look at spaces 0 rightDown 4 rightUp
                if (self.getSpaces()[space].getPosition()[1]-4)>0 and (15-self.getSpaces()[space].getPosition()[0])>3:
                    rightUp1=self.getSpaces()[space-14].getOccupiedBy()
                    rightUp2=self.getSpaces()[space-28].getOccupiedBy()
                    rightUp3=self.getSpaces()[space-42].getOccupiedBy()
                    rightUp4=self.getSpaces()[space-56].getOccupiedBy()

                    tempCount =0
                    #check to make sure all these spaces are either blank or the color of the player whose turn it is
                    if ((rightUp1 == turn or rightUp1==2) and (rightUp2 == turn or rightUp2==2) and (rightUp3 == turn or rightUp3==2) and (rightUp4 == turn or rightUp4==2)):
                        #increase tempCount for the number of actual spaces filled with player's stone
                        tempCount += 1
                        if rightUp1 ==turn:
                            tempCount+=1
                        if rightUp2==turn:
                            tempCount+=1
                        if rightUp3==turn:
                            tempCount+=1
                        if rightUp4==turn:
                            tempCount+=1
                    #Replace diagonalCount with tempcount if tempcount is larger
                    if tempCount>diagonalCount:
                        diagonalCount = tempCount

                #look at spaces 0 rightUp 4 rightDown
                if (self.getSpaces()[space].getPosition()[0]-4)>0 and (15-self.getSpaces()[space].getPosition()[1])>3:
                    leftDown1=self.getSpaces()[space+14].getOccupiedBy()
                    leftDown2=self.getSpaces()[space+28].getOccupiedBy()
                    leftDown3=self.getSpaces()[space+42].getOccupiedBy()
                    leftDown4=self.getSpaces()[space+56].getOccupiedBy()
                    tempCount=0

                    #check to make sure all these spaces are either blank or the color of the player whose turn it is
                    if ((leftDown1 == turn or leftDown1==2) and (leftDown2 == turn or leftDown2==2) and (leftDown3 == turn or leftDown3==2) and (leftDown4 == turn or leftDown4==2)):
                        #increase tempCount for the number of actual spaces filled with player's stone
                        tempCount += 1
                        if leftDown1 ==turn:
                            tempCount+=1
                        if leftDown2==turn:
                            tempCount+=1
                        if leftDown3==turn:
                            tempCount+=1
                        if leftDown4==turn:
                            tempCount+=1
                    #Replace diagonalCount with tempcount if tempcount is larger
                    if tempCount>diagonalCount:
                        diagonalCount = tempCount

                #look at spaces 3 rightUp 1 rightDown
                if (self.getSpaces()[space].getPosition()[1]-3)>0 and (15-self.getSpaces()[space].getPosition()[0])>2 and (self.getSpaces()[space].getPosition()[0]-1)>0 and (15-self.getSpaces()[space].getPosition()[1])>0:
                    rightUp1=self.getSpaces()[space-14].getOccupiedBy()
                    rightUp2=self.getSpaces()[space-28].getOccupiedBy()
                    rightUp3=self.getSpaces()[space-42].getOccupiedBy()
                    leftDown1=self.getSpaces()[space+14].getOccupiedBy()

                    tempCount =0
                    #check to make sure all these spaces are either blank or the color of the player whose turn it is
                    if ((rightUp1 == turn or rightUp1==2) and (rightUp2 == turn or rightUp2==2) and (rightUp3 == turn or rightUp3==2) and (leftDown1 == turn or leftDown1==2)):
                        #increase tempCount for the number of actual spaces filled with player's stone
                        tempCount += 1
                        if rightUp1 ==turn:
                            tempCount+=1
                        if rightUp2==turn:
                            tempCount+=1
                        if rightUp3==turn:
                            tempCount+=1
                        if leftDown1==turn:
                            tempCount+=1
                    #Replace diagonalCount with tempcount if tempcount is larger
                    if tempCount>diagonalCount:
                        diagonalCount = tempCount


                #look at spaces 2 rightUp 2 rightDown
                if (self.getSpaces()[space].getPosition()[1]-2)>0 and (15-self.getSpaces()[space].getPosition()[0])>1 and (self.getSpaces()[space].getPosition()[0]-2)>0 and (15-self.getSpaces()[space].getPosition()[1])>1:
                    rightUp1=self.getSpaces()[space-14].getOccupiedBy()
                    rightUp2=self.getSpaces()[space-28].getOccupiedBy()
                    leftDown1=self.getSpaces()[space+14].getOccupiedBy()
                    leftDown2=self.getSpaces()[space+28].getOccupiedBy()
                    tempCount = 0
                    #check to make sure all these spaces are either blank or the color of the player whose turn it is
                    if ((rightUp1 == turn or rightUp1==2) and (rightUp2 == turn or rightUp2==2) and (leftDown1 == turn or leftDown1==2) and (leftDown2 == turn or leftDown2==2)):
                        #increase tempCount for the number of actual spaces filled with player's stone
                        tempCount += 1
                        if rightUp1 ==turn:
                            tempCount+=1
                        if rightUp2==turn:
                            tempCount+=1
                        if leftDown1==turn:
                            tempCount+=1
                        if leftDown2==turn:
                            tempCount+=1
                    #Replace diagonalCount with tempcount if tempcount is larger
                    if tempCount>diagonalCount:
                        diagonalCount = tempCount


                #look at spaces 1 rightUp 3 rightDown
                if (self.getSpaces()[space].getPosition()[1]-1)>0 and (15-self.getSpaces()[space].getPosition()[0])>0 and (self.getSpaces()[space].getPosition()[0]-3)>0 and (15-self.getSpaces()[space].getPosition()[1])>2:
                    rightUp1=self.getSpaces()[space-14].getOccupiedBy()
                    leftDown1=self.getSpaces()[space+14].getOccupiedBy()
                    leftDown2=self.getSpaces()[space+28].getOccupiedBy()
                    leftDown3=self.getSpaces()[space+42].getOccupiedBy()
                    tempCount = 0

                    #check to make sure all these spaces are either blank or the color of the player whose turn it is
                    if ((rightUp1 == turn or rightUp1==2) and (leftDown1 == turn or leftDown1==2) and (leftDown2 == turn or leftDown2==2) and (leftDown3 == turn or leftDown3==2)):
                        #increase tempCount for the number of actual spaces filled with player's stone
                        tempCount += 1
                        if rightUp1 ==turn:
                            tempCount+=1
                        if leftDown1==turn:
                            tempCount+=1
                        if leftDown2==turn:
                            tempCount+=1
                        if leftDown3==turn:
                            tempCount+=1
                    #Replace diagonalCount with tempcount if tempcount is larger
                    if tempCount>diagonalCount:
                        diagonalCount = tempCount

                #Increase specific count based on the best diagonalCount found
                if(diagonalCount == 1):
                    dcount1+=1
                elif(diagonalCount == 2):
                    dcount2+=1
                elif(diagonalCount == 3):
                    dcount3+=1
                elif(diagonalCount == 4):
                    dcount4+=1
                elif(diagonalCount == 5):
                    dcount5+=1

        #returns the number of vertical rows that have a chance of winning and have 2, 3, 4, or 5 columns
        return (dcount1, dcount2, dcount3, dcount4, dcount5)

    def getChains(self):

        turn = self.whoseTurn()
        opp = abs(turn-1)

        chainList = []
        tempList = []
        tempHoriz2 = []
        tempHoriz3 = []
        tempHoriz4 = []
        tempVert2 = []
        tempVert3 = []
        tempVert4 = []
        tempDiag11 = []
        tempDiag12 = []
        tempDiag13 = []
        tempDiag21 = []
        tempDiag22 = []
        tempDiag23 = []
        tempHoriz2w = []
        tempHoriz3w = []
        tempHoriz4w = []
        tempVert2w = []
        tempVert3w = []
        tempVert4w = []
        tempDiag11w = []
        tempDiag12w = []
        tempDiag13w = []
        tempDiag21w = []
        tempDiag22w = []
        tempDiag23w = []
        singles = []


        tempHoriz4 = self.chainHoriz4(turn)
        tempVert4 = self.chainVert4(turn)
        tempDiag14 = self.chainDiag14(turn)
        tempDiag24 = self.chainDiag24(turn)
        tempHoriz4w = self.chainHoriz4(opp)
        tempVert4w = self.chainVert4(opp)
        tempDiag14w = self.chainDiag14(opp)
        tempDiag24w = self.chainDiag24(opp)


        if tempHoriz4:
            for element in tempHoriz4:
                chainList.append(element)
        if tempVert4:
            for element in tempVert4:
                chainList.append(element)
        if tempDiag14:
            for element in tempDiag14:
                chainList.append(element)
        if tempDiag24:
            for element in tempDiag24:
                chainList.append(element)
        if tempHoriz4w:
            for element in tempHoriz4w:
                chainList.append(element)
        if tempVert4w:
            for element in tempVert4w:
                chainList.append(element)
        if tempDiag14w:
            for element in tempDiag14w:
                chainList.append(element)
        if tempDiag24w:
            for element in tempDiag24w:
                chainList.append(element)

        if not chainList:
            print('chain3')
            tempHoriz3 = self.chainHoriz3(turn)
            tempVert3 = self.chainVert3(turn)
            tempDiag13 = self.chainDiag13(turn)
            tempDiag23 = self.chainDiag23(turn)
            tempHoriz3w = self.chainHoriz3(opp)
            tempVert3w = self.chainVert3(opp)
            tempDiag13w = self.chainDiag13(opp)
            tempDiag23w = self.chainDiag23(opp)

            if tempHoriz3w:
                for element in tempHoriz3w:
                    chainList.append(element)
            if tempVert3w:
                for element in tempVert3w:
                    chainList.append(element)
            if tempDiag13w:
                for element in tempDiag13w:
                    chainList.append(element)
            if tempDiag23w:
                for element in tempDiag23w:
                    chainList.append(element)
            if tempHoriz3:
                for element in tempHoriz3:
                    chainList.append(element)
            if tempVert3:
                for element in tempVert3:
                    chainList.append(element)
            if tempDiag13:
                for element in tempDiag13:
                    chainList.append(element)
            if tempDiag23:
                for element in tempDiag23:
                    chainList.append(element)

        if not chainList:
            print("chain2")
            tempHoriz2 = self.chainHoriz2(turn)
            tempVert2 = self.chainVert2(turn)
            tempDiag12 = self.chainDiag12(turn)
            tempDiag22 = self.chainDiag22(turn)
            tempHoriz2w = self.chainHoriz2(opp)
            tempVert2w = self.chainVert2(opp)
            tempDiag12w = self.chainDiag12(opp)
            tempDiag22w = self.chainDiag22(opp)

            if tempHoriz2w:
                for element in tempHoriz2w:
                    chainList.append(element)
            if tempVert2w:
                for element in tempVert2w:
                    chainList.append(element)
            if tempDiag12w:
                for element in tempDiag12w:
                    chainList.append(element)
            if tempDiag22w:
                for element in tempDiag22w:
                    chainList.append(element)
            if tempHoriz2:
                for element in tempHoriz2:
                    chainList.append(element)
            if tempVert2:
                for element in tempVert2:
                    chainList.append(element)
            if tempDiag12:
                for element in tempDiag12:
                    chainList.append(element)
            if tempDiag22:
                for element in tempDiag22:
                    chainList.append(element)



        if not chainList:
            print("singles")
            chainList = self.getSingles();

        if chainList:
            for element in chainList:
                # print("begining x: ", element.getPosition()[0], " y: ", element.getPosition()[1])

                tempList.append((element.getPosition()[0]-1) + (element.getPosition()[1]-1)*15)

            tempList = list(set(tempList))
            chainList =[]

            for chain in tempList:
                chainList.append(self.getSpaces()[chain])

        return chainList


        #check horizontal
    def chainHoriz2(self, turn):
        left = False
        right = False
        chainList = []

        #go through eat space and check which ones are viable
        for space in range(0,225):
            if(self.getSpaces()[space].getOccupiedBy() == turn):

                #look at spaces 0 right 4 left
                if (self.getSpaces()[space].getPosition()[0]-2)>0 and (15-self.getSpaces()[space].getPosition()[0])>0:
                    left1=self.getSpaces()[space-1].getOccupiedBy()
                    #check to make sure all these spaces are either blank or the color of the player whose turn it is
                    if (left1 == turn):
                        left = True

                if((15-self.getSpaces()[space].getPosition()[0])>0 and (self.getSpaces()[space].getPosition()[0]-1)>0):
                    right1=self.getSpaces()[space+1].getOccupiedBy()

                    if (right1 == turn):
                        right = True

                if(left):
                    if(self.getSpaces()[space+1].getOccupiedBy() == 2):
                        chainList.append(self.getSpaces()[space+1])
                elif(right):
                     if(self.getSpaces()[space-1].getOccupiedBy() == 2):
                        chainList.append(self.getSpaces()[space-1])

        #returns the number of horizontal rows that have a chance of winning and have 2, 3, 4, or 5 columns
        return (chainList)
            #check horizontal
    def chainHoriz3(self, turn):
        left = False
        right = False
        chainList = []

        #go through eat space and check which ones are viable
        for space in range(0,225):
            if(self.getSpaces()[space].getOccupiedBy() == turn):

                #look at spaces 0 right 4 left
                if (self.getSpaces()[space].getPosition()[0]-2)>0 and (15-self.getSpaces()[space].getPosition()[0])>0:
                    left1=self.getSpaces()[space-1].getOccupiedBy()
                    left2=self.getSpaces()[space-2].getOccupiedBy()
                    #check to make sure all these spaces are either blank or the color of the player whose turn it is
                    if (left1 == turn and left2 == turn):
                        left = True

                if((15-self.getSpaces()[space].getPosition()[0])>1 and (self.getSpaces()[space].getPosition()[0]-1)>0):
                    right1=self.getSpaces()[space+1].getOccupiedBy()
                    right2=self.getSpaces()[space+2].getOccupiedBy()

                    if (right1 == turn and right2 == turn):
                        right = True

                if(left):
                    print(space)
                    if(self.getSpaces()[space+1].getOccupiedBy() == 2):
                        chainList.append(self.getSpaces()[space+1])
                elif(right):
                     if(self.getSpaces()[space-1].getOccupiedBy() == 2):
                        chainList.append(self.getSpaces()[space-1])

        #returns the number of horizontal rows that have a chance of winning and have 2, 3, 4, or 5 columns
        return (chainList)

    def chainHoriz4(self, turn):
        left = False
        right = False
        chainList = []

        #go through eat space and check which ones are viable
        for space in range(0,225):
            if(self.getSpaces()[space].getOccupiedBy() == turn):

                #look at spaces 0 right 4 left
                if (self.getSpaces()[space].getPosition()[0]-3)>0 and (15-self.getSpaces()[space].getPosition()[0])>0:
                    left1=self.getSpaces()[space-1].getOccupiedBy()
                    left2=self.getSpaces()[space-2].getOccupiedBy()
                    left3=self.getSpaces()[space-3].getOccupiedBy()

                    #check to make sure all these spaces are either blank or the color of the player whose turn it is
                    if (left1 == turn and left2 == turn and left3 == turn):
                        left = True

                if((15-self.getSpaces()[space].getPosition()[0])>2 and (self.getSpaces()[space].getPosition()[0]-1)>0):
                    right1=self.getSpaces()[space+1].getOccupiedBy()
                    right2=self.getSpaces()[space+2].getOccupiedBy()
                    right3=self.getSpaces()[space+3].getOccupiedBy()

                    if (right1 == turn and right2 == turn and right3 == turn):
                        right = True

                if(left):
                    if(self.getSpaces()[space+1].getOccupiedBy() == 2):
                        chainList.append(self.getSpaces()[space+1])
                elif(right):
                     if(self.getSpaces()[space-1].getOccupiedBy() == 2):
                        chainList.append(self.getSpaces()[space-1])

        #returns the number of horizontal rows that have a chance of winning and have 2, 3, 4, or 5 columns
        return (chainList)

        #check horizontal
    def chainVert2(self, turn):
        up = False
        down = False
        chainList = []

        #go through eat space and check which ones are viable
        for space in range(0,225):
            if(self.getSpaces()[space].getOccupiedBy() == turn):

                #look at spaces 0 right 4 left
                if (self.getSpaces()[space].getPosition()[1]-1)>0 and (15-self.getSpaces()[space].getPosition()[1])>0:
                    up1=self.getSpaces()[space-15].getOccupiedBy()
                    #check to make sure all these spaces are either blank or the color of the player whose turn it is
                    if (up1 == turn):
                        up = True

                if((15-self.getSpaces()[space].getPosition()[1])>0 and (self.getSpaces()[space].getPosition()[1]-1)>0):
                    down1=self.getSpaces()[space+15].getOccupiedBy()

                    if (down1 == turn):
                        down = True

                if(up):
                    if(self.getSpaces()[space+15].getOccupiedBy() == 2):
                        chainList.append(self.getSpaces()[space+15])
                elif(down):
                     if(self.getSpaces()[space-15].getOccupiedBy() == 2):
                        chainList.append(self.getSpaces()[space-15])

        #returns the number of horizontal rows that have a chance of winning and have 2, 3, 4, or 5 columns
        return (chainList)

    def chainVert3(self, turn):
        up = False
        down = False
        chainList = []

        #go through eat space and check which ones are viable
        for space in range(0,225):
            if(self.getSpaces()[space].getOccupiedBy() == turn):

                #look at spaces 0 right 4 left
                if (self.getSpaces()[space].getPosition()[1]-2)>0 and (15-self.getSpaces()[space].getPosition()[1])>0:
                    up1=self.getSpaces()[space-15].getOccupiedBy()
                    up2=self.getSpaces()[space-30].getOccupiedBy()
                    #check to make sure all these spaces are either blank or the color of the player whose turn it is
                    if (up1 == turn and up2 == turn):
                        up = True

                if((15-self.getSpaces()[space].getPosition()[1])>1 and (self.getSpaces()[space].getPosition()[1]-1)>0):
                    down1=self.getSpaces()[space+15].getOccupiedBy()
                    down2=self.getSpaces()[space+30].getOccupiedBy()

                    if (down1 == turn and down2 == turn):
                        down = True

                if(up):
                    if(self.getSpaces()[space+15].getOccupiedBy() == 2):
                        chainList.append(self.getSpaces()[space+15])
                elif(down):
                     if(self.getSpaces()[space-15].getOccupiedBy() == 2):
                        chainList.append(self.getSpaces()[space-15])

        #returns the number of horizontal rows that have a chance of winning and have 2, 3, 4, or 5 columns
        return (chainList)

    def chainVert4(self, turn):
        up = False
        down = False
        chainList = []

        #go through eat space and check which ones are viable
        for space in range(0,225):
            if(self.getSpaces()[space].getOccupiedBy() == turn):

                #look at spaces 0 right 4 left
                if (self.getSpaces()[space].getPosition()[1]-3)>0 and (15-self.getSpaces()[space].getPosition()[1])>0:
                    up1=self.getSpaces()[space-15].getOccupiedBy()
                    up2=self.getSpaces()[space-30].getOccupiedBy()
                    up3=self.getSpaces()[space-45].getOccupiedBy()
                    #check to make sure all these spaces are either blank or the color of the player whose turn it is
                    if (up1 == turn and up2 == turn and up3 == turn):
                        up = True

                if((15-self.getSpaces()[space].getPosition()[1])>2 and (self.getSpaces()[space].getPosition()[1]-1)>0):
                    down1=self.getSpaces()[space+15].getOccupiedBy()
                    down2=self.getSpaces()[space+30].getOccupiedBy()
                    down3=self.getSpaces()[space+45].getOccupiedBy()

                    if (down1 == turn and down2 == turn and down3 == turn):
                        down = True

                if(up):
                    print(space)
                    if(self.getSpaces()[space+15].getOccupiedBy() == 2):
                        chainList.append(self.getSpaces()[space+15])
                elif(down):
                     if(self.getSpaces()[space-15].getOccupiedBy() == 2):
                        chainList.append(self.getSpaces()[space-15])

        #returns the number of horizontal rows that have a chance of winning and have 2, 3, 4, or 5 columns
        return (chainList)


    def chainDiag12(self, turn):
        upLeft = False
        downRight = False
        chainList = []

        #go through eat space and check which ones are viable
        for space in range(0,225):
            if(self.getSpaces()[space].getOccupiedBy() == turn):

                #look at spaces 0 right 4 left
                if (self.getSpaces()[space].getPosition()[0]-1)>0 and (self.getSpaces()[space].getPosition()[1]-1)>0 and (15-self.getSpaces()[space].getPosition()[0])>0 and (15-self.getSpaces()[space].getPosition()[1])>0:
                    upLeft1=self.getSpaces()[space-16].getOccupiedBy()
                    #check to make sure all these spaces are either blank or the color of the player whose turn it is
                    if (upLeft1 == turn):
                        upLeft = True

                if((15-self.getSpaces()[space].getPosition()[0])>0 and (15-self.getSpaces()[space].getPosition()[1])>0 and self.getSpaces()[space].getPosition()[0]-1)>0 and (self.getSpaces()[space].getPosition()[1]-1)>0:
                    downRight1=self.getSpaces()[space+16].getOccupiedBy()

                    if (downRight1 == turn):
                        downRight = True

                if(upLeft):
                    if(self.getSpaces()[space+16].getOccupiedBy() == 2):
                        chainList.append(self.getSpaces()[space+16])
                elif(downRight):
                     if(self.getSpaces()[space-16].getOccupiedBy() == 2):
                        chainList.append(self.getSpaces()[space-16])

        #returns the number of horizontal rows that have a chance of winning and have 2, 3, 4, or 5 columns
        return (chainList)


    def chainDiag13(self, turn):
        upLeft = False
        downRight = False
        chainList = []

        #go through eat space and check which ones are viable
        for space in range(0,225):
            if(self.getSpaces()[space].getOccupiedBy() == turn):

                #look at spaces 0 right 4 left
                if (self.getSpaces()[space].getPosition()[0]-2)>0 and (self.getSpaces()[space].getPosition()[1]-2)>0 and (15-self.getSpaces()[space].getPosition()[0])>0 and (15-self.getSpaces()[space].getPosition()[1])>0:
                    upLeft1=self.getSpaces()[space-16].getOccupiedBy()
                    upLeft2=self.getSpaces()[space-32].getOccupiedBy()
                    #check to make sure all these spaces are either blank or the color of the player whose turn it is
                    if (upLeft1 == turn and upLeft2 == turn):
                        upLeft = True

                if((15-self.getSpaces()[space].getPosition()[0])>1 and (15-self.getSpaces()[space].getPosition()[1])>1 and self.getSpaces()[space].getPosition()[0]-1)>0 and (self.getSpaces()[space].getPosition()[1]-1)>0:
                    downRight1=self.getSpaces()[space+16].getOccupiedBy()
                    downRight2=self.getSpaces()[space+32].getOccupiedBy()

                    if (downRight1 == turn and downRight2 == turn):
                        downRight = True

                if(upLeft):
                    if(self.getSpaces()[space+16].getOccupiedBy() == 2):
                        chainList.append(self.getSpaces()[space+16])
                elif(downRight):
                     if(self.getSpaces()[space-16].getOccupiedBy() == 2):
                        chainList.append(self.getSpaces()[space-16])

        #returns the number of horizontal rows that have a chance of winning and have 2, 3, 4, or 5 columns
        return (chainList)

    def chainDiag14(self, turn):
        upLeft = False
        downRight = False
        chainList = []

        #go through eat space and check which ones are viable
        for space in range(0,225):
            if(self.getSpaces()[space].getOccupiedBy() == turn):

                #look at spaces 0 right 4 left
                if (self.getSpaces()[space].getPosition()[0]-3)>0 and (self.getSpaces()[space].getPosition()[1]-3)>0 and (15-self.getSpaces()[space].getPosition()[0])>0 and (15-self.getSpaces()[space].getPosition()[1])>0:
                    upLeft1=self.getSpaces()[space-16].getOccupiedBy()
                    upLeft2=self.getSpaces()[space-32].getOccupiedBy()
                    upLeft3=self.getSpaces()[space-48].getOccupiedBy()
                    #check to make sure all these spaces are either blank or the color of the player whose turn it is
                    if (upLeft1 == turn and upLeft2 == turn and upLeft3 == turn):
                        upLeft = True

                if((15-self.getSpaces()[space].getPosition()[0])>2 and (15-self.getSpaces()[space].getPosition()[1])>2 and self.getSpaces()[space].getPosition()[0]-1)>0 and (self.getSpaces()[space].getPosition()[1]-1)>0:
                    downRight1=self.getSpaces()[space+16].getOccupiedBy()
                    downRight2=self.getSpaces()[space+32].getOccupiedBy()
                    downRight3=self.getSpaces()[space+48].getOccupiedBy()

                    if (downRight1 == turn and downRight2 == turn and downRight3 == turn):
                        downRight = True

                if(upLeft):
                    if(self.getSpaces()[space+16].getOccupiedBy() == 2):
                        chainList.append(self.getSpaces()[space+16])
                elif(downRight):
                     if(self.getSpaces()[space-16].getOccupiedBy() == 2):
                        chainList.append(self.getSpaces()[space-16])

        #returns the number of horizontal rows that have a chance of winning and have 2, 3, 4, or 5 columns
        return (chainList)


    def chainDiag22(self, turn):
        upRight = False
        downLeft = False
        chainList = []

        #go through eat space and check which ones are viable
        for space in range(0,225):
            if(self.getSpaces()[space].getOccupiedBy() == turn):

                #look at spaces 0 right 4 left
                if (self.getSpaces()[space].getPosition()[1]-1)>0 and (15-self.getSpaces()[space].getPosition()[0])>0 and (self.getSpaces()[space].getPosition()[0]-1)>0 and (15-self.getSpaces()[space].getPosition()[1])>0:
                    upRight1=self.getSpaces()[space-14].getOccupiedBy()
                    #check to make sure all these spaces are either blank or the color of the player whose turn it is
                    if (upRight1 == turn):
                        upRight = True

                if((self.getSpaces()[space].getPosition()[0]-1)>0 and (15-self.getSpaces()[space].getPosition()[1])>0 and self.getSpaces()[space].getPosition()[1]-1)>0 and (15-self.getSpaces()[space].getPosition()[0])>0:
                    downLeft1=self.getSpaces()[space+14].getOccupiedBy()

                    if (downLeft1 == turn):
                        downLeft = True

                if(upRight):
                    if(self.getSpaces()[space+14].getOccupiedBy() == 2):
                        chainList.append(self.getSpaces()[space+14])
                elif(downLeft):
                     if(self.getSpaces()[space-14].getOccupiedBy() == 2):
                        chainList.append(self.getSpaces()[space-14])

        #returns the number of horizontal rows that have a chance of winning and have 2, 3, 4, or 5 columns
        return (chainList)

    def chainDiag23(self, turn):
        upRight = False
        downLeft = False
        chainList = []

        #go through eat space and check which ones are viable
        for space in range(0,225):
            if(self.getSpaces()[space].getOccupiedBy() == turn):

                #look at spaces 0 right 4 left
                if (self.getSpaces()[space].getPosition()[1]-2)>0 and (15-self.getSpaces()[space].getPosition()[0])>1 and (self.getSpaces()[space].getPosition()[0]-1)>0 and (15-self.getSpaces()[space].getPosition()[1])>0:
                    upRight1=self.getSpaces()[space-14].getOccupiedBy()
                    upRight2=self.getSpaces()[space-28].getOccupiedBy()
                    #check to make sure all these spaces are either blank or the color of the player whose turn it is
                    if (upRight1 == turn and upRight2 == turn):
                        upRight = True

                if((self.getSpaces()[space].getPosition()[0]-2)>0 and (15-self.getSpaces()[space].getPosition()[1])>1 and self.getSpaces()[space].getPosition()[1]-1)>0 and (15-self.getSpaces()[space].getPosition()[0])>0:
                    downLeft1=self.getSpaces()[space+14].getOccupiedBy()
                    downLeft2=self.getSpaces()[space+28].getOccupiedBy()

                    if (downLeft1 == turn and downLeft2 == turn):
                        downLeft = True

                if(upRight):
                    if(self.getSpaces()[space+14].getOccupiedBy() == 2):
                        chainList.append(self.getSpaces()[space+14])
                elif(downLeft):
                     if(self.getSpaces()[space-14].getOccupiedBy() == 2):
                        chainList.append(self.getSpaces()[space-14])

        #returns the number of horizontal rows that have a chance of winning and have 2, 3, 4, or 5 columns
        return (chainList)

    def chainDiag24(self, turn):
        upRight = False
        downLeft = False
        chainList = []

        #go through eat space and check which ones are viable
        for space in range(0,225):
            if(self.getSpaces()[space].getOccupiedBy() == turn):

                #look at spaces 0 right 4 left
                if (self.getSpaces()[space].getPosition()[1]-3)>0 and (15-self.getSpaces()[space].getPosition()[0])>2 and (self.getSpaces()[space].getPosition()[0]-1)>0 and (15-self.getSpaces()[space].getPosition()[1])>0:
                    upRight1=self.getSpaces()[space-14].getOccupiedBy()
                    upRight2=self.getSpaces()[space-28].getOccupiedBy()
                    upRight3=self.getSpaces()[space-42].getOccupiedBy()
                    #check to make sure all these spaces are either blank or the color of the player whose turn it is
                    if (upRight1 == turn and upRight2 == turn and upRight3 == turn):
                        upRight = True

                if((self.getSpaces()[space].getPosition()[0]-3)>0 and (15-self.getSpaces()[space].getPosition()[1])>2 and self.getSpaces()[space].getPosition()[1]-1)>0 and (15-self.getSpaces()[space].getPosition()[0])>0:
                    downLeft1=self.getSpaces()[space+14].getOccupiedBy()
                    downLeft2=self.getSpaces()[space+28].getOccupiedBy()
                    downLeft3=self.getSpaces()[space+42].getOccupiedBy()

                    if (downLeft1 == turn and downLeft2 == turn and downLeft3 == turn):
                        downLeft = True

                if(upRight):
                    if(self.getSpaces()[space+14].getOccupiedBy() == 2):
                        chainList.append(self.getSpaces()[space+14])
                elif(downLeft):
                     if(self.getSpaces()[space-14].getOccupiedBy() == 2):
                        chainList.append(self.getSpaces()[space-14])

        #returns the number of horizontal rows that have a chance of winning and have 2, 3, 4, or 5 columns
        return (chainList)


    def getSingles(self):

        turn = self.whoseTurn()
        children = []

        for tile in self.getSpaces():

            upLeft = -1
            up = -1
            upRight = -1
            left = -1
            right = -1
            downLeft = -1
            down = -1
            downRight = -1
            check = False

            if not tile.getIsFilled():

                currentPosX = tile.getPosition()[0]
                currentPosY = tile.getPosition()[1]
                currentPos = ((tile.getPosition()[1]-1)*15) + (tile.getPosition()[0]-1)
                if(currentPosX -1 > 0 and currentPosY -1 > 0):
                    upLeft = currentPos -16
                if(currentPosY -1 > 0):
                    up = currentPos - 15
                if(15-currentPosX > 0 and currentPosY -1 > 0):
                    upRight = currentPos - 14
                if(currentPosX -1 > 0):
                    left = currentPos -1
                if(15-currentPosX > 0):
                    right = currentPos + 1
                if(currentPosX -1 > 0 and 15 - currentPosY > 0):
                    downLeft = currentPos + 14
                if(15 - currentPosY > 0):
                    down = currentPos + 15
                if(15-currentPosX > 0 and 15 - currentPosY > 0):
                    downRight = currentPos + 16


                if(upLeft != -1):
                    if(self.getSpaces()[upLeft].getOccupiedBy() != 2 and self.getSpaces()[upLeft].getOccupiedBy() == turn):
                        #print("upLeft", self.getSpaces()[upLeft].getOccupiedBy(), " current turn ", turn)
                        children.append(tile)
                if(up != -1):
                    if (self.getSpaces()[up].getOccupiedBy() != 2 and self.getSpaces()[up].getOccupiedBy() == turn):
                        #print("up", self.getSpaces()[up].getOccupiedBy(), " current turn ", turn)
                        children.append(tile)
                if (upRight != -1):
                    if (self.getSpaces()[upRight].getOccupiedBy() != 2 and self.getSpaces()[upRight].getOccupiedBy() == turn):
                        #print("upRight", self.getSpaces()[upRight].getOccupiedBy(), " current turn ", turn)
                        children.append(tile)
                if (left != -1):
                    if (self.getSpaces()[left].getOccupiedBy() != 2 and self.getSpaces()[left].getOccupiedBy() == turn):
                        #print("left", self.getSpaces()[left].getOccupiedBy(), " current turn ", turn)
                        children.append(tile)
                if (right != -1):
                    if (self.getSpaces()[right].getOccupiedBy() != 2 and self.getSpaces()[right].getOccupiedBy() == turn):
                        #print("right", self.getSpaces()[right].getOccupiedBy(), " current turn ", turn)
                        children.append(tile)
                if (downLeft != -1):
                    if (self.getSpaces()[downLeft].getOccupiedBy() != 2 and self.getSpaces()[downLeft].getOccupiedBy() == turn):
                        #print("downLeft", self.getSpaces()[downLeft].getOccupiedBy(), " current turn ", turn)
                        children.append(tile)
                if (down != -1):
                    if (self.getSpaces()[down].getOccupiedBy() != 2 and self.getSpaces()[down].getOccupiedBy() == turn):
                        #print("down", self.getSpaces()[down].getOccupiedBy(), " current turn ", turn)
                        children.append(tile)
                if (downRight != -1):
                    if (self.getSpaces()[downRight].getOccupiedBy() != 2 and self.getSpaces()[downRight].getOccupiedBy() == turn):
                        #print("downRight", self.getSpaces()[downRight].getOccupiedBy(), " current turn ", turn)
                        children.append(tile)

        return children
