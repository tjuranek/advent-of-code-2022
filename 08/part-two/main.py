lines = open('input.txt').readlines()
grid = list(map(lambda line: list(map(lambda value: int(value), line.strip())), lines))

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

def getScenicScoreForDirection(trees: list[int], currentTree: int):
  score = 0

  for tree in trees:
    score += 1

    if tree >= currentTree:
      break

  return score

def getScenicScore(rowIndex: int, columnIndex: int) -> bool:
  treesAbove, treesBelow = getTreesInColumn(rowIndex, columnIndex)
  treesLeft, treesRight = getTreesInRow(rowIndex, columnIndex) 
  currentTree = grid[rowIndex][columnIndex]

  treesAbove.reverse()
  treesLeft.reverse()

  aboveScore = getScenicScoreForDirection(treesAbove, currentTree)
  belowScore = getScenicScoreForDirection(treesBelow, currentTree)
  leftScore = getScenicScoreForDirection(treesLeft, currentTree)
  rightScore = getScenicScoreForDirection(treesRight, currentTree)

  return aboveScore * belowScore * leftScore * rightScore

highestScenicScore = 0

for rowIndex, gridRow in enumerate(grid):
  for columnIndex, gridRowColumn in enumerate(gridRow):
    scenicScore = getScenicScore(rowIndex, columnIndex)

    if scenicScore > highestScenicScore:
      highestScenicScore = scenicScore

print(highestScenicScore)