import random
import matplotlib.pyplot as plt

def tit_for_tat(player_last_move, opponent_last_move):
    if opponent_last_move is None:
        return 'C'
    else:
        return opponent_last_move

def random_player(player_last_move, opponent_last_move):
    return random.choice(['C', 'D'])

def unforgiving_player(player_last_move, opponent_last_move):
    if opponent_last_move and 'D' in opponent_last_move:
        return 'D'  # Defect if opponent has ever defected
    else:
        return 'C'

def calculate_points(move1, move2):
    if move1 == 'C' and move2 == 'C':
        return 3, 3
    elif move1 == 'C' and move2 == 'D':
        return 0, 5
    elif move1 == 'D' and move2 == 'C':
        return 5, 0
    elif move1 == 'D' and move2 == 'D':
        return 1, 1

def play_game(player1_strategy, player2_strategy, player3_strategy, rounds=10):
    player1_moves = []
    player2_moves = []
    player3_moves = []
    player1_points = []
    player2_points = []
    player3_points = []

    for _ in range(rounds):
        player1_last_move = player1_moves[-1] if player1_moves else None
        player2_last_move = player2_moves[-1] if player2_moves else None
        player3_last_move = player3_moves[-1] if player3_moves else None

        player1_move = player1_strategy(player1_last_move, player2_last_move)
        player2_move = player2_strategy(player2_last_move, player1_last_move)
        player3_move = player3_strategy(player3_last_move, player1_last_move)

        player1_moves.append(player1_move)
        player2_moves.append(player2_move)
        player3_moves.append(player3_move)

        points1, points2 = calculate_points(player1_move, player2_move)
        points1_3, points3 = calculate_points(player1_move, player3_move)

        player1_points.append(points1 + points1_3)
        player2_points.append(points2)
        player3_points.append(points3)

        print(f"Round {_ + 1}: Player 1 ({player1_move}) vs. Player 2 ({player2_move}) vs. Player 3 ({player3_move})")

    return player1_points, player2_points, player3_points

def plot_results(player1_points, player2_points, player3_points):
    rounds = list(range(1, len(player1_points) + 1))
    cumulative_points_player1 = [sum(player1_points[:i]) for i in range(1, len(player1_points) + 1)]
    cumulative_points_player2 = [sum(player2_points[:i]) for i in range(1, len(player2_points) + 1)]
    cumulative_points_player3 = [sum(player3_points[:i]) for i in range(1, len(player3_points) + 1)]

    plt.plot(rounds, cumulative_points_player1, label='Tit for Tat')
    plt.plot(rounds, cumulative_points_player2, label='Unforgiving Player')
    plt.plot(rounds, cumulative_points_player3, label='Random Player')
    plt.xlabel('Rounds')
    plt.ylabel('Cumulative Points')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    # Play games
    results_game1 = play_game(tit_for_tat, random_player, unforgiving_player, rounds=10)
    results_game2 = play_game(unforgiving_player, tit_for_tat, random_player, rounds=10)

    # Combine results from all games
    total_player1_points = results_game1[0] + results_game2[0]
    total_player2_points = results_game1[1] + results_game2[1]
    total_player3_points = results_game1[2] + results_game2[2]

    # Plot cumulative points for each player across all games
    plot_results(total_player1_points, total_player2_points, total_player3_points)

# 