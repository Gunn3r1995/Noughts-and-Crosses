from tkinter import *


class Score:

    def __init__(self, tk):
        self.player = IntVar()
        self.draw = IntVar()
        self.ai_agent = IntVar()
        self.player_2 = IntVar()
        self.game_won = FALSE
        self.score_label_toggle = "AI"

        self.score_label = Label(tk, text="Player: " + str(self.player.get()) +
                                          "\n Draw: " + str(self.draw.get()) +
                                          "\n AI Agent: " + str(self.ai_agent.get()))
        self.score_label.pack()

    def player_win(self):
        if not self.game_won:
            self.player.set(self.player.get() + 1)
            self.update_label()
            self.game_won = TRUE

    def player_2_win(self):
        if not self.game_won:
            self.player_2.set(self.player_2.get() + 1)
            self.update_label()
            self.game_won = TRUE

    def ai_agent_win(self):
        if not self.game_won:
            self.ai_agent.set(self.ai_agent.get() + 1)
            self.update_label()
            self.game_won = TRUE

    def draw_(self):
        if not self.game_won:
            self.draw.set(self.draw.get() + 1)
            self.update_label()
            self.game_won = TRUE

    def score_label_toggle_(self):
        if self.score_label_toggle == "AI":
            self.player.set(0)
            self.ai_agent.set(0)
            self.draw.set(0)

            self.score_label["text"] = "Player: " + str(self.player.get()) + \
                                       "\n Draw: " + str(self.draw.get()) + \
                                       "\n AI Agent: " + str(self.ai_agent.get())
        elif self.score_label_toggle == "FRIENDS":
            self.player.set(0)
            self.draw.set(0)
            self.player_2.set(0)

            self.score_label["text"] = "Player: " + str(self.player.get()) + \
                                       "\n Draw: " + str(self.draw.get()) + \
                                       "\n Player 2: " + str(self.player_2.get())

    def update_label(self):
        if self.score_label_toggle == "AI":
            self.score_label["text"] = "Player: " + str(self.player.get()) + \
                                       "\n Draw: " + str(self.draw.get()) + \
                                       "\n AI Agent: " + str(self.ai_agent.get())
        else:
            self.score_label["text"] = "Player: " + str(self.player.get()) + \
                                       "\n Draw: " + str(self.draw.get()) + \
                                       "\n Player 2: " + str(self.player_2.get())
