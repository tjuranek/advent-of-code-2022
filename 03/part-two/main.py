def getItemPriority(item: chr) -> int:
  return ord(item) - (38 if item.isupper() else 96)

def getGroupsOfThreeRucksacks(rucksacks: list[str]) -> list[list[str]]:
  groups = []
  
  for index in range(0, len(rucksacks), 3):
    groups.append(rucksacks[index : index + 3])
    
  return groups

input = open("input.txt")
rucksacks = input.readlines()

sumOfRucksackGroupPriorities = 0

for rucksackGroup in getGroupsOfThreeRucksacks(rucksacks):
  rucksackOne, rucksackTwo, rucksackThree = rucksackGroup

  for item in rucksackOne:
    if item in rucksackTwo and item in rucksackThree:
      sumOfRucksackGroupPriorities += getItemPriority(item);
      break;

print(sumOfRucksackGroupPriorities)
