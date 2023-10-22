import os
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import pygame
import string

os.environ["SDL_VIDEODRIVER"] = "dummy"
pygame.init()
pygame.mixer.music.load("Ghostface Playa - Why Not.mp3")

def play_music():
    pygame.mixer.music.play()

def generate_key():
    input_word = word_entry.get()
    if not input_word:
        messagebox.showerror("Error", "Enter a word to generate a key")
        return

    input_word_list = list(input_word)
    random.shuffle(input_word_list)
    shuffled_word = ''.join(input_word_list)

    letters_key = shuffled_word[:3] + shuffled_word[-3:]
    numbers_key = ""
    alphabet = string.ascii_uppercase

    for char in letters_key:
        if char in alphabet:
            char_index = alphabet.index(char)
            numbers_key += str(char_index % 10)

    key = f"{letters_key[:3]}-{numbers_key[:6]}-{letters_key[-3:]}"
    key_label.config(text=key)

window = tk.Tk()
window.title("dr livesey rom and death edition")

bg_image = Image.open("DrLivsey.jpeg")
bg_image = ImageTk.PhotoImage(bg_image)
bg_label = tk.Label(window, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

window.geometry(f"{bg_image.width()}x{bg_image.height()}")

play_music()

word_label = tk.Label(window, text="Введи слово, юнга:")
word_label.pack()
word_entry = tk.Entry(window)
word_entry.pack()

generate_button = tk.Button(window, text="Generate Key", command=generate_key)
generate_button.pack()

key_label = tk.Label(window, text="", font=("Helvetica", 16))
key_label.pack()

window.mainloop()



