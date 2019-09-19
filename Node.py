import copy
# Class for defining given position reached
class Node:
    def __init__(self, squareDistribution, father, high, emptySpacePositionX, emptySpacePositionY, cost = -1):
        self.squareDistribution = squareDistribution
        self.cost = cost
        self.father = father
        self.high = high
        self.emptySpacePositionX = emptySpacePositionX
        self.emptySpacePositionY = emptySpacePositionY
    
    def getLeftDistribution(self):
        if self.emptySpacePositionX == 0: #Cant move left 
            return None
        squareDistribution = copy.deepcopy(self.squareDistribution)
        squareDistribution[self.emptySpacePositionX][self.emptySpacePositionY] = self.squareDistribution[self.emptySpacePositionX - 1][self.emptySpacePositionY] 
        squareDistribution[self.emptySpacePositionX - 1][self.emptySpacePositionY] = '-1'
        return squareDistribution
    
    def getRightDistribution(self):
        if self.emptySpacePositionX == 2: #Cant move right
            return None
        squareDistribution = copy.deepcopy(self.squareDistribution)
        squareDistribution[self.emptySpacePositionX][self.emptySpacePositionY] = self.squareDistribution[self.emptySpacePositionX + 1][self.emptySpacePositionY] 
        squareDistribution[self.emptySpacePositionX + 1][self.emptySpacePositionY] = '-1'
        return squareDistribution
    
    def getUpDistribution(self):
        if self.emptySpacePositionY == 0: #Cant move up
            return None
        squareDistribution = copy.deepcopy(self.squareDistribution)
        squareDistribution[self.emptySpacePositionX][self.emptySpacePositionY] = self.squareDistribution[self.emptySpacePositionX][self.emptySpacePositionY-1] 
        squareDistribution[self.emptySpacePositionX][self.emptySpacePositionY - 1]  = '-1'
        return squareDistribution
    
    def getDownDistribution(self):
        if self.emptySpacePositionY == 2: #Cant move down
            return None
        squareDistribution = copy.deepcopy(self.squareDistribution)
        squareDistribution[self.emptySpacePositionX][self.emptySpacePositionY] = self.squareDistribution[self.emptySpacePositionX][self.emptySpacePositionY + 1] 
        squareDistribution[self.emptySpacePositionX][self.emptySpacePositionY + 1] = '-1'
        return squareDistribution

    def toString(self):  #returns the distribution matrix as a String
        s = ''
        for i in range(0 , 3):
            for h in range(0 , 3):
                s = s + self.squareDistribution[i][h] #concatenates every number in the square in a secuencial way
        return s
    
