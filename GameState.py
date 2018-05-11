import random


class GameState(object):
    win_lines = ([0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6])
    outcomes = ("X", "Draw", "O")

    def __init__(self, cells=[]):
        if len(cells) == 0:
            self.cells = [None for i in range(9)]
        else:
            self.cells = cells

    def show(self):
        for element in [self.cells[i:i + 3] for i in range(0, len(self.cells), 3)]:
            print(element)

    def available_moves(self):
        """what spots are left empty?"""
        return [k for k, v in enumerate(self.cells) if v is None]

    def available_combos(self, player):
        """what combos are available?"""
        return self.available_moves() + self.get_squares(player)

    def complete(self):
        """is the game over?"""
        if None not in [v for v in self.cells]:
            return True
        if self.winner() is not None:
            return True
        return False

    def X_won(self):
        return self.winner() == 'X'

    def O_won(self):
        return self.winner() == 'O'

    def tied(self):
        return self.complete() and self.winner() is None

    def winner(self):
        for player in ('X', 'O'):
            positions = self.get_squares(player)
            for combo in self.win_lines:
                win = True
                for pos in combo:
                    if pos not in positions:
                        win = False
                if win:
                    return player
        return None

    def get_squares(self, player):
        """squares that belong to a player"""
        return [k for k, v in enumerate(self.cells) if v == player]

    def make_move(self, position, player):
        """place on square on the board"""
        self.cells[position] = player

    def get_random_playable_place(self):
        return random.randint(0, len(self.available_moves()) - 1)

    def alphabeta(self, node, player, alpha, beta):
        if node.complete():
            if node.X_won():
                return -1
            elif node.tied():
                return 0
            elif node.O_won():
                return 1
        for move in node.available_moves():
            node.make_move(move, player)
            val = self.alphabeta(node, get_enemy(player), alpha, beta)
            node.make_move(move, None)
            if player == 'O':
                if val > alpha:
                    alpha = val
                if alpha >= beta:
                    return beta
            else:
                if val < beta:
                    beta = val
                if beta <= alpha:
                    return alpha
        if player == 'O':
            return alpha
        else:
            return beta


def get_enemy(player):
    if player == "X":
        return "O"
    return "X"
