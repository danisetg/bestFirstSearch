#Main class

from Node import Node
from FSPriorityQueue import FSPriorityQueue
from FSOrderedList import HashTable

class Puzzle:
    def __init__(self):        
        self.initialState = None
        self.newStates = FSPriorityQueue() 
        self.visitedStates = HashTable()
        self.solution = None       
        self.finalState = None

    def puzzleMethod(self, initialState, finalState):
        self.initialState = initialState
        self.finalState = finalState
        self.newStates.put(self.initialState, 0) #Put the initial state to the states queue
        list = []
        if self._searchForSolution() == True:
            self._getPath(list)  #To get the movements        
        list.reverse()
        return list

    def _searchForSolution(self):
        while (not self.newStates.empty()) and (self.solution is None): #Check if the new states queue is empty (Q ≠ Ø) and (P ∩ Q = Ø) who represent the not found solution
            state = self.newStates.get()  #Get the better state
            self.visitedStates.Insert(state.toString()) #Put the state to the visited list (Consult if this is the correct place (*)) 
            if state.squareDistribution == self.finalState: #Base condition (P ∩ Q = Ø)
                self.solution = state
                return True  
            else:
                self._expand(state)                                       
        return False 
    
    def _heuristic(self, state):                
        i = 0
        count = 0
        while (i < 9): #Count the wrong positions
            x = i % 3 #To get x coordinates
            y = i // 3 #To get y coordinates
            if state.squareDistribution[x][y] != self.finalState[x][y]:
                count += 1
            i +=1
        state.cost = state.high + count
    
    def _getPath(self, list):        
        while not(self.solution.father is None):
            row =  self.solution.emptySpacePositionRow - self.solution.father.emptySpacePositionRow # Horizontal move
            column =  self.solution.emptySpacePositionColumn - self.solution.father.emptySpacePositionColumn # Vertical move
            if column != 0:  # Left or right move
                if column < 0:
                    list.append('Left')
                else:
                    list.append('Rigth')
            else: # Up or down move
                if row < 0:
                    list.append('Up')
                else:
                    list.append('Down')
            self.solution = self.solution.father        
    
    def _expand(self, state):
        #Try to create the childs
        #Remember we must check if the new child exist in the visited states!!!! (*)
        #Up move
        if not(state.getUpDistribution() is None):
            up = Node(state.getUpDistribution(), state, state.high + 1, state.emptySpacePositionRow - 1, state.emptySpacePositionColumn)
            self._heuristic(up) #Update cost
            if self.visitedStates.Search(up.toString()) is None:
                self.newStates.put(up, up.cost) #Put the new child state to the states queue
        #Down move    
        if not(state.getDownDistribution() is None):
            down = Node(state.getDownDistribution(), state, state.high + 1, state.emptySpacePositionRow + 1, state.emptySpacePositionColumn)
            self._heuristic(down) #Update cost
            if self.visitedStates.Search(down.toString()) is None:
                self.newStates.put(down, down.cost) #Put the new child state to the states queue
        #Left move    
        if not(state.getLeftDistribution() is None):
            left = Node(state.getLeftDistribution(), state, state.high + 1, state.emptySpacePositionRow, state.emptySpacePositionColumn - 1)
            self._heuristic(left) #Update cost
            if self.visitedStates.Search(left.toString()) is None:
                self.newStates.put(left, left.cost) #Put the new child state to the states queue
        #Right move
        if not(state.getRightDistribution() is None):
            right = Node(state.getRightDistribution(), state, state.high + 1, state.emptySpacePositionRow, state.emptySpacePositionColumn + 1)
            self._heuristic(right) #Update cost
            if self.visitedStates.Search(right.toString()) is None:
                self.newStates.put(right, right.cost) #Put the new child state to the states queue