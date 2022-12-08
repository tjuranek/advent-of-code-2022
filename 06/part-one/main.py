buffer = open('input.txt').readline()

def areStringCharsUnique(string: str) -> bool:
  for index in range(0, len(string)):
    if string.count(string[index]) > 1:
      return False

  return True

for charIndex in range(0, len(buffer) - 3):
  marker = buffer[charIndex: charIndex + 4]

  if areStringCharsUnique(marker):
    print(charIndex + 4)
    break;