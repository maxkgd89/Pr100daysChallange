#choosing random number between 1 and 100
import random
RN=random.randint(1, 100)

#function to set difficulty
playerturns=0
def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    global playerturns
    playerturns=10
    return playerturns
  elif level == "hard":
    playerturns=5
    return playerturns
  else:
    print("You have not chosen a valid difficulty. Please try again.")

set_difficulty()
print(f" playerturns ={playerturns}")

#function to check user's guess against actual answer. Print "Too high." or "Too low." or "You got it!"
def check_answer(guess):
  if guess > RN:
    print("Too high.")
  elif guess < RN:
    print("Too low.")
  elif guess == RN:
    print(f"You got it! The answer was {RN}.")

#let user guess number
while True:
  guess = int(input("Make a guess: "))
  check_answer(guess)
  print(f" playerturns remaining - {playerturns} ")
  playerturns -= 1
  if playerturns == 0:
    print("You've run out of guesses, you lose.")
    break

print('lets play again')
set_difficulty()
print(f" playerturns ={playerturns}")

while True:
      guess = int(input("Make a guess: "))
      check_answer(guess)
      print(f" playerturns remaining - {playerturns} ")
      playerturns -= 1
      if playerturns == 0:
        print("You've run out of guesses, you lose.")
        break
