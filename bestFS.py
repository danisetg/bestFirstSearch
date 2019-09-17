# Class for defining given position reached
class Node:
    def __init__(self, squareDistribution, cost, father, high, emptySpacePositionX, emptySpacePositionY):
        self.squareDistribution = squareDistribution
        self.cost = cost
        self.father = father
        self.high = high
        self.emptySpacePositionX = emptySpacePositionX
        self.emptySpacePositionY = emptySpacePositionY
    
    def moveUp(self):
        self.squareDistribution[self.emptySpacePositionX][self.emptySpacePositionY] = self.squareDistribution[self.emptySpacePositionX - 1][self.emptySpacePositionY] 
        self.squareDistribution[self.emptySpacePositionX - 1][self.emptySpacePositionY] = -1
        self.emptySpacePositionX -= 1
    
    def moveDown(self):
        self.squareDistribution[self.emptySpacePositionX][self.emptySpacePositionY] = self.squareDistribution[self.emptySpacePositionX + 1][self.emptySpacePositionY] 
        self.squareDistribution[self.emptySpacePositionX + 1][self.emptySpacePositionY] = -1
        self.emptySpacePositionX += 1
    
    def moveLeft(self):
        self.squareDistribution[self.emptySpacePositionX][self.emptySpacePositionY] = self.squareDistribution[self.emptySpacePositionX][self.emptySpacePositionY-1] 
        self.squareDistribution[self.emptySpacePositionX][self.emptySpacePositionY - 1]  = -1
        self.emptySpacePositionY -= 1
    
    def moveRigth(self):
        self.squareDistribution[self.emptySpacePositionX][self.emptySpacePositionY] = self.squareDistribution[self.emptySpacePositionX][self.emptySpacePositionY + 1] 
        self.squareDistribution[self.emptySpacePositionX][self.emptySpacePositionY + 1] = -1
        self.emptySpacePositionX += 1



print("Introduce the number of test cases:")
t = input()
print(t)
for i in range(0, int(t)):
    print("Introduce the initial Square distribution. Use '-1' for empty square")
    distrib = [[0 for x in range(3)] for y in range(3)] 
    for x in range(0, 3):
            distrib[x] = input().split()
    print(distrib)