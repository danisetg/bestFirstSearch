import copy
# Class for defining given position reached
class Node:
    def __init__(self, squareDistribution, father, high, emptySpacePositionRow, emptySpacePositionColumn, cost = -1):
        self.squareDistribution = squareDistribution
        self.cost = cost
        self.father = father
        self.high = high
        self.emptySpacePositionRow = emptySpacePositionRow
        self.emptySpacePositionColumn = emptySpacePositionColumn
    
    def getLeftDistribution(self):
        if self.emptySpacePositionColumn == 0: #Cant move left 
            return None
        squareDistribution = copy.deepcopy(self.squareDistribution)
        squareDistribution[self.emptySpacePositionRow][self.emptySpacePositionColumn] = self.squareDistribution[self.emptySpacePositionRow][self.emptySpacePositionColumn - 1] 
        squareDistribution[self.emptySpacePositionRow][self.emptySpacePositionColumn - 1] = '-1'
        return squareDistribution
    
    def getRightDistribution(self):
        if self.emptySpacePositionColumn == 2: #Cant move right
            return None
        squareDistribution = copy.deepcopy(self.squareDistribution)
        squareDistribution[self.emptySpacePositionRow][self.emptySpacePositionColumn] = self.squareDistribution[self.emptySpacePositionRow][self.emptySpacePositionColumn + 1] 
        squareDistribution[self.emptySpacePositionRow][self.emptySpacePositionColumn + 1] = '-1'
        return squareDistribution
    
    def getUpDistribution(self):
        if self.emptySpacePositionRow == 0: #Cant move up
            return None
        squareDistribution = copy.deepcopy(self.squareDistribution)
        squareDistribution[self.emptySpacePositionRow][self.emptySpacePositionColumn] = self.squareDistribution[self.emptySpacePositionRow - 1][self.emptySpacePositionColumn] 
        squareDistribution[self.emptySpacePositionRow - 1][self.emptySpacePositionColumn]  = '-1'
        return squareDistribution
    
    def getDownDistribution(self):
        if self.emptySpacePositionRow == 2: #Cant move down
            return None
        squareDistribution = copy.deepcopy(self.squareDistribution)
        squareDistribution[self.emptySpacePositionRow][self.emptySpacePositionColumn] = self.squareDistribution[self.emptySpacePositionRow + 1][self.emptySpacePositionColumn] 
        squareDistribution[self.emptySpacePositionRow + 1][self.emptySpacePositionColumn] = '-1'
        return squareDistribution

    def toString(self):  #returns the distribution matrix as a String
        s = ''
        for i in range(0 , 3):
            for h in range(0 , 3):
                s = s + self.squareDistribution[i][h] #concatenates every number in the square in a secuencial way
        return s
    
