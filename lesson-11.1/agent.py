'''
Rock-Paper-Scissors game
Starter code for Stanford CME 193
author: Sven Schmit
'''

import random


class Agent:
  def getMove(self, moves_other, moves_self):
    pass


class InstructorAgent(Agent):
  def __init__(self):
    p_rock = random.random()
    p_scissors = random.random()
    p_paper = random.random()
    p_total = p_rock + p_scissors + p_paper

    self.p_rock = p_rock / p_total
    self.p_scissors = self.p_rock + p_scissors / p_total

  def getMove(self, moves_other, moves_self):
    random_move = random.random()
    if random_move < self.p_rock:
      return 'r'
    elif random_move < self.p_scissors:
      return 's'
    else:
      return 'p'


class MyAgent(Agent):
  def getMove(self, moves_other, moves_self):
    def __init__(self):
      p_rock = 100
      p_scissors = random.random()
      p_paper = 20
      p_total = p_rock + p_scissors + p_paper

      self.p_rock = p_rock / p_total
      self.p_scissors = p_rock + p_scissors / p_total
    random_move = random.random()
    if random_move < self.p_rock and moves_other[0] != 'r':
      return 'r'
    elif random_move < self.p_scissors and moves_self[len(moves_self) - 1] != 'p':
      return 's'
    else:
      return 'p'


class HumanAgent(Agent):
  def getMove(self, moves_other, moves_self):
    step = ''
    while step != 'r' and step != 'p' and step != 's':
      step = input('What is your next move? Please enter one letter: \nr for ROCK\ns for SCISSORS\np for PAPER\n=>')
    return step
