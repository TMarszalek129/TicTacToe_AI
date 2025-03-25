from easyAI import TwoPlayerGame
from easyAI.Player import Human_Player
from abc import ABC, abstractclassmethod
from copy import deepcopy

import numpy as np

# Based on easyAI example
class TicTacToe(TwoPlayerGame):
    """The board positions are numbered as follows:
    1 2 3
    4 5 6
    7 8 9
    """
    def __init__(self, players, first_player = 1):
        self.players = players
        self.board = [0 for i in range(9)]
        self.current_player = first_player  # default player 1 starts.
        self.loser = None
        self.winner = None

    def possible_moves(self):
        return [i + 1 for i, e in enumerate(self.board) if e == 0]

    def make_move(self, move):
        self.board[int(move) - 1] = self.current_player

    def unmake_move(self, move):  # optional method (speeds up the AI)
        self.board[int(move) - 1] = 0

    def lose(self):
        """ Has the opponent "three in line ?" """
        return any(
            [
                all([(self.board[c - 1] == self.opponent_index) for c in line])
                for line in [
                    [1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9],  # horiz.
                    [1, 4, 7],
                    [2, 5, 8],
                    [3, 6, 9],  # vertical
                    [1, 5, 9],
                    [3, 5, 7],
                ]
            ]
        )  # diagonal

    def is_over(self):
        return (self.possible_moves() == []) or self.lose()

    def show(self):
            print(
                "\n"
                + "\n".join(
                    [
                        " ".join([[".", "O", "X"][self.board[3 * j + i]] for i in range(3)])
                        for j in range(3)
                    ]
                )
            )

    def scoring(self):
        return -100 if self.lose() else 0

    def play(self, nmoves=1000, verbose=True, possible_loss=False):
        """
        Method for starting the play of a game to completion. If one of the
        players is a Human_Player, then the interaction with the human is via
        the text terminal.

        Parameters
        -----------

        nmoves:
          The limit of how many moves (plies) to play unless the game ends on
          it's own first.

        verbose:
          Setting verbose=True displays additional text messages.
        """

        history = []
        if verbose:
            self.show()
        for self.nmove in range(1, nmoves + 1):
            if self.is_over():
                break
            move = self.player.ask_move(self)
            if possible_loss == True:
                num = np.random.rand()
                if num >= 0.2:
                    history.append((deepcopy(self), move))
                    self.make_move(move)
                    if verbose:
                        print(
                            "\nMove #%d: player %d plays %s :"
                            % (self.nmove, self.current_player, str(move))
                        )
                        self.show()
                        self.switch_player()
                else:
                    if verbose:
                        print(
                            "\nMove #%d:" % (self.nmove),
                            "Move failed... Try again..."
                        )
                    self.switch_player()
            elif possible_loss == False:
                history.append((deepcopy(self), move))
                self.make_move(move)
                if verbose:
                    print(
                        "\nMove #%d: player %d plays %s :"
                        % (self.nmove, self.current_player, str(move))
                    )
                    self.show()
                    self.switch_player()

        history.append(deepcopy(self))
        if self.scoring() == -100:
            self.loser = self.current_player
            self.winner = self.opponent_index

        return history, self.loser, self.winner, self.nmove-1