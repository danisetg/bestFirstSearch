# Class for defining given position reached
class Node:
    def __init__(self, squareDistribution, father, high, emptySpacePositionX, emptySpacePositionY, cost = -1):
        self.squareDistribution = squareDistribution
        self.cost = cost
        self.father = father
        self.high = high
        self.emptySpacePositionX = emptySpacePositionX
        self.emptySpacePositionY = emptySpacePositionY
    
    def getUpDistribution(self):
        squareDistribution = self.squareDistribution
        squareDistribution[self.emptySpacePositionX][self.emptySpacePositionY] = self.squareDistribution[self.emptySpacePositionX - 1][self.emptySpacePositionY] 
        squareDistribution[self.emptySpacePositionX - 1][self.emptySpacePositionY] = -1
        return squareDistribution
    
    def getDownDistribution(self):
        squareDistribution = self.squareDistribution
        squareDistribution[self.emptySpacePositionX][self.emptySpacePositionY] = self.squareDistribution[self.emptySpacePositionX + 1][self.emptySpacePositionY] 
        squareDistribution[self.emptySpacePositionX + 1][self.emptySpacePositionY] = -1
        return squareDistribution
    
    def getLeftDistribution(self):
        squareDistribution = self.squareDistribution
        squareDistribution[self.emptySpacePositionX][self.emptySpacePositionY] = self.squareDistribution[self.emptySpacePositionX][self.emptySpacePositionY-1] 
        squareDistribution[self.emptySpacePositionX][self.emptySpacePositionY - 1]  = -1
        return squareDistribution
    
    def getRightDistribution(self):
        squareDistribution = self.squareDistribution
        squareDistribution[self.emptySpacePositionX][self.emptySpacePositionY] = self.squareDistribution[self.emptySpacePositionX][self.emptySpacePositionY + 1] 
        squareDistribution[self.emptySpacePositionX][self.emptySpacePositionY + 1] = -1
        emptySpacePositionX += 1
    
