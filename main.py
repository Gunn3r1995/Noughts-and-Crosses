from tkinter import *

from Grid import Grid
from Difficulty import Difficulty
from Score import Score


def play(event):
    global grid
    # Getting Selected Node
    across = int(grid.canvasx(event.x) / grid.cell_size)
    down = int(grid.canvasy(event.y) / grid.cell_size)
    square = across + (down * 3)

    if grid.grid[square] == "X" or grid.grid[square] == "O":
        return

    # Check if won
    if check_winner():
        return

    #  Play game depending on difficulty
    if difficulty.difficulty.get() == "Play against a friend":
        next_move(across, down, square)
    elif difficulty.difficulty.get() == "Easy":
        easy_next_move(across, down, square)
    elif difficulty.difficulty.get() == "Medium":
        medium_next_move(across, down, square)
    elif difficulty.difficulty.get() == "Hard":
        hard_next_move(across, down, square)
    elif difficulty.difficulty.get() == "Impossible":
        impossible_next_move(across, down, square)


def next_move(across, down, square):
    if grid.player == "O":
        grid.create_oval(
            across * grid.cell_size, down * grid.cell_size,
            (across + 1) * grid.cell_size, (down + 1) * grid.cell_size
        )
        grid.grid[square] = "O"
        grid.player = "X"
    else:
        grid.create_line(
            across * grid.cell_size, down * grid.cell_size,
            (across + 1) * grid.cell_size, (down + 1) * grid.cell_size
        )
        grid.create_line(
            across * grid.cell_size, (down + 1) * grid.cell_size,
            (across + 1) * grid.cell_size, down * grid.cell_size
        )
        grid.grid[square] = "X"
        grid.player = "O"

    # Check if won
    if check_winner():
        return


def easy_next_move(across, down, square):
    # Input Player's move
    grid.create_oval(
        across * grid.cell_size, down * grid.cell_size,
        (across + 1) * grid.cell_size, (down + 1) * grid.cell_size
    )
    grid.grid[square] = "O"

    # Check if won
    if check_winner():
        return

    # Get Random Place and draw/assign
    grid.play_random_playable_place()

    # Check if won
    if check_winner():
        return


def medium_next_move(across, down, square):
    print("medium")
    # Implement


def hard_next_move(across, down, square):
    print("hard")
    # Implement


def impossible_next_move(across, down, square):
    print("impossible")
    # Implement


def check_winner():
    for across in range(3):
        row = across * 3
        line = str(grid.grid[row]) + str(grid.grid[row + 1]) + str(grid.grid[row + 2])
        if line == "XXX":
            grid.create_line(0, grid.cell_size * across + grid.cell_size / 2,
                             grid.size, grid.cell_size * across + grid.cell_size / 2, width=5, fill="red")
            winner("X")
            return TRUE
        elif line == "OOO":
            grid.create_line(0, grid.cell_size * across + grid.cell_size / 2,
                             grid.size, grid.cell_size * across + grid.cell_size / 2, width=5, fill="green")
            winner("O")
            return TRUE

    for down in range(3):
        line = str(grid.grid[down]) + str(grid.grid[down + 3]) + str(grid.grid[down + 6])
        if line == "XXX":
            grid.create_line(grid.cell_size * down + grid.cell_size / 2, 0,
                             grid.cell_size * down + grid.cell_size / 2, grid.size, width=5, fill="red")
            winner("X")
            return TRUE
        elif line == "OOO":
            grid.create_line(grid.cell_size * down + grid.cell_size / 2, 0,
                             grid.cell_size * down + grid.cell_size / 2, grid.size, width=5, fill="green")
            winner("O")
            return TRUE

    line = str(grid.grid[0]) + str(grid.grid[4]) + str(grid.grid[8])

    if line == "XXX":
        grid.create_line(0, 0, grid.size, grid.size, width=5, fill="red")
        winner("X")
        return TRUE
    elif line == "OOO":
        grid.create_line(0, 0, grid.size, grid.size, width=5, fill="green")
        winner("O")
        return TRUE

    line = str(grid.grid[2]) + str(grid.grid[4]) + str(grid.grid[6])

    if line == "XXX":
        grid.create_line(0, grid.size, grid.size, 0, width=5, fill="red")
        winner("X")
        return TRUE
    elif line == "OOO":
        grid.create_line(0, grid.size, grid.size, 0, width=5, fill="green")
        winner("O")
        return TRUE

    if len(grid.get_playable_places()) == 0:
        winner("DRAW")
        return TRUE

    return FALSE


def winner(player):
    if player == "O":
        print("Winner Player, Congratulations!!")
        score.player_win()
    elif player == "X":
        print("Better Luck Next Time!")
        if difficulty.difficulty.get() == "Play against a friend":
            score.player_2_win()
        else:
            score.ai_agent_win()
    else:
        print("Draw, Well Played")
        score.draw_()


def difficulty_option_clicked(*args):
    grid.reset()
    global friends
    if difficulty.difficulty.get() == "Play against a friend":
        friends = TRUE
        score.score_label_toggle = "FRIENDS"
        score.score_label_toggle_()
    elif not difficulty.difficulty.get() == "Play against a friend" and friends:
        friends = FALSE
        score.score_label_toggle = "AI"
        score.score_label_toggle_()


def reset():
    score.game_won = FALSE
    grid.reset()


# Main
tk = Tk()

difficulty = Difficulty(tk)
difficulty.difficulty.trace("w", difficulty_option_clicked)

grid = Grid(tk, 300)
grid.bind("<Button-1>", play)

Button(tk, fg='blue', text='Reset Game', command=lambda: reset()).pack()
score = Score(tk)
friends = FALSE

tk.mainloop()
