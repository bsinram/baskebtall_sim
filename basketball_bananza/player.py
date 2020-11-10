class Player:
  def __init__ (self, name, onOffense, human, fieldGoal, dunk, block, steal):
    self.name = name
    self.score = 0
    self.onOffense = onOffense
    self.human = human
    self.fieldGoal = fieldGoal
    self.dunk = dunk
    self.block = block
    self.steal = steal