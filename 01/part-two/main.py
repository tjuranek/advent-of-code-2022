input = open("input.txt")
lines = input.readlines()

currentElfCalories = 0
caloriesPerElf = []

for line in lines:
  if line == "\n":
    caloriesPerElf.append(currentElfCalories)
    currentElfCalories = 0
  else:
    currentElfCalories += int(line)

caloriesPerElf.sort(reverse=True)

print(caloriesPerElf[0] + caloriesPerElf[1] + caloriesPerElf[2])