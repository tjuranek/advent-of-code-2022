from enum import Enum

class OpponentPlay(Enum):
  A = 'ROCK'
  B = 'PAPER'
  C = 'SCISSORS'

class MyPlay(Enum):
  X = 'ROCK'
  Y = 'PAPER'
  Z = 'SCISSORS'

class ShapePoints(Enum):
  ROCK = 1
  PAPER = 2
  SCISSORS = 3

class RoundPoints(Enum):
  Lost = 0
  Draw = 3
  Won = 6

def getShapePoints(myPlay: MyPlay) -> int:
  return ShapePoints[myPlay.value].value;

def getOutcomePoints(myPlay: MyPlay, opponentPlay: OpponentPlay) -> int:
  if myPlay.value == opponentPlay.value:
    return RoundPoints.Draw.value

  if myPlay.value == "ROCK" and opponentPlay.value == "SCISSORS":
    return RoundPoints.Won.value

  if myPlay.value == "SCISSORS" and opponentPlay.value == "PAPER":
    return RoundPoints.Won.value
  
  if myPlay.value == "PAPER" and opponentPlay.value == "ROCK":
    return RoundPoints.Won.value

  return RoundPoints.Lost.value

def getRoundPoints(myPlay: MyPlay, opponentPlay: OpponentPlay) -> int:
  return getShapePoints(myPlay) + getOutcomePoints(myPlay, opponentPlay)

input = open("input.txt")
lines = input.readlines()

totalScore = 0

for line in lines:
  opponentValue, myValue = line.split()

  opponentPlay = OpponentPlay[opponentValue]
  myPlay = MyPlay[myValue] 

  totalScore += getRoundPoints(myPlay, opponentPlay)

print(totalScore)