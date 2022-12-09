lines = open('input.txt').readlines()
grid = list(map(lambda line: list(map(lambda value: int(value), line.strip())), lines))

ROW_EDGES = [0, len(lines[0].strip()) - 1]
COLUMN_EDGES = [0, len(lines) - 1]

def getTreesInColumn(rowIndex, columnIndex) -> list[list[int]]:
  treesAbove = []
  treesBelow = []

  for index, gridRow in enumerate(grid):
    currentTree = gridRow[columnIndex]

    if index < rowIndex:
      treesAbove.append(currentTree)

    if index > rowIndex:
      treesBelow.append(currentTree)

  return [treesAbove, treesBelow]

def getTreesInRow(rowIndex, columnIndex) -> list[list[int]]:
  treesToLeft = grid[rowIndex][: columnIndex]
  treesToRight = grid[rowIndex][columnIndex + 1 :]

  return [treesToLeft, treesToRight]

def isTreeVisible(rowIndex: int, columnIndex: int) -> bool:
  if rowIndex in ROW_EDGES or columnIndex in COLUMN_EDGES:
    return True 

  treesAbove, treesBelow = getTreesInColumn(rowIndex, columnIndex)
  treesLeft, treesRight = getTreesInRow(rowIndex, columnIndex) 
  currentTree = grid[rowIndex][columnIndex]

  visibleFromAbove = max(treesAbove, default = 0) < currentTree
  visibleFromBelow = max(treesBelow, default = 0) < currentTree
  visibleFromLeft = max(treesLeft, default = 0) < currentTree
  visibleFromRight = max(treesRight, default = 0) < currentTree

  return visibleFromAbove or visibleFromBelow or visibleFromLeft or visibleFromRight

visibleTreesCount = 0

for rowIndex, gridRow in enumerate(grid):
  for columnIndex, gridRowColumn in enumerate(gridRow):
    if isTreeVisible(rowIndex, columnIndex):
      visibleTreesCount += 1

print(visibleTreesCount)