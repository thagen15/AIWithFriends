class Space():
    """docstring for space."""
    def __init__(self, xPos,yPos):
        self.isFilled = False
        self.position = [xPos,yPos]
        #0 is white, 1 is black, 2 is empty
        self.occupiedBy = 2

    #Fill the space with a players color
    def fill(self, player):
        self.isFilled = True
        self.occupiedBy = player

    def getIsFilled(self):
        return self.isFilled

    def getOccupiedBy(self):
        return self.occupiedBy

    def getPosition(self):
        return self.position
