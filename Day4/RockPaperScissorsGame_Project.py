rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
import sys
print("Welcome to Rock Paper Scissors Game!")
choice = int(
    input(
        "What do you want to choose? Type 0 for Rock, 1 for Paper or 2 for Scissor. "
    ))
if(choice > 2 or choice < 0):
    sys.exit("Incorrect option! Play Again")
computer_choice = random.randint(0, 2)
emoji = [rock, paper, scissors]
print(
    f"Your choice:{emoji[choice]}\nComputer's choice:{emoji[computer_choice]}")
if ((choice == 0 and computer_choice == 1)
        or (computer_choice == 2 and choice == 1)
        or (computer_choice == 0 and choice == 2)):
    print("You lost the game!")
elif ((choice == 0 and computer_choice == 2)
      or (computer_choice == 1 and choice == 2)
      or (computer_choice == 0 and choice == 1)):
    print("You won!")
elif ((choice == 0 and computer_choice == 0)
      or (computer_choice == 1 and choice == 1)
      or (choice == 2 and computer_choice == 2)):
    print("Match draw")

