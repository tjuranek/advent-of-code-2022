program = open('input.txt').readlines()

cycleValues = [1]

cycleCount = 0
cycleValue = 1
cycleStrengths = {}

for line in program:
  command = line.strip().split(' ')

  cycleCount += 1
  print(cycleCount, cycleValue, command[0])
  cycleStrengths[cycleCount] = cycleCount * cycleValue

  if command[0] == 'noop': continue

  cycleCount += 1
  cycleStrengths[cycleCount] = cycleCount * cycleValue
  print(cycleCount, cycleValue)
  cycleValue += int(command[1])


sum = 0
for index in [20, 60, 100, 140, 180, 220]:
  print(cycleStrengths[index])
  sum += cycleStrengths[index]

print(sum)
