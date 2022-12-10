from enum import Enum

class Direction(Enum):
  UP = 'U'
  DOWN = 'D'
  LEFT = 'L'
  RIGHT = 'R'

class Node:
  def __init__(self):
    self.x = 0
    self.y = 0
    self.history = [(0, 0)]

  def isAdjacent(self, node: 'Node'):
    xDifferential = abs(self.x - node.x)
    yDifferential = abs(self.y - node.y)

    return xDifferential <= 1 and yDifferential <= 1

  def lead(self, direction: Direction):
    if direction == Direction.UP:
      self.y += 1 

    if direction == Direction.DOWN:
      self.y -= 1 

    if direction == Direction.LEFT:
      self.x -= 1 

    if direction == Direction.RIGHT:
      self.x += 1 

    self.history.append((self.x, self.y))

  def follow(self, node: 'Node'):
    if self.isAdjacent(node):
      return

    nextPosition = node.history[len(node.history) - 2]

    self.x = nextPosition[0]
    self.y = nextPosition[1]
    self.history.append((self.x, self.y))

def main():
  head = Node()
  tail = Node()
  commands = open('input.txt').readlines()

  for command in commands:
    move, quantity = command.strip().split(' ')
    direction = Direction(move)

    for _ in range(0, int(quantity)):
      head.lead(direction)
      tail.follow(head)

  uniqueTailHistory = set(tail.history)
  print(len(uniqueTailHistory))

main()
