import random
import dataset_14_00 as ds

score = 0
game_should_continue = True
account_B = random.choice(ds.data)

#format account data into printable format
def format_data(account):
  account_name = account['name']
  account_age = account['age']
  account_rating = account['rating']
  return f"name {account_name},age {account_age},rating {account_rating}"

def check_answer(guess, a_followers, b_followers):
  """Takes the user guess and follower counts and returns if they got it right."""
  if a_followers > b_followers:
      return guess == "a"
  else:
      return guess == "b"

while game_should_continue: 
  #generate a random account from the game data
  account_A=account_B
  account_B=random.choice(ds.data)
  while account_A == account_B:
    account_B=random.choice(ds.data)

  #print the account data for comparison
  print(f"Compare A: {format_data(account_A)}")
  print("VS")
  print(f"Against B: {format_data(account_B)}")

  #Ask user for a guess
  guess = input("Who has more followers? Type 'A' or 'B': ").lower()

  #check if user is correct
  #Get follower count of each account
  account_A_follower_count = account_A['follower_count']
  account_B_follower_count = account_B['follower_count']
  is_correct =check_answer(
    guess,account_A_follower_count,account_B_follower_count)

  #sets right reply as account_A
  if account_A_follower_count > account_B_follower_count:
    account_A = account_A
  else :
    account_A = account_B

  #Give user feedback on their guess
  if is_correct:
    score += 1
    print(f"You got it right! and your score is {score}")
    input("press button to continue")

  else:
    print(f"Sorry, that's wrong and your score is {score}")
    continue_choice = input("Do you want to continue? Type 'y' or 'n': ").lower()
    if continue_choice == 'n':
        game_should_continue = False
        print("Game Over")
    score=0
