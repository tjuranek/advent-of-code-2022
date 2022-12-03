from enum import Enum

class Move(Enum):
  A = 'ROCK'
  B = 'PAPER'
  C = 'SCISSORS'

class Strategy(Enum): 
  X = 'LOST'
  Y = 'DRAW'
  Z = 'WON'

class MapOpponentMoveToMyStrategy(Enum): 
  A = {
    Strategy.X: Move.C,
    Strategy.Y: Move.A,
    Strategy.Z: Move.B
  }
  B = {
    Strategy.X: Move.A,
    Strategy.Y: Move.B,
    Strategy.Z: Move.C
  }
  C = {
    Strategy.X: Move.B,
    Strategy.Y: Move.C,
    Strategy.Z: Move.A
  }

class MovePoints(Enum):
  ROCK = 1
  PAPER = 2
  SCISSORS = 3

class RoundPoints(Enum):
  Lost = 0
  Draw = 3
  Won = 6

def getMoveForStrategy(myStrategy: Strategy, opponentMove: Move) -> Move: 
  return MapOpponentMoveToMyStrategy[opponentMove.name].value[myStrategy];

def getMovePoints(move: Move) -> int:
  return MovePoints[move.value].value;

def getOutcomePoints(myMove: Move, opponentMove: Move) -> int:
  if myMove.value == opponentMove.value:
    return RoundPoints.Draw.value

  if myMove.value == "ROCK" and opponentMove.value == "SCISSORS":
    return RoundPoints.Won.value

  if myMove.value == "SCISSORS" and opponentMove.value == "PAPER":
    return RoundPoints.Won.value
  
  if myMove.value == "PAPER" and opponentMove.value == "ROCK":
    return RoundPoints.Won.value

  return RoundPoints.Lost.value

def getRoundPoints(myStrategy: Strategy, opponentMove: Move) -> int:
  myMove = getMoveForStrategy(myStrategy, opponentMove);
  return getMovePoints(myMove) + getOutcomePoints(myMove, opponentMove)

input = open("input.txt")
lines = input.readlines()

totalScore = 0

for line in lines:
  opponentValue, myValue = line.split()
  totalScore += getRoundPoints(Strategy[myValue], Move[opponentValue])

print(totalScore)