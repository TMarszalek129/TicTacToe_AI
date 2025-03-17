if __name__ == "__main__":

    from easyAI import AI_Player, Negamax
    from TicTacToe import TicTacToe

    ai_algo = Negamax(6)
    ai_algo2 = Negamax(6)
    wins = []
    for i in range(100):
        _, loser, winner = TicTacToe([AI_Player(ai_algo), AI_Player(ai_algo2)]).play(verbose=False, possible_loss=True)
        wins.append(winner)
        print("Player {} - {} is the winner!!!".format(winner, 'O' if winner == 1 else 'X' if winner == 2 else "No one"))

    player_1_win = wins.count(1)
    player_2_win = wins.count(2)
    draws = 100 - player_1_win - player_2_win

    print("\nPlayer 1 wins {} times, \nPlayer 2 wins {} times, \nDraws: {} times".format(player_1_win, player_2_win, draws))