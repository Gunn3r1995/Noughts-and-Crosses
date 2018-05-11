import numbers
import random
from tkinter import Canvas


class BoardGUI(Canvas):
    win_lines = ([0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6])

    def __init__(self, master, size):
        self.cell_size = size / 3
        self.size = size
        Canvas.__init__(self, master, width=self.size, height=self.size)
        master.title('Noughts and Crosses')
        self.pack()
        self.player = "X"
        self.reset()

    def reset(self):
        print("Reset")
        self.player = "X"
        self.delete("all")
        self.grid = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.draw_grid_lines()

    def draw_grid_lines(self):
        self.create_line(self.cell_size, 0, self.cell_size, self.size)
        self.create_line(self.cell_size * 2, 0, self.cell_size * 2, self.size)

        self.create_line(0, self.cell_size, self.size, self.cell_size)
        self.create_line(0, self.cell_size * 2, self.size, self.cell_size * 2)

    def draw_O(self, cell):
        print("Drawing X at: " + str(cell))
        if cell == 0:
            self.create_oval(0, 0, self.cell_size, self.cell_size)
        elif cell == 1:
            self.create_oval(self.cell_size, 0, self.cell_size * 2, self.cell_size)
        elif cell == 2:
            self.create_oval(self.cell_size * 2, 0, self.cell_size * 3, self.cell_size)
        elif cell == 3:
            self.create_oval(0, self.cell_size, self.cell_size, self.cell_size * 2)
        elif cell == 4:
            self.create_oval(self.cell_size, self.cell_size, self.cell_size * 2, self.cell_size * 2)
        elif cell == 5:
            self.create_oval(self.cell_size * 2, self.cell_size, self.cell_size * 3, self.cell_size * 2)
        elif cell == 6:
            self.create_oval(0, self.cell_size * 2, self.cell_size, self.cell_size * 3)
        elif cell == 7:
            self.create_oval(self.cell_size, self.cell_size * 2, self.cell_size * 2, self.cell_size * 3)
        elif cell == 8:
            self.create_oval(self.cell_size * 2, self.cell_size * 2, self.cell_size * 3, self.cell_size * 3)

    def draw_X(self, cell):
        print("Drawing X at: " + str(cell))
        if cell == 0:
            self.create_line(0, 0, self.cell_size, self.cell_size)
            self.create_line(0, self.cell_size, self.cell_size, 0)
        elif cell == 1:
            self.create_line(self.cell_size, 0, self.cell_size * 2, self.cell_size)
            self.create_line(self.cell_size, self.cell_size, self.cell_size * 2, 0)
        elif cell == 2:
            self.create_line(self.cell_size * 2, 0, self.cell_size * 3, self.cell_size)
            self.create_line(self.cell_size * 2, self.cell_size, self.cell_size * 3, 0)
        elif cell == 3:
            self.create_line(0, self.cell_size, self.cell_size, self.cell_size * 2)
            self.create_line(0, self.cell_size * 2, self.cell_size, self.cell_size)
        elif cell == 4:
            self.create_line(self.cell_size, self.cell_size, self.cell_size * 2, self.cell_size * 2)
            self.create_line(self.cell_size, self.cell_size * 2, self.cell_size * 2, self.cell_size)
        elif cell == 5:
            self.create_line(self.cell_size * 2, self.cell_size, self.cell_size * 3, self.cell_size * 2)
            self.create_line(self.cell_size * 2, self.cell_size * 2, self.cell_size * 3, self.cell_size)
        elif cell == 6:
            self.create_line(0, self.cell_size * 2, self.cell_size, self.cell_size * 3)
            self.create_line(0, self.cell_size * 3, self.cell_size, self.cell_size * 2)
        elif cell == 7:
            self.create_line(self.cell_size * 1, self.cell_size * 2, self.cell_size * 2, self.cell_size * 3)
            self.create_line(self.cell_size, self.cell_size * 3, self.cell_size * 2, self.cell_size * 2)
        elif cell == 8:
            self.create_line(self.cell_size * 2, self.cell_size * 2, self.cell_size * 3, self.cell_size * 3)
            self.create_line(self.cell_size * 2, self.cell_size * 3, self.cell_size * 3, self.cell_size * 2)

    def play_random_playable_place(self):
        playable_places = self.get_playable_places()
        move = random.randint(0, len(playable_places) - 1)
        self.draw_O(playable_places[move])
        self.grid[playable_places[move]] = "O"

    def get_playable_places(self):
        return [x for x in self.grid if isinstance(x, numbers.Number)]

    def get_cells(self, player):
        return [k for k, v in enumerate(self.grid) if v == player]

    def draw_win_lines(self, winning_line, player):
        if winning_line == [0, 1, 2]:
            self.create_line(0, self.cell_size / 2, self.size, self.cell_size / 2, width=5,
                             fill=self.get_player_colour(player))
        elif winning_line == [3, 4, 5]:
            self.create_line(0, self.cell_size + self.cell_size / 2, self.size, self.cell_size + self.cell_size / 2,
                             width=5, fill=self.get_player_colour(player))
        elif winning_line == [6, 7, 8]:
            self.create_line(0, self.cell_size * 2 + self.cell_size / 2, self.size,
                             self.cell_size * 2 + self.cell_size / 2, width=5, fill=self.get_player_colour(player))
        elif winning_line == [0, 3, 6]:
            self.create_line(self.cell_size / 2, 0, self.cell_size / 2, self.size, width=5,
                             fill=self.get_player_colour(player))
        elif winning_line == [1, 4, 7]:
            self.create_line(self.cell_size + self.cell_size / 2, 0, self.cell_size + self.cell_size / 2, self.size,
                             width=5, fill=self.get_player_colour(player))
        elif winning_line == [2, 5, 8]:
            self.create_line(self.cell_size * 2 + self.cell_size / 2, 0, self.cell_size * 2 + self.cell_size / 2,
                             self.size, width=5, fill=self.get_player_colour(player))
        elif winning_line == [0, 4, 8]:
            self.create_line(0, 0, self.size, self.size, width=5, fill=self.get_player_colour(player))
        elif winning_line == [2, 4, 6]:
            self.create_line(0, self.size, self.size, 0, width=5, fill=self.get_player_colour(player))

    @staticmethod
    def get_player_colour(player):
        if player == "X":
            return "Green"
        return "Red"
