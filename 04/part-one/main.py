input = open("input.txt")
lines = input.readlines()

class Pair:
  def __init__(self, input: str):
    lowerInputStr, higherInputStr = input.split('-')

    self.lowerLimit = int(lowerInputStr)
    self.higherLimit = int(higherInputStr)

  def containsPair(self, pair: 'Pair') -> bool:
    return self.lowerLimit <= pair.lowerLimit and self.higherLimit >= pair.higherLimit

pairFullyContainsAnotherCounter = 0

for line in lines:
  pairOne, pairTwo = map(lambda i: Pair(i), line.split(','));

  if (pairOne.containsPair(pairTwo) or pairTwo.containsPair(pairOne)):
    pairFullyContainsAnotherCounter += 1

print(pairFullyContainsAnotherCounter)