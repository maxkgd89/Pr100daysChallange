import random

cards = []
playerlist = []
computerlist = []

#initialise set of cards
def setnewcardset():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#player and computer score
def setnewscore():  
  playerlist = []
  computerlist = []

#update player's score, remove card from deck
def player_scoreupdate():
  playercard = random.choice(cards)
  playerlist.append(playercard)
  cards.remove(playercard)
  print(f"player's score is {set_eval(playerlist)}")

#update comp's score, remove card from deck
def comp_scoreupdate():
  playercard = random.choice(cards)
  computerlist.append(playercard)
  cards.remove(playercard)
  print(f"computer's score is {set_eval(computerlist)}")

#score evaluation
def set_eval(list):
  Pscore = 0
  for X in range(0,len(list)):
    Pscore = Pscore + list[X]
  return Pscore

def play_game():

  while True:
    if set_eval(playerlist) == 21:
      print("player win")
      break
    elif set_eval(playerlist) > 21:
      print("player lose")
      break
    elif set_eval(computerlist) == 21:
      print("player lose")
      break
    elif set_eval(computerlist) > 21:
      print("player win")
      break
    else:
      print("keep playing")
      player_scoreupdate()
      comp_scoreupdate()

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  #clear()
  play_game()

