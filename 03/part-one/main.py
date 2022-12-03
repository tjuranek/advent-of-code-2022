def getItemPriority(item: chr) -> int:
  return ord(item) - (38 if item.isupper() else 96)

def getRucksackCompartments(rucksack: str) -> list[str]:
  index = len(rucksack) // 2
  splitableRucksack = rucksack[:index] + '|' + rucksack[index:] 

  return splitableRucksack.split('|')

input = open("input.txt")
rucksacks = input.readlines()

sumOfItemPriorities = 0

for rucksack in rucksacks:
  compartmentOne, compartmentTwo = getRucksackCompartments(rucksack)

  for item in compartmentOne:
    if item in compartmentTwo:
      sumOfItemPriorities += getItemPriority(item)
      break;

print(sumOfItemPriorities)


