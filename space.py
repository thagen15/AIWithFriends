class Space():
    """docstring for space."""
    def __init__(self, xPos,yPos):
        self.isFilled = False
        self.position = [xPos,yPos]
        self.occupiedBy = 2

    def fill(self, player):
        self.isFilled = True
        self.occupiedBy = player

    def getIsFilled(self):
        return self.isFilled
    def getOccupiedBy(self):
        return self.occupiedBy
    def getPosition(self):
        return self.position
