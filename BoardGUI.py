import numbers
import random
from tkinter import Canvas


class BoardGUI(Canvas):

    def __init__(self, master, size):
        self.cell_size = size / 3
        self.size = size
        Canvas.__init__(self, master, width=self.size, height=self.size)
        # self.bind("<Button-1>", click)
        master.title('Noughts and Crosses')
        self.pack()
        self.player = "X"
        self.reset()

    def reset(self):
        print("Reset")
        self.player = "O"
        self.delete("all")
        self.grid = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.draw_grid_lines()

    def draw_grid_lines(self):
        self.create_line(self.cell_size, 0, self.cell_size, self.size)
        self.create_line(self.cell_size * 2, 0, self.cell_size * 2, self.size)

        self.create_line(0, self.cell_size, self.size, self.cell_size)
        self.create_line(0, self.cell_size * 2, self.size, self.cell_size * 2)

    def draw_O(self, place):
        print("Drawing X at: " + str(place))
        if place == 0:
            self.create_oval(0, 0, self.cell_size, self.cell_size)
        elif place == 1:
            self.create_oval(self.cell_size, 0, self.cell_size*2, self.cell_size)
        elif place == 2:
            self.create_oval(self.cell_size*2, 0, self.cell_size*3, self.cell_size)
        elif place == 3:
            self.create_oval(0, self.cell_size, self.cell_size, self.cell_size*2)
        elif place == 4:
            self.create_oval(self.cell_size, self.cell_size, self.cell_size*2, self.cell_size*2)
        elif place == 5:
            self.create_oval(self.cell_size*2, self.cell_size, self.cell_size*3, self.cell_size*2)
        elif place == 6:
            self.create_oval(0, self.cell_size*2, self.cell_size, self.cell_size*3)
        elif place == 7:
            self.create_oval(self.cell_size, self.cell_size*2, self.cell_size*2, self.cell_size*3)
        elif place == 8:
            self.create_oval(self.cell_size*2, self.cell_size*2, self.cell_size*3, self.cell_size*3)

    def draw_X(self, place):
        print("Drawing X at: " + str(place))
        if place == 0:
            self.create_line(0, 0, self.cell_size, self.cell_size)
            self.create_line(0, self.cell_size, self.cell_size, 0)
        elif place == 1:
            self.create_line(self.cell_size, 0, self.cell_size * 2, self.cell_size)
            self.create_line(self.cell_size, self.cell_size, self.cell_size * 2, 0)
        elif place == 2:
            self.create_line(self.cell_size * 2, 0, self.cell_size * 3, self.cell_size)
            self.create_line(self.cell_size * 2, self.cell_size, self.cell_size * 3, 0)
        elif place == 3:
            self.create_line(0, self.cell_size, self.cell_size, self.cell_size * 2)
            self.create_line(0, self.cell_size * 2, self.cell_size, self.cell_size)
        elif place == 4:
            self.create_line(self.cell_size, self.cell_size, self.cell_size * 2, self.cell_size * 2)
            self.create_line(self.cell_size, self.cell_size * 2, self.cell_size * 2, self.cell_size)
        elif place == 5:
            self.create_line(self.cell_size * 2, self.cell_size, self.cell_size * 3, self.cell_size * 2)
            self.create_line(self.cell_size * 2, self.cell_size * 2, self.cell_size * 3, self.cell_size)
        elif place == 6:
            self.create_line(0, self.cell_size * 2, self.cell_size, self.cell_size * 3)
            self.create_line(0, self.cell_size * 3, self.cell_size, self.cell_size * 2)
        elif place == 7:
            self.create_line(self.cell_size * 1, self.cell_size * 2, self.cell_size * 2, self.cell_size * 3)
            self.create_line(self.cell_size, self.cell_size * 3, self.cell_size * 2, self.cell_size * 2)
        elif place == 8:
            self.create_line(self.cell_size * 2, self.cell_size * 2, self.cell_size * 3, self.cell_size * 3)
            self.create_line(self.cell_size * 2, self.cell_size * 3, self.cell_size * 3, self.cell_size * 2)

    def play_random_playable_place(self):
        playable_places = self.get_playable_places()
        place = random.randint(0, len(playable_places) - 1)
        self.draw_X(playable_places[place])
        self.grid[playable_places[place]] = "X"

    def get_playable_places(self):
        return [x for x in self.grid if isinstance(x, numbers.Number)]
