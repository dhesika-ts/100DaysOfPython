from art import logo
from replit import clear
def add(a,b):
  return a+b
def subtract(a,b):
  return a-b
def multiply(a,b):
  return a*b
def divide(a,b):
  return a/b
calc_dict={
  "+":add,
  "-":subtract,
  "*":multiply,
  "/":divide
}
def calculator():
  print(logo)
  a=float(input("What's your first number: "))
  for symbol in calc_dict:
    print(symbol)
  to_continue='y'
  while(to_continue=='y'):
    operation=input("Pick an operation: ")
    b=float(input("What's your next number: "))
    answer=calc_dict[operation](a,b)
    print(f"{a} {symbol} {b} = {answer}")
    to_continue=input(f"Do you want to continue calculation with {answer}? Type 'y' for YES or 'n' for NO: ")
    if(to_continue=='y'):
      a=answer
    else:
      print("Gud bye!")
      clear()
      calculator()
calculator()