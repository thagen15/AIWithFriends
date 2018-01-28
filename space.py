class Space(object):
    """docstring for space."""
    def __init__(self, xPos,yPos):
        super(space, self).__init__()
        self.isFilled = False
        self.position = [xPos,yPos]

    def fill(player):
        self.isFilled = True
        self.occupiedBy = player
    def getIsFilled(self):
        return self.isFilled
    def getPosition(self):
        return self.position
