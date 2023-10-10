import game_data as gd
import art
import random
from replit import clear

def random_number():
  return random.randint(0,len(gd.data)-1)

def compare(a,b):
  print(f"Compare A: {gd.data[a]['name']}, {gd.data[a]['description']} from {gd.data[a]['country']}")
  print(art.vs)
  print(f"Against B: {gd.data[b]['name']}, {gd.data[b]['description']} from {gd.data[b]['country']}")
  if(gd.data[a]['follower_count']>gd.data[b]['follower_count']):
    return 'a'
  else:
    return 'b'
 
def game():
  print(art.logo)
  game_on=True
  score=0
  a=random_number()
  while(game_on):
    b=random_number()
    result=compare(a,b)
    player_choice=input("Who has more followers? Type 'a' or 'b': ").lower()
    clear()
    print(art.logo)
    if(player_choice==result):
      score+=1
      if(result=='b'):
        a=b 
      print(f"You're right! current score: {score}")
    else:
      game_on=False
      print(f"Sorry that's wrong. Your final score: {score}")
game()