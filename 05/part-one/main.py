input = open("input.txt")
lines = input.readlines()

def parseStacksFromInput(inputLines: list[str]) -> list[list[str]]:
  stacksBottomLineIndex = inputLines.index('\n') - 2;
  rows = []

  for lineIndex, line in enumerate(inputLines[0: stacksBottomLineIndex + 1]):
    rows.append([]);

    for charIndex in range(1, len(line), 4):
      rows[lineIndex].append(line[charIndex])

  # messy, but converts rows to columns and then filters whitespace values
  uncleanColumns = list(map(lambda column: list(column), zip(*reversed(rows))));
  cleanColumns = list(map(lambda column: list(filter(lambda columnValue: columnValue != ' ', column)), uncleanColumns))

  return cleanColumns

def parseMovesFromInput(inputLines: list[str]):
  movesStartLineIndex = inputLines.index('\n') + 1;
  moves = []

  for line in inputLines[movesStartLineIndex:]:
    words = line.strip().split(' ')
    moves.append((int(words[1]), int(words[3]), int(words[5])))

  return moves

stacks = parseStacksFromInput(lines)

for move in parseMovesFromInput(lines):
  quantity, fromStack, toStack = move

  for operation in range(0, quantity):
    stacks[toStack - 1].append(stacks[fromStack - 1].pop(-1))


answer = ""

for stack in stacks:
  answer += stack.pop(-1)

print(answer)





