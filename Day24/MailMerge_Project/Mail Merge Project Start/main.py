#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

PLACE_HOLDER="[name]"

with open("./Input/Names/invited_names.txt","r") as names:
    names_list=names.readlines()
with open("./Input/Letters/starting_letter.txt","r") as letter:
    letter_str=letter.read()
    for name in names_list:
        with open(f"./Output/ReadyToSend/letter_for_{name.strip()}.txt", "w") as file:
            new_letter=letter_str.replace(PLACE_HOLDER, name.strip())
            file.write(new_letter)