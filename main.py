import sys

boardSize = int(sys.argv[1])

# each cell has 8 possible neighbors
def getAdjacents(row, col) : 
  return [
    [row - 1, col], # N
    [row + 1, col], # S
    [row, col + 1], # E
    [row, col - 1], # W
    [row - 1, col + 1], # N.E
    [row - 1, col - 1], # N.W
    [row + 1, col + 1], # S.E
    [row + 1, col - 1], # S.W
  ]

def readConfigurationData(boardSize):
  rowConfiguration = []
  for i in range(boardSize):
    arr = sys.argv[2 + i].split(',')
    for idx, value in enumerate(arr):
      if value == 'true' or value == 'True':
        arr[idx] = True
      else:
        arr[idx] = False
    rowConfiguration.append(arr)
  return rowConfiguration

rowConfiguration = readConfigurationData(boardSize)

initialBoard = [ [ 0 for i in range(boardSize) ] for j in range(boardSize) ]
board = []

for rowIdx, row in enumerate(rowConfiguration):
  for colIdx, value in enumerate(row):
    if value:
      adjacents = getAdjacents(rowIdx, colIdx)
      for i in range(len(adjacents)):
        if adjacents[i][0] >= 0 and adjacents[i][1] >= 0 and adjacents[i][0] < len(rowConfiguration) and adjacents[i][1] < len(rowConfiguration[rowIdx]):
          initialBoard[adjacents[i][0]][adjacents[i][1]] += 1
          
#No delete
def showInitialBoard(initialBoard, boardSize):
  result = ""
  for i in range(boardSize):
    result = result + "["
    for j in range(boardSize):
      result = result + str(initialBoard[i][j])
      if j < boardSize - 1:
        result = result + ","
    result = result + "]"
    if (i < boardSize - 1):
      result = result + ","
  print("\nThe Minesweeper configuration is:", result)

showInitialBoard(initialBoard, boardSize);