import random
from tkinter import *

from BoardGUI import BoardGUI
from Difficulty import Difficulty
from GameState import GameState
from Score import Score


def play(event):
    # Getting Selected Node
    across = int(grid.canvasx(event.x) / grid.cell_size)
    down = int(grid.canvasy(event.y) / grid.cell_size)
    cell = across + (down * 3)

    # Ensure move not played
    if ensure_move_not_played(cell):
        return

    # Check if won
    if check_winner():
        return

    #  Play game depending on difficulty
    if difficulty.get() == "Play against a friend":
        next_move(cell)
    elif difficulty.get() == "Easy":
        easy_next_move(cell)
    elif difficulty.get() == "Medium":
        medium_next_move(cell)
    elif difficulty.get() == "Hard":
        hard_next_move(cell)
    elif difficulty.get() == "Impossible":
        impossible_next_move(cell)


def ensure_move_not_played(cell):
    return True if grid.grid[cell] == "X" or grid.grid[cell] == "O" else False


def next_move(cell):
    if grid.player == "O":
        grid.draw_O(cell)
        grid.grid[cell] = "O"
        grid.player = "X"
    else:
        grid.draw_X(cell)
        grid.grid[cell] = "X"
        grid.player = "O"

    # Check if won
    if check_winner():
        return


def easy_next_move(cell):
    # Input Player's move
    grid.draw_X(cell)
    grid.grid[cell] = "X"

    # Check if won
    if check_winner():
        return

    # Get Random Place and draw/assign
    grid.play_random_playable_place()

    # Check if won
    if check_winner():
        return


def medium_next_move(cell):
    # Input Player's move
    grid.draw_X(cell)
    grid.grid[cell] = "X"
    actual_board.make_move(cell, "X")

    if actual_board.complete():
        check_winner()
        return

    if random.random() <= 0.6:
        print("Best Move")
        move = calculate_best_move(actual_board, "O")
        actual_board.make_move(move, "O")
        grid.grid[move] = "O"
        grid.draw_O(move)
    else:
        unwanted_moves = calculate_best_move(actual_board, "O", True)
        available_moves = actual_board.available_moves()

        for move in available_moves:
            if move in unwanted_moves:
                continue
            else:
                print("Worst Move")
                actual_board.make_move(move, "O")
                grid.grid[move] = "O"
                grid.draw_O(move)

                if actual_board.complete():
                    check_winner()
                    return
                return
        # Have to play random, there all good moves
        print("HAVE TO PLAY RANDOM")
        move = random.choice(unwanted_moves)
        actual_board.make_move(move, "O")
        grid.grid[move] = "O"
        grid.draw_O(move)

    if actual_board.complete():
        check_winner()
        return


def hard_next_move(cell):
    print("hard")
    # Implement
    # Input Player's move
    grid.draw_X(cell)
    grid.grid[cell] = "X"
    actual_board.make_move(cell, "X")

    if actual_board.complete():
        check_winner()
        return

    if random.random() <= 0.8:
        print("Best Move")
        move = calculate_best_move(actual_board, "O")
        actual_board.make_move(move, "O")
        grid.grid[move] = "O"
        grid.draw_O(move)

        if actual_board.complete():
            check_winner()
            return
        return
    else:
        unwanted_moves = calculate_best_move(actual_board, "O", True)
        available_moves = actual_board.available_moves()

        for move in available_moves:
            if move in unwanted_moves:
                continue
            else:
                print("Worst Move")
                actual_board.make_move(move, "O")
                grid.grid[move] = "O"
                grid.draw_O(move)

                if actual_board.complete():
                    check_winner()
                    return
                return
        # Have to play random, there all good moves
        print("HAVE TO PLAY RANDOM")
        move = random.choice(unwanted_moves)
        actual_board.make_move(move, "O")
        grid.grid[move] = "O"
        grid.draw_O(move)

    if actual_board.complete():
        check_winner()
        return


def impossible_next_move(cell):
    # Input Player's move
    grid.draw_X(cell)
    grid.grid[cell] = "X"
    actual_board.make_move(cell, "X")

    if actual_board.complete():
        check_winner()
        return

    move = calculate_best_move(actual_board, "O")
    print("MOVE: ", str(move))
    actual_board.make_move(move, "O")
    grid.grid[move] = "O"
    grid.draw_O(move)

    print("===============")
    actual_board.show()
    print("===============")

    if actual_board.complete():
        check_winner()
        return


def check_winner():
    for player in ("X", "O"):
        positions = grid.get_cells(player)
        for combo in grid.win_lines:
            win = True
            for pos in combo:
                if pos not in positions:
                    win = False
            if win:
                grid.draw_win_lines(combo, player)
                winner(player)
                return True
    if None not in [v for v in grid.grid]:
        winner("Draw")
        return True
    return False


def winner(player):
    if player == "X":
        print("X Wins!!")
        score.player_win()
    elif player == "O":
        print("O Wins!!")
        if difficulty.get() == "Play against a friend":
            score.player_2_win()
        else:
            score.ai_agent_win()
    else:
        print("Draw, Well Played")
        score.draw_()


def difficulty_option_clicked(*args):
    grid.reset()
    global friends
    if difficulty.get() == "Play against a friend":
        friends = TRUE
        score.score_label_toggle = "FRIENDS"
        score.score_label_toggle_()
    elif not difficulty.get() == "Play against a friend" and friends:
        friends = FALSE
        score.score_label_toggle = "AI"
        score.score_label_toggle_()


def reset():
    score.game_won = FALSE
    grid.reset()
    global actual_board
    actual_board = GameState()


def get_enemy(player):
    if player == "X":
        return "O"
    return "X"


def calculate_best_move(board, player, return_all=False):
    a = -2
    choices = []
    if len(board.available_moves()) == 9:
        return 4
    for move in board.available_moves():
        board.make_move(move, player)
        val = board.alphabeta(board, get_enemy(player), -2, 2)
        board.make_move(move, None)
        print("move:", move + 1, "causes:", board.outcomes[val + 1])
        if val > a:
            a = val
            choices = [move]
        elif val == a:
            choices.append(move)
    if return_all:
        return choices
    return random.choice(choices)


def play_random_playable_move():
    move = actual_board.get_random_playable_place()
    grid.draw_X(move)
    grid.grid[move] = "X"


# Main
tk = Tk()

difficulty = Difficulty(tk)
difficulty.difficulty.trace("w", difficulty_option_clicked)

grid = BoardGUI(tk, 300)
grid.bind("<Button-1>", play)

Button(tk, fg='blue', text='Reset Game', command=lambda: reset()).pack()
score = Score(tk)
friends = False

actual_board = GameState()


tk.mainloop()
