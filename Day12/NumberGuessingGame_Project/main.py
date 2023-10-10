import art
print(art.logo)
import random
EASY_LEVEL_TURNS=10
HARD_LEVEL_TURNS=5
def game():
  number=random.randint(1,100)
  print("Welcome to NumberGuessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  level=input("Which level do you wanna play? Type 'easy' or 'hard'? :").lower()
  if(level=="easy"):
    turns=EASY_LEVEL_TURNS
  elif(level=="hard"):
    turns=HARD_LEVEL_TURNS
  guessed =False
  while(turns!=0 and guessed==False):
    print(f"You have {turns} attempts to guess a number.")
    guess=int(input("Guess a number: "))
    if(guess==number):
      guessed=True
      print(f"You got it! The number was {guess}.")
    elif(guess>number):
      turns-=1
      print("Your guess is too high")
    elif(guess<number):
      turns-=1
      print("Your guess is too low.")
    if(guessed!=True and turns!=0):
      print("Guess Again.")
  if(turns==0):
    print("You've run out of guesses, lost the game!")
  play_again=input("Wanna play again? Type 'y' or 'n': ")
  if(play_again=='y'):
    game()
  else:
    print("Gudbye!")
  
game()
