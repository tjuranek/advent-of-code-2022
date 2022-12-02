input = open("input.txt")
lines = input.readlines()

maxCalories = 0
currentElfCalories = 0

for line in lines:
  if line == "\n":
    if currentElfCalories > maxCalories:
      print(f'current: {currentElfCalories}, max: {maxCalories}')
      maxCalories = currentElfCalories
    
    currentElfCalories = 0

  else:
    currentElfCalories = currentElfCalories + int(line)

print(maxCalories)




  
    



