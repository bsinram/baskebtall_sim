import random
import time
from basketball_bananza.situationScoring import situationScore


# Outcome
def outcome (oPlayer,oPlayerAction, dPlayer, dPlayerAction):
  if oPlayerAction == 1:
    thisrand = random.randint(0,100)
    if thisrand <= (dPlayer.block * situationScore(oPlayerAction, dPlayerAction)):
      shootingSt = f"The shot is rejected by {dPlayer.name}!"
    elif thisrand <= oPlayer.fieldGoal:
      shootingSt = f"What a beautiful shot by {oPlayer.name}"
      oPlayer.score = oPlayer.score+1
    else:
      shootingSt = f"And {oPlayer.name} threw a brick" 
    print(shootingSt)
  else:
    if random.randint(0,100) <= (dPlayer.steal * situationScore(oPlayerAction, dPlayerAction)):
      dunkingSt = f"Oh! {dPlayer.name} comes up with a steal!"
    elif random.randint(0,100) <= oPlayer.dunk:
      dunkingSt = f"{oPlayer.name} throws it down with authority!"
      oPlayer.score = oPlayer.score+1
    else:
      dunkingSt = f"Oh my! {oPlayer.name} was stuffed by the rim!"
    print(dunkingSt)   


def possession(oPlayer, dPlayer):
  # Offensive choice
  if oPlayer.human:
    oPlayerAction = input("Type '1' to shoot or '2' to dunk: ")
    oPlayerAction = int(oPlayerAction)
  else:
    oPlayerAction = random.randint(1,2)
  if oPlayerAction == 1:
    oSt = f"{oPlayer.name} shoots..."
  elif oPlayerAction == 2:
    oSt = f"{oPlayer.name} drives the lane..." 
  
  # Defensive choice
  if dPlayer.human:
    dPlayerAction = input("Type '1' to block or '2' to steal: ")
    dPlayerAction = int(dPlayerAction)
  else:
    dPlayerAction = random.randint(1,2)
  if dPlayerAction == 1:
    dSt = f"{dPlayer.name} leaps to contest the shot..."
  elif dPlayerAction ==2:
    dSt = f"{dPlayer.name} swipes to steal..."
  print(oSt)
  time.sleep(1)
  print(dSt) 
  time.sleep(1)
  outcome(oPlayer, oPlayerAction, dPlayer, dPlayerAction)
  time.sleep(1)