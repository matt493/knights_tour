import time
import os

SIZE = 0
STEP = 0
AUTO = True
DEBUG = False

os.system('cls')

while SIZE <= 0: SIZE = int(input("Enter SIZE for the board (SIZE > 0): "))     #reading a +ve int as board size

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
        if DEBUG: print("Next Step:",self.step)
        self.color = Board.empty.format(Board.horse)

    def isTraversed(self):
        return self.is_traversed
    pass

BOARD = [[ Board(j,i) for i in range(1, SIZE+1) ] for j in range(1, SIZE+1)]    # matrix co-ordinates range from 1 .. SIZE + 1 ie: offset by 1 just for readability
# BOARD = [[ Board(j,i) for i in range(SIZE) ] for j in range(SIZE)]

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
            if DEBUG:
                print('moves from',(eachCell.x,eachCell.y), end=': ')
                for each in moves:
                    print((each.x,each.y), end = ' ')
                print()

            if len(moves) <= minLen:
                minChild = moves
                minLen = len(minChild)
                minAccessible = eachCell

    if minAccessible:
        if DEBUG: print( "\nminAccessible: ",(minAccessible.x,minAccessible.y))
        return minAccessible
    else:
        return None

def explore(cell : Board):
    global STEP

    #set the current cell as knight's position, set traversed and give the current cell a step number
    cell.setKnight()
    
    if AUTO:
        time.sleep(0.3)
    else:
        input('Press [ENTER]')
    drawBoard()

    availableMoves = getValidMoves(cell)
    if availableMoves == None:  #stop exploring if no more moves to make
        if DEBUG: print("NO MORE MOVES!")
        return None

    elif len(availableMoves) == 1:  # condition when only one move is available
        if DEBUG: 
            print("AVAILABLE MOVE:", end = '')
            for each in availableMoves:
                print((each.x,each.y), end = ' ')
            print()

        explore(availableMoves[0])  # explore the new cell

    elif len(availableMoves) > 1:   # condition when more than one moves are available

        if DEBUG: 
            print("AVAILABLE MOVES:", end = '')
            for each in availableMoves:
                print((each.x,each.y), end = ' ')
            print()

        next = getMinAccessible(availableMoves) # find the min accessible cell from available valid moves
        if next: 
            if DEBUG: print("next move: ",(next.x,next.y))
            explore(next)   # exploring the next min accessible cell in the board
        else:
            explore(availableMoves[0])  # exploring the very last cell in the board, nowhere else to go other than the last available move
            return None

def getValidMoves(cell : Board):


# adjusting the cell co-ordinates to take the offset into account
    x = cell.x - 1
    y = cell.y - 1

# list of all the valid moves a knight can make
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

    availableMoves = []
    for i in range(0, SIZE):
        for j in range(0, SIZE):
            if (i,j) in validMoves:
                if not BOARD[i][j].isTraversed():
                    availableMoves.append(BOARD[i][j])
    
    if len(availableMoves) > 0:
        return availableMoves
    else:
        return None
     

def main():
    x = y = 0
# checking x and y is a valid input
    while (x < 1) or (x > SIZE): x = int(input("Enter startX :"))
    while (y < 1) or (y > SIZE): y = int(input("Enter startY :"))

# adjusting offset
    x = x - 1
    y = y - 1

# starting recursive exploration 
    explore(BOARD[x][y])
    input('Press [ENTER] to see final output...')
    drawNumberedBoard()

if __name__ == '__main__':
    main()