import asciiArt
print(asciiArt.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def ceaser(text,shift,direction):
  end_text=""
  if(shift>26):
    shift%=26
  if(direction=="decode"):
    shift*=-1
  for letter in text:  
    if(letter in alphabet):
      pos=alphabet.index(letter)
      new_pos=pos+shift
      while(new_pos>len(alphabet)):
        new_pos-=26
      end_text+=alphabet[new_pos]
    else:
      end_text+=letter
  print(f"The {direction}d text is {end_text}") 
  to_continue=input('Continue Encoding/decoding? Type "yes" or "no": ').lower()
  if(to_continue!='no'):
    direction = input("Type 'encode' to encrypt, type 'decode'to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    ceaser(text,shift,direction)

ceaser(text,shift,direction)

  




