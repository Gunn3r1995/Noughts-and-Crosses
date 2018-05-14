import random


class GameState(object):
    win_lines = ([0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6])
    outcomes = ("X", "Draw", "O")

    def __init__(self, cells=[]):
        if len(cells) == 0:
            self.cells = [None for i in range(9)]
        else:
            self.cells = cells

    def playable_cells(self):
        return [i for i, j in enumerate(self.cells) if j is None]

    def available_combos(self, player):
        return self.playable_cells() + self.get_cells(player)

    def complete(self):
        if None not in [v for v in self.cells]:
            return True
        if self.winner() is not None:
            return True
        return False

    def X_won(self):
        return self.winner() == "X"

    def O_won(self):
        return self.winner() == "O"

    def tied(self):
        return self.complete() and self.winner() is None

    def winner(self):
        for player in ("X", "O"):
            played_cells = self.get_cells(player)
            for combo in self.win_lines:
                win = True
                for cell in combo:
                    if cell not in played_cells:
                        win = False
                if win:
                    return player
        return None

    def get_cells(self, player):
        return [k for k, v in enumerate(self.cells) if v == player]

    def make_move(self, cell, player):
        self.cells[cell] = player

    def get_random_playable_place(self):
        return random.randint(0, len(self.playable_cells()) - 1)

    def minimax(self, game_state, player, alpha, beta):
        # Check game_state is complete
        if game_state.complete():
            if game_state.X_won():
                return -1
            elif game_state.tied():
                return 0
            elif game_state.O_won():
                return 1
        # Get all playable cells and make all possible moves
        for move in game_state.playable_cells():
            # Make move
            game_state.make_move(move, player)
            # Continue to go deeper (Until complete)
            val = self.minimax(game_state, swap_player(player), alpha, beta)
            # Undo last move (for game_state)
            game_state.make_move(move, None)
            # Check if move is best value for AI (Alpha-beta prune)
            if player == 'O':
                if val > alpha:
                    alpha = val
                if alpha >= beta:
                    return beta
            else:
                # Check if move is worst value for Human (Alpha-beta prune)
                if val < beta:
                    beta = val
                if beta <= alpha:
                    return alpha
        if player == 'O':
            return alpha
        else:
            return beta


def swap_player(player):
    # Swap current player
    if player == "X":
        return "O"
    return "X"
