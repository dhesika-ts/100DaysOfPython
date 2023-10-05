from replit import clear
from art import logo
print(logo)
print("Welcome to  Silent Auction Program!")
bids={}
bidders_left="yes"
while(bidders_left=="yes"):
  person_name=input("What is your name?: ")
  bid_amount=int(input("What is your bid?: $"))
  bidders_left=input('Are there any bidder left? Type "yes" or "no": ').lower()
  bids[person_name]=bid_amount
  #clear()
  
def find_highest_bid(bids):
  highest_bid=0
  winner=""
  for bidder in bids:
    if(bids[bidder]>highest_bid):
      highest_bid=bids[bidder]
      winner=bidder
  print(f"The winner is '{winner}' and the bid amount is ${highest_bid}")
  
find_highest_bid(bids)

