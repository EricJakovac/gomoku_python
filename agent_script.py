import config
import random


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
    # (an example of how to implement this function)
    # similar to the function `is_terminal_state`,
    #     but instead of just checking if there is a line with 5 `player` stones,
    #     it has to count the number of `player` stones in each straight line with length 5
    #     Ignore lines for which it is impossible to have 5 `player` stones in the future
    #         (e.g., because there is an enemy stone in that line)
    # the stone count is the score
    #     but if the current player is the maximizing player the score is positive
    #     and if the current player is the minimizing player the score is negative
    # return score
    pass


# Checks if a given state is a terminal state (i.e., if the game is over: somebody won or the board is full and nobody won)
def is_terminal_state(board_matrix, player, is_max_player):
    # check if there is at least one line with 5 `player` stones
    #     (it is enough to check only the stones of the player who played last: `player`)
    #     lines can be: horizontal, vertical, or diagonal (two diagonals: / and \)
    # terminal_state is true or false (true if there is at least one line with 5 `player` stones) and false otherwise
    # score is 0, float("inf"), or float("-inf")
    #       0 if nobody won (the board is full)
    #    +inf if the maximizing player won
    #    -inf if the minimizing player won
    # return terminal_state, score
    pass


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
    # set the `move` coordinate in the board_matrix to -1 or 1 (player)
    pass

# Removes the last move
def remove_move(board_matrix, player, move):
    # set the `move` coordante in the board_matrix to 0
    pass


# Returns a list of valid moves (represented as tuples of the x and y coordinates) for the current player in the given state
#   All possible moves (empty positions)
def get_valid_moves(board_matrix):
    pass


def main(board_matrix, player):
    y = round(random.random() * (BOARD_SIZE-1))
    x = round(random.random() * (BOARD_SIZE-1))
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
