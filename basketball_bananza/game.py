import requests
import time

from basketball_bananza.gameplay_functions import possession
from basketball_bananza.commentary import returnWinner

class Game:
    def __init__ (self, p1, p2):
      self.p1 = p1
      self.p2 = p2

    def run_game(self):

      # Gameplay loop
      while self.p1.score < 10 and self.p2.score < 10:
        if self.p1.onOffense:
          possession(self.p1, self.p2)
        else: 
          possession(self.p2, self.p1)  
        print("The score is now", self.p1.name, self.p1.score,",", self.p2.name, self.p2.score)
        self.p1.onOffense = not self.p1.onOffense
        self.p2.onOffense = not self.p2.onOffense
        time.sleep(1)


      if (self.p2.score > self.p1.score):
        print(returnWinner(self.p2.name, self.p2.score, self.p1.name, self.p1.score))
      elif(self.p2.score < self.p1.score):
        print(returnWinner(self.p1.name, self.p1.score, self.p2.name, self.p2.score))

      previousGames = requests.get("https://api.steinhq.com/v1/storages/5e891312b88d3d04ae081681/Sheet1").json()  
      print(requests.post("https://api.steinhq.com/v1/storages/5e891312b88d3d04ae081681/Sheet1",json=[{"Game #": len(previousGames)+1, "P1 Score": self.p1.score, "P2 Score": self.p2.score}]).json())