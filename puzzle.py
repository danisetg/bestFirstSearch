#Main class

from bestFS import Node

FINAL_STATE = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]

class Puzzle:
    def __init__(self, initialState):
        self.initialState = initialState        
    
    def _heuristic(self, state):                
        i = 0
        count = 0
        while (i < 9): #Count the wrong positions
            x = i % 3 #To get x coordinates
            y = i // 3 #To get y coordinates
            if state.squareDistribution[x][y] != FINAL_STATE[x][y]:
                count += 1
            i +=1
        state.cost = state.high + count
    
    