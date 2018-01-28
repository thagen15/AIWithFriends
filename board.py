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
