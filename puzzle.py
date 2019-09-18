#Main class

from bestFS import Node
from FSPriorityQueue import FSPriorityQueue
from FSOrderedList import FSOrderedList

FINAL_STATE = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]

class Puzzle:
    def __init__(self, initialState):        
        self.initialState = initialState
        self.newStates = FSPriorityQueue() 
        self.visitedStates = FSOrderedList()       
    
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

    def puzzleMethod(self):
        self.newStates.put(self.initialState, 0) #Put the initial state to the states queue
        self.searchForSolution()

    def searchForSolution(self):
        if not self.newStates.empty(): #Check if the new states queue is empty
            state = self.newStates.get()  #Get the better state
            self.visitedStates.add(state) #Move the bettter state to the visited list (Consult if this is the correct place (*)) 
            if state.squareDistribution == FINAL_STATE: #Base condition
                #Save in the LIFO the position (*)
                return True  
            else:
                #Try to create the childs
                #Remember we must check if the new child exist in the visited states!!!! (*)
                #Up move
                if state.getUpDistribution:
                    up = Node(state.getUpDistribution, state, state.high + 1, state.emptySpacePositionX, state.emptySpacePositionY - 1)
                    self._heuristic(up) #Update cost
                    self.newStates.put(up, up.cost) #Put the new child state to the states queue
                #Down move    
                if state.getDownDistribution:
                    down = Node(state.getDownDistribution, state, state.high + 1, state.emptySpacePositionX, state.emptySpacePositionY + 1)
                    self._heuristic(down) #Update cost
                    self.newStates.put(down, down.cost) #Put the new child state to the states queue
                #Left move    
                if state.getLeftDistribution:
                    left = Node(state.getLeftDistribution, state, state.high + 1, state.emptySpacePositionX - 1, state.emptySpacePositionY)
                    self._heuristic(left) #Update cost
                    self.newStates.put(left, left.cost) #Put the new child state to the states queue
                #Right move
                if state.getRightDistribution:
                    right = Node(state.getRightDistribution, state, state.high + 1, state.emptySpacePositionX + 1, state.emptySpacePositionY)
                    self._heuristic(right) #Update cost
                    self.newStates.put(right, right.cost) #Put the new child state to the states queue    

            found = self.searchForSolution()  #Recursive call
            if found:
                True #Save in the LIFO the position of this state(*)
            return found    
        return False
