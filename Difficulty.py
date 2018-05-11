from tkinter import *


class Difficulty:

    def __init__(self, tk):
        self.difficulty = StringVar()
        self.difficulty.set("Easy")
        Label(tk, text="Choose Difficulty, or player against a friend").pack()
        OptionMenu(tk, self.difficulty, "Easy", "Medium", "Hard", "Impossible", "Play against a friend").pack(pady=5)

    def get(self):
        return self.difficulty.get()