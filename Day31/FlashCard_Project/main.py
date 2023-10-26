from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")
print(f"Records:{len(to_learn)}")


# known
def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


# flip card
def flip_card():
    english_word = current_card['English']
    canvas.itemconfig(card_title, text="English", fill='white')
    canvas.itemconfig(card_word, text=english_word, fill='white')
    canvas.itemconfig(card_img, image=card_back_img)


# next card
def next_card():
    global current_card
    global flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    french_word = current_card['French']
    canvas.itemconfig(card_title, text="French", fill='black')
    canvas.itemconfig(card_word, text=french_word, fill='black')
    canvas.itemconfig(card_img, image=card_front_img)
    flip_timer = window.after(3000, flip_card)


# ui
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

canvas = Canvas()
canvas.config(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_img = canvas.create_image(400, 260, image=card_front_img)
card_title = canvas.create_text(400, 150, text="Title", font=('Ariel', 40, 'italic'))
card_word = canvas.create_text(400, 250, text="word", font=('Ariel', 60, 'bold'))
canvas.grid(row=0, column=0, columnspan=2)

unknown_button_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=unknown_button_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

known_button_image = PhotoImage(file="images/right.png")
known_button = Button(image=known_button_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

next_card()

window.mainloop()
