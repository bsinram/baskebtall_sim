# Pass players over to the scoreboard file. Reference the players there, then bring back to the main file
import random
import requests
import time

from basketball_bananza.player import Player
from basketball_bananza.situationScoring import situationScore
from basketball_bananza.gameplay_functions import outcome, possession
from basketball_bananza.commentary import returnWinner
from basketball_bananza.game import Game
from basketball_bananza.scoreboard import Scoreboard

if __name__ == '__main__':

  # Set self.human to "False" for both players to simulate
  p1 = Player("LeBron James", True, False, 65, 90, 20, 10)
  p2 = Player("Michael Jordan", False, False, 60, 90, 15, 20)
  p3 = Player("Kobe Bryant", False, False, 60, 90, 15, 20)


  g = Game(p1, p2)
  g.run_game()