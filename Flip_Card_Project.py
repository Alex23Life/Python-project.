import pandas as pd
from tkinter import *
from random import *

BACKGROUND_COLOR = "#B1DDC6"
to_learn = {}
current_card = {}

try:
    data = pd.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    original_data = pd.read_csv('data/french_words.csv')
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, window_flip_timer
    window.after_cancel(window_flip_timer)
    current_card = choice(to_learn)
    canvas.itemconfig(canvas_bg, image=back_card)
    canvas.itemconfig(canvas_title, text="French", fill="white")
    canvas.itemconfig(canvas_word, text=current_card['French'], fill="white")
    window_flip_timer = window.after(3000, flip_card)
    print(f"{len(to_learn)} words left.")


def flip_card():
    canvas.itemconfig(canvas_bg, image=front_card)
    canvas.itemconfig(canvas_title, text="English", fill='black')
    canvas.itemconfig(canvas_word, text=current_card['English'], fill='black')


def repeat_card():
    global window_flip_timer
    window.after_cancel(window_flip_timer)
    canvas.itemconfig(canvas_bg, image=back_card)
    canvas.itemconfig(canvas_title, text="French", fill="white")
    canvas.itemconfig(canvas_word, text=current_card['French'], fill="white")
    window_flip_timer = window.after(3000, flip_card)


def is_known():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv('data/words_to_learn.csv', index=False)
    next_card()


# WINDOW
window = Tk()
window.title("")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)
window_flip_timer = window.after(3000, func=next_card)

# IMAGES
wrong_icon = PhotoImage(file="images/wrong.png")
right_icon = PhotoImage(file="images/right.png")
repeat_icon = PhotoImage(file="images/repeat.png")
front_card = PhotoImage(file="images/card_front.png")
back_card = PhotoImage(file="images/card_back.png")

# CANVAS
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas_bg = canvas.create_image(400, 263, image=front_card)
canvas_title = canvas.create_text(400, 150, text="title", font=("Ariel", 40, "italic"))
canvas_word = canvas.create_text(400, 260, text="word", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=3)

# BUTTONS
wrong_button = Button(image=wrong_icon, bg=BACKGROUND_COLOR, command=next_card)
wrong_button.grid(column=0, row=1)
repeat_button = Button(image=repeat_icon, bg=BACKGROUND_COLOR, command=repeat_card)
repeat_button.grid(column=1, row=1)
right_button = Button(image=right_icon, bg=BACKGROUND_COLOR, command=is_known)
right_button.grid(column=2, row=1)

next_card()

window.mainloop()
