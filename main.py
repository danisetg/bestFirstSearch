from Puzzle import Puzzle
from Node import Node

print("Introduzca el número de casos que desee comprobar")
tests = int(input()) #Number of test cases
for i in range(0, tests): 
    initialDistrib = [[],[],[]] #initialize initial distribution matrix
    finalDistrib = [[],[],[]] #initialize final distribution matrix
    emptyPositionColumn = 0
    emptyPositionRow = 0
    print("Introduzca la distribución inicial del puzzle, use '-1' para el cuadro vacío")
    for h in range(0,3): #input the three rows of distribution numbers
        initialDistrib[h] = (input().split(' '))
        for k in range(0, 3):
            if (initialDistrib[h][k] == '-1'):
                emptyPositionColumn = k
                emptyPositionRow = h

    initialNode = Node(initialDistrib, None, 0, emptyPositionRow, emptyPositionColumn)
    print("Introduzca la distribución final del puzzle, use '-1' para el cuadro vacío")
    for h in range(0,3): #input the three rows of distribution numbers
        finalDistrib[h] = (input().split(' '))
    puzzle = Puzzle()
    print(puzzle.puzzleMethod(initialNode, finalDistrib))
