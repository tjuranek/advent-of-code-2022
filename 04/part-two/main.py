input = open("input.txt")
lines = input.readlines()

class Pair:
  def __init__(self, input: str):
    lowerInputStr, higherInputStr = input.split('-')

    self.values = range(int(lowerInputStr), int(higherInputStr) + 1)

  def hasOverlapWith(self, pair: 'Pair') -> bool:
    return set(self.values).intersection(pair.values)

pairFullyContainsAnotherCounter = 0

for line in lines:
  pairOne, pairTwo = map(lambda i: Pair(i), line.split(','));

  if (pairOne.hasOverlapWith(pairTwo)):
      pairFullyContainsAnotherCounter += 1

print(pairFullyContainsAnotherCounter)