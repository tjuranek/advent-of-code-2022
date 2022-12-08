import functools

CHANGE_DIRECTORY_DELIMITER = 'cd'
COMMAND_DELIMITER = '$'
DIRECTORY_DELIMITER = 'dir'
LIST_DELIMITER = 'ls'
ROOT_DIR_DELIMITER = '/'

class File:
  def __init__(self, name: str, size: int):
    self.name = name
    self.size = size 

class Directory:
  def __init__(self, name: str, parentDirectory: 'Directory'):
    self.files = []
    self.name = name
    self.parentDirectory = parentDirectory
    self.subDirectories = []

  def addSubDirectoryIfNotExists(self, directory: 'Directory'):
    directoryNames = map(lambda d: d.name, self.subDirectories)

    if (directory.name in directoryNames):
      return

    self.subDirectories.append(directory)

  def addFileIfNotExists(self, file: File):
    fileNames = map(lambda f: f.name, self.files)

    if (file.name in fileNames):
      return

    self.files.append(file)

  def getSize(self) -> int:
    sumOfDirectorySizes = functools.reduce(lambda prev, next: prev + next.getSize(), self.subDirectories, 0)
    sumOfFileSizes = functools.reduce(lambda prev, next: prev + next.size, self.files, 0)

    return sumOfDirectorySizes + sumOfFileSizes

  def getSubDirectory(self, directoryName: str) -> 'Directory':
    return next(subDirectory for subDirectory in self.subDirectories if subDirectory.name == directoryName)

def isCommand(line: str) -> bool:
  return line.split(' ')[0] == COMMAND_DELIMITER

def isDirectory(line: str) -> bool:
  return line.split(' ')[0] == DIRECTORY_DELIMITER

def isFile(line: str) -> bool:
  return isDirectory(line) == False

def parseCommand(line: str) -> list[str]:
  delimiter, command, argument =  (line.split(' ') + [None])[:3]
  return [command, argument]

def parseDirectoryName(line: str) -> str:
  return line.split(' ')[1]

def parseFile(line: str) -> list[str]:
 return line.split(' ') 

def buildFileTree(terminalOutput: list[str]):
  rootDirectory = Directory('/', None)
  pointer = rootDirectory

  for line in terminalOutput:
    line = line.strip()

    if isCommand(line):
      command, argument = parseCommand(line)

      if command == LIST_DELIMITER:
        continue

      if command == CHANGE_DIRECTORY_DELIMITER:
        match argument:
          case '/':
            pointer = rootDirectory
          case '..':
            pointer = pointer.parentDirectory
          case _:
            pointer = pointer.getSubDirectory(argument)

      continue

    if (isDirectory(line)):
      directoryName = parseDirectoryName(line)
      pointer.addSubDirectoryIfNotExists(Directory(directoryName, pointer))
      continue

    if (isFile(line)):
      size, name = parseFile(line)
      pointer.addFileIfNotExists(File(name, int(size)))
      continue

  return rootDirectory

def getFileTreeDirectorySizes(rootDirectory: Directory):
  sizes = [rootDirectory.getSize()]

  for subDirectory in rootDirectory.subDirectories:
    sizes = sizes + getFileTreeDirectorySizes(subDirectory)

  return sizes

rootDirectory = buildFileTree(open('input.txt').readlines())
directorySizes = getFileTreeDirectorySizes(rootDirectory)
print(functools.reduce(lambda prev, next: prev + next if next <= 100000 else prev, directorySizes, 0))
