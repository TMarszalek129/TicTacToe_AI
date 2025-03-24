if __name__ == "__main__":

    from easyAI import AI_Player, Negamax
    from NegamaxAlphaBetaPruning import NegamaxAB
    from TicTacToe import TicTacToe

    import numpy as np
    import time

    ai_algo = NegamaxAB(1, pruning=True, mode='expecti')
    ai_algo2 = NegamaxAB(10, pruning=True, mode='expecti')
    # ai_algo = Negamax(2)
    # ai_algo2 = Negamax(8)
    wins = []
    times = []
    for i in range(100):
        start = time.time()
        _, loser, winner, nmove = TicTacToe([AI_Player(ai_algo), AI_Player(ai_algo2)], first_player=2)\
            .play(verbose=False, possible_loss=True)
        end = time.time()
        wins.append(winner)
        times.append((end - start)/nmove)
        print("Player {} - {} is the winner!!!".format(winner, 'O' if winner == 1 else 'X' if winner == 2 else "No one"))

    player_1_win = wins.count(1)
    player_2_win = wins.count(2)
    draws = 100 - player_1_win - player_2_win
    avg_times = np.mean(times)

    print("\nPlayer 1 wins {} times, \nPlayer 2 wins {} times, \nDraws: {} times".format(player_1_win, player_2_win, draws))
    print('Average decision time: ', avg_times)