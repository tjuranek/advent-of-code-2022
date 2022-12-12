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
    self.next = None

  def recordHistory(self):
    self.history.append((self.x, self.y)) 

  def lead(self, direction: Direction):
    if direction == Direction.UP:
      self.y += 1 

    if direction == Direction.DOWN:
      self.y -= 1 

    if direction == Direction.LEFT:
      self.x -= 1 

    if direction == Direction.RIGHT:
      self.x += 1 

    self.recordHistory()

  def follow(self, leadingNode: 'Node'):
    onlyYChanged = self.x == leadingNode.x
    onlyXChanged = self.y == leadingNode.y

    if onlyYChanged:
      yDiff = leadingNode.y - self.y

      if abs(yDiff) > 1:
        self.y += yDiff + 1 if yDiff < 0 else yDiff - 1
    elif onlyXChanged:
      xDiff = leadingNode.x - self.x

      if abs(xDiff):
        self.x += xDiff + 1 if xDiff < 0 else xDiff - 1
    else:
      xDiff = leadingNode.x - self.x
      yDiff = leadingNode.y - self.y

      if abs(xDiff) > 1 or abs(yDiff) > 1:
        if xDiff > 1: xDiff = 1
        if xDiff < -1: xDiff = -1
        if yDiff > 1: yDiff = 1
        if yDiff < -1: yDiff = -1

        self.x += xDiff
        self.y += yDiff

    self.recordHistory()

class NodeList: 
  def __init__(self):
    self.head = None
    self.tail = None
    self.length = 0

  def populate(self, length: int):
    for _ in range(0, length):
      self.push(Node())

  def push(self, node: 'Node'):
    if self.head == None:
      self.head = node
    else:
      self.tail.next = node

    self.tail = node
    self.length += 1

  def move(self, direction: Direction):
    index = 0
    pointer = self.head

    while pointer != None:
      if index == 0:
        pointer.lead(direction)
        pointer.next.follow(pointer)
      elif pointer.next:
        pointer.next.follow(pointer)

      index += 1
      pointer = pointer.next

nodeList = NodeList()
nodeList.populate(10)

for command in open('input.txt', 'r'):
  move, quantity = command.strip().split(' ')
  direction = Direction(move)

  for _ in range(0, int(quantity)):
    nodeList.move(direction)

print(len(set(nodeList.tail.history)))