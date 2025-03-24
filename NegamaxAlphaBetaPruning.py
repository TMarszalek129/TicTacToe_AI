from easyAI import Negamax
import pickle
import numpy as np

LOWERBOUND, EXACT, UPPERBOUND = -1, 0, 1
inf = float("infinity")

def negamax(game, depth, origDepth, scoring, alpha=+inf, beta=-inf, pruning=True):

    # alphaOrig = alpha

    if (depth == 0) or game.is_over():
        return scoring(game) * (1 + 0.001 * depth)

    possible_moves = game.possible_moves()
    state = game
    best_move = possible_moves[0]
    if depth == origDepth:
        state.ai_move = possible_moves[0]

    bestValue = -inf
    unmake_move = hasattr(state, "unmake_move")

    for move in possible_moves:

        if not unmake_move:
            game = state.copy()  # re-initialize move

        game.make_move(move)
        game.switch_player()

        value = -negamax(game, depth - 1, origDepth, scoring, -beta, -alpha, pruning)

        if unmake_move:
            game.switch_player()
            game.unmake_move(move)

        # bestValue = max( bestValue,  move_alpha )
        if bestValue < value:
            bestValue = value
            best_move = move

        if alpha < value and pruning:
            alpha = value
            # best_move = move
            if depth == origDepth:
                state.ai_move = move
            if alpha >= beta:
                break

    return bestValue

def expecti_megamax(game, depth, origDepth, scoring, alpha=+inf, beta=-inf, pruning=True, chance=False):
    if (depth == 0) or game.is_over():
        return scoring(game) * (1 + 0.001 * depth)

    possible_moves = game.possible_moves()
    state = game
    best_move = possible_moves[0]
    if depth == origDepth:
        state.ai_move = possible_moves[0]

    bestValue = -inf
    unmake_move = hasattr(state, "unmake_move")
    if not chance:
        for move in possible_moves:

            if not unmake_move:
                game = state.copy()  # re-initialize move

            game.make_move(move)
            game.switch_player()

            value = -expecti_megamax(game, depth - 1, origDepth, scoring, -beta, -alpha, pruning, True)

            if unmake_move:
                game.switch_player()
                game.unmake_move(move)

            # bestValue = max( bestValue,  move_alpha )
            if bestValue < value:
                bestValue = value
                best_move = move

            if alpha < value and pruning:
                alpha = value
                # best_move = move
                if depth == origDepth:
                    state.ai_move = move
                if alpha >= beta:
                    break

        return bestValue
    else:
        expected = 0
        for move in possible_moves:
            if not unmake_move:
                game = state.copy()  # re-initialize move

            game.make_move(move)
            # game.switch_player()
            # game.unmake_move(move)

            value = -expecti_megamax(game, depth - 1, origDepth, scoring, -beta, -alpha, pruning, False)

            if unmake_move:
                game.switch_player()
                game.unmake_move(move)

            expected += value / len(possible_moves)

        return expected
class NegamaxAB(Negamax):
    def __init__(self, depth, scoring=None, win_score = +inf, pruning=True, mode = 'negamax'):
        self.scoring = scoring
        self.depth = depth
        self.win_score = win_score
        self.pruning = pruning
        self.mode = mode

    def __call__(self, game):
        """
        Returns the AI's best move given the current state of the game.
        """

        scoring = (
            self.scoring if self.scoring else (lambda g: g.scoring())
        )  # horrible hack
        if self.mode == 'negamax':
            self.alpha = negamax(
                game,
                self.depth,
                self.depth,
                scoring,
                -self.win_score,
                +self.win_score,
                self.pruning
            )
        elif self.mode == 'expecti':
            self.alpha = expecti_megamax(
                game,
                self.depth,
                self.depth,
                scoring,
                -self.win_score,
                +self.win_score,
                self.pruning
            )
        else:
            pass
        return game.ai_move