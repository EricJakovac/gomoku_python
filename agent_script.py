import random

import config

DEPTH = config.DEPTH

BOARD_SIZE = None
if config.BOARD_SIZE == "large":
    BOARD_SIZE = 15
elif config.BOARD_SIZE == "small":
    BOARD_SIZE = 7
elif config.BOARD_SIZE == "tiny":
    BOARD_SIZE = 3


# Evaluates the current state of the game board and returns a score that represents the desirability of the state for the maximizing player
def evaluate_state(board_matrix, player, is_max_player):
    score = 0

    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if board_matrix[i][j] == player:
                for dx, dy in [(1, 0), (0, 1), (1, 1), (1, -1)]:
                    count = 0
                    for k in range(5):
                        x, y = i + dx * k, j + dy * k
                        if 0 <= x < BOARD_SIZE and 0 <= y < BOARD_SIZE:
                            if board_matrix[x][y] == player:
                                count += 1
                            elif board_matrix[x][y] != 0:
                                break
                        else:
                            break
                    if count > 0:
                        score += count if is_max_player else -count
    return score


# Checks if a given state is a terminal state (i.e., if the game is over: somebody won or the board is full and nobody won)
def is_terminal_state(board_matrix, player):
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if board_matrix[i][j] == player:
                # Horizontalno
                if j + 4 < BOARD_SIZE and all(board_matrix[i][j + k] == player for k in range(5)):
                    return True, float("inf")
                # Vertikalno
                if i + 4 < BOARD_SIZE and all(board_matrix[i + k][j] == player for k in range(5)):
                    return True, float("inf")
                # Dijagonala /
                if i - 4 >= 0 and j + 4 < BOARD_SIZE and all(board_matrix[i - k][j + k] == player for k in range(5)):
                    return True, float("inf")
                # Dijagonala \
                if (
                    i + 4 < BOARD_SIZE
                    and j + 4 < BOARD_SIZE
                    and all(board_matrix[i + k][j + k] == player for k in range(5))
                ):
                    return True, float("inf")

    # Provjera je li ploča puna
    if all(board_matrix[i][j] != 0 for i in range(BOARD_SIZE) for j in range(BOARD_SIZE)):
        return True, 0  # Izjednačeno

    return False, None


# The minimax recursive function, returns the state's score
def minimax(board_matrix, depth, is_max_player, player):
    # if depth == 0 or gameover in current state
    #   return evaluation of current state
    #
    # if is_max_player
    #   max_eval = -inf
    #   for each child of current state
    #     eval = minimax(child, depth-1, false, player)
    #     max_eval = max(max_eval, eval)
    #   return max_eval
    #
    # else
    #   min_eval = +inf
    #   for each child of current state
    #     eval = minimax(child, depth-1, true, player)
    #     min_eval = min(min_eval, eval)
    #   return min_eval
    pass


# Modifies the given state (board_matrix) to make the specified move for the current player
def make_move(board_matrix, player, move):
    x, y = move
    board_matrix[x][y] = player


# Removes the last move
def remove_move(board_matrix, move):
    x, y = move
    board_matrix[x][y] = 0


# Returns a list of valid moves (represented as tuples of the x and y coordinates) for the current player in the given state
#   All possible moves (empty positions)
def get_valid_moves(board_matrix):
    valid_moves = []
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if board_matrix[i][j] == 0:
                valid_moves.append((i, j))
    return valid_moves


def main(board_matrix, player):
    y = round(random.random() * (BOARD_SIZE - 1))
    x = round(random.random() * (BOARD_SIZE - 1))
    print(get_valid_moves(board_matrix))
    """
    ### search for the best move with minimax algorithm
    best_score = float("-inf")
    best_move = None
    for move in get_valid_moves(board_matrix, player):
        make_move(board_matrix, player, move)
        score = minimax(board_matrix, DEPTH, True, player)
        remove_move(board_matrix, player, move)
        if score > best_score:
            best_score = score
            best_move = move
    y, x = best_move
    """
    return (y, x)
