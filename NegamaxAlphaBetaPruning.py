from easyAI import Negamax
import pickle

LOWERBOUND, EXACT, UPPERBOUND = -1, 0, 1
inf = float("infinity")

def negamax(game, depth, origDepth, scoring, alpha=+inf, beta=-inf):

    alphaOrig = alpha

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

        move_alpha = -negamax(game, depth - 1, origDepth, scoring, -beta, -alpha)

        if unmake_move:
            game.switch_player()
            game.unmake_move(move)

        # bestValue = max( bestValue,  move_alpha )
        if bestValue < move_alpha:
            bestValue = move_alpha
            best_move = move

        if alpha < move_alpha:
            alpha = move_alpha
            # best_move = move
            if depth == origDepth:
                state.ai_move = move
            if alpha >= beta:
                break

    return bestValue
class NegamaxAlphaBetaPruning(Negamax):
    def __init__(self, depth, scoring=None, alpha=+inf, beta=-inf):
        self.scoring = scoring
        self.depth = depth
        self.alpha = alpha
        self.beta = beta

    def __call__(self, game):
        """
        Returns the AI's best move given the current state of the game.
        """

        scoring = (
            self.scoring if self.scoring else (lambda g: g.scoring())
        )  # horrible hack

        self.alpha = negamax(
            game,
            self.depth,
            self.depth,
            scoring,
            -self.alpha,
            +self.beta,
        )
        return game.ai_move