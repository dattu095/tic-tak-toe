import math


def get_possible_moves(board):
    """
    Returns a list of possible moves on the board.

    Args:
        board (Board): The current state of the game board.

    Returns:
        list: A list of tuples representing the coordinates of possible moves.
    """
    return [(i, j) for i in range(3) for j in range(3) if board.coordIsValid(i, j)]


def maximize(board, depth):
    """
    Maximizer function for the minimax algorithm.

    Args:
        board (Board): The current state of the game board.
        depth (int): The current depth in the minimax tree.

    Returns:
        int: The best score for the maximizing player.
    """
    best_score = -math.inf
    for move in get_possible_moves(board):
        board.make_move(move[0], move[1], "X")
        score = minimax(board, depth + 1, False)
        board.make_move(move[0], move[1], " ")
        best_score = max(score, best_score)
    return best_score


def minimize(board, depth):
    """
    Minimizer function for the minimax algorithm.

    Args:
        board (Board): The current state of the game board.
        depth (int): The current depth in the minimax tree.

    Returns:
        int: The best score for the minimizing player.
    """
    best_score = math.inf
    for move in get_possible_moves(board):
        board.make_move(move[0], move[1], "O")
        score = minimax(board, depth + 1, True)
        board.make_move(move[0], move[1], " ")
        best_score = min(score, best_score)
    return best_score


def minimax(board, depth, is_maximizing):
    """
    Implements the minimax algorithm for the Tic-Tac-Toe game.

    Args:
        board (Board): The current state of the game board.
        depth (int): The current depth in the minimax tree.
        is_maximizing (bool): Whether it's the maximizer's turn.

    Returns:
        int: The best score for the current board state.
    """
    result = board.checkWin()
    if result is not None:
        return result

    return maximize(board, depth) if is_maximizing else minimize(board, depth)


def get_best_move(board, player):
    """
    Determines the best move using the minimax algorithm.

    Args:
        board (Board): The current state of the game board.
        player (str): The current player ('X' or 'O').

    Returns:
        tuple: The coordinates of the best move for the current player.
    """
    best_score = -math.inf if player == "X" else math.inf
    best_move = None
    for move in get_possible_moves(board):
        board.make_move(move[0], move[1], player)
        score = minimax(board, 0, player == "O")
        board.make_move(move[0], move[1], " ")
        if player == "X" and score > best_score or player == "O" and score < best_score:
            best_score = score
            best_move = move
    return best_move
