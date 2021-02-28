import time
import os

SIZE = int(input("Enter SIZE for the board: "))
STEP = 0

class Board:

    empty = ' [{}]'
    traversed = 'V'
    horse = 'H' 

    def __init__(self,x, y):    # constructor
        self.x = x
        self.y = y

        self.color = Board.empty.format(' ')
        self.is_traversed = False

        self.step = 0
    
    def getStep(self):
        if self.step <= 9:
            self.color = Board.empty.format('0' + str(self.step))
        else:
            self.color = Board.empty.format(self.step)
        return self.color

    def setKnight(self):
        global STEP
        self.is_traversed = True

        STEP = STEP + 1
        self.step = STEP
        print("Next Step:",self.step)
        self.color = Board.empty.format(Board.horse)

    def isTraversed(self):
        return self.is_traversed
    pass

# BOARD = [[ Board(j,i) for i in range(1, SIZE+1) ] for j in range(1, SIZE+1)]
BOARD = [[ Board(j,i) for i in range(SIZE) ] for j in range(SIZE)]

def drawBoard():
    os.system('cls')
    for col in BOARD:
        for row in col:
            print( row.color, end = "")
            # print('(%d,%d)' % (row.x, row.y), end = "")   # prints as co-ordinate system
        print('\n')
    # input('Press Enter..')

def drawNumberedBoard():
    os.system('cls')
    for col in BOARD:
        for row in col:
            print( row.getStep(), end = "")
        print('\n')

def getMinAccessible(availableMoves : list):
    moves = []
    minChild = []
    minAccessible = None
    minLen = 8
    for eachCell in availableMoves:     # each is an obj of Board
        moves = getValidMoves(eachCell)
        if moves != None:
            print('moves from',(eachCell.x,eachCell.y), end=': ')
            for each in moves:
                print((each.x,each.y), end = ' ')
            print()

            if len(moves) <= minLen:
                minChild = moves
                minLen = len(minChild)
                minAccessible = eachCell

    # print('\nminChild: ', end='')
    # for each in minChild:
    #     print((each.x,each.y), end = ' ')
    # print()

    if minAccessible:
        print( "\nminAccessible: ",(minAccessible.x,minAccessible.y))
        return minAccessible
    else:
        return None

def explore(cell : Board):
    global STEP

    #set the current cell as knight's position, set traversed and give the current cell a step number
    cell.setKnight()
    # input('Press Enter..')
    time.sleep(0.3)
    drawBoard()

    availableMoves = getValidMoves(cell)
    if availableMoves == None:  #stop exploring if no more moves to make
        print("NO MORE MOVES!")
        return None

    elif len(availableMoves) == 1:  # condition when only one move is available
        print("AVAILABLE MOVE:", end = '')
        for each in availableMoves:
            print((each.x,each.y), end = ' ')
        print()

        explore(availableMoves[0])

    elif len(availableMoves) > 1:   # condition when more than one moves are available
        print("AVAILABLE MOVES:", end = '')
        for each in availableMoves:
            print((each.x,each.y), end = ' ')
        print()

        next = getMinAccessible(availableMoves)
        if next != None: 
            print("next move: ",(next.x,next.y))
            explore(next)
        else:
            print("no more childs!")
            explore(availableMoves[0])
            return None

def getValidMoves(cell : Board):


    # adjusting the cell co-ordinates to take the offset into account
    x = cell.x 
    y = cell.y 

    validMoves = [
    (x-1, y-2),
    (x-2, y-1),
    (x-2, y+1),
    (x-1, y+2),
    (x+1, y+2),
    (x+2, y+1),
    (x+2, y-1),
    (x+1, y-2)
    ]
    # print('VALID MOVES: ', validMoves)

    availableMoves = []
    for i in range(0, SIZE):
        for j in range(0, SIZE):
            if (i,j) in validMoves:
                if not BOARD[i][j].isTraversed():
                    availableMoves.append(BOARD[i][j])

    # print('availableMoves:')
    # for each in availableMoves:
    #     print(' (',each.x,',',each.y,')', end = '')
    # print()
    
    if len(availableMoves) > 0:
        return availableMoves
    else:
        return None
     

def main():

    x = int(input("Enter startX :")) - 1
    y = int(input("Enter startY :")) - 1

    explore(BOARD[x][y])
    input('Press ENTER to see final output...')
    drawNumberedBoard()

if __name__ == '__main__':
    main()