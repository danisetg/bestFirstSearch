#Main class

import math

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

        if self._isSolvable() == True:
            self.newStates.put(self.initialState, 0) #Put the initial state to the states queue
            list = []
            if self._searchForSolution() == True:
                self._getPath(list)  #To get the movements        
            list.reverse()
            return list
        return "There is not solution for this case!!!" 

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
        list.append('Done')        
        while not(self.solution.father is None):                        
            row =  self.solution.emptySpacePositionRow - self.solution.father.emptySpacePositionRow # Horizontal move
            column =  self.solution.emptySpacePositionColumn - self.solution.father.emptySpacePositionColumn # Vertical move
            if column != 0:  # Left or right move
                if column < 0:
                    list.append('Left')
                else:
                    list.append('Right')
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
    
    def _printState(self, distribution):        
        for i in range(len(distribution[0])):
            for j in range(len(distribution)):
                print(distribution[j][i], end="")
            print("") 
        print("------")

    def _isSolvable(self):
        # Convertions the states to strings and eliminate the -1 character
        iState = self.initialState.toString().replace('-1', '')
        fState = ("".join(self.finalState[0]) + "".join(self.finalState[1]) + "".join(self.finalState[2])).replace('-1', '') # This is not the optimal code, but works
        count = 0
        for i in range(len(fState)):                        
            count += self._distance(iState, fState[i])
            iState = iState.replace(fState[i], '')  # To delete the processed value
        return count % 2 == 0
    
    def _distance(self, iState, value):
        for i in range(len(iState)):
            if value == iState[i]:
                return i
