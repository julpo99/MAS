import numpy as np

payoff_matrix_player_1 = np.array([[1, 2, 3, 3], [3, 4, 2, 4], [1, 2, 5, 2]])
payoff_matrix_player_2 = np.array([[5, 2, 4, 1], [0, 1, 5, 2], [3, 6, 2, 3]])
payoff_matrix_player_2 = np.transpose(payoff_matrix_player_2)

player_1_counts = np.array([1, 1, 1])
player_2_counts = np.array([1, 1, 1, 1])

player_1_pi_matrix = np.array([player_1_counts[0] / np.sum(player_1_counts), player_1_counts[1] / np.sum(
    player_1_counts), player_1_counts[2] / np.sum(player_1_counts)])
player_2_pi_matrix = np.array([player_2_counts[0] / np.sum(player_2_counts), player_2_counts[1] / np.sum(
    player_2_counts), player_2_counts[2] / np.sum(player_2_counts), player_2_counts[3] / np.sum(player_2_counts)])


for i in range(100):
    player_1_payoff = np.dot(payoff_matrix_player_1, player_2_pi_matrix)
    player_2_payoff = np.dot(payoff_matrix_player_2, player_1_pi_matrix)

    player_1_counts[np.argmax(player_1_payoff)] += 1
    player_2_counts[np.argmax(player_2_payoff)] += 1
    player_1_pi_matrix = np.array([player_1_counts[0] / np.sum(player_1_counts), player_1_counts[1] / np.sum(
        player_1_counts), player_1_counts[2] / np.sum(player_1_counts)])
    player_2_pi_matrix = np.array([player_2_counts[0] / np.sum(player_2_counts), player_2_counts[1] / np.sum(
        player_2_counts), player_2_counts[2] / np.sum(player_2_counts), player_2_counts[3] / np.sum(player_2_counts)])

print("Player 1 counts: ", player_1_counts)
print("Player 2 counts: ", player_2_counts)
print("Player 1 pi matrix: ", player_1_pi_matrix)
print("Player 2 pi matrix: ", player_2_pi_matrix)


# Results 1000000 iterations
# Player 1 counts:  [     1 500556 499446]
# Player 2 counts:  [     1 600020 399982      1]
# Player 1 pi matrix:  [9.99997000e-07 5.00554498e-01 4.99444502e-01]
# Player 2 pi matrix:  [9.999960e-07 6.000176e-01 3.999804e-01 9.999960e-07]

# Results 100 iterations
# Player 1 counts:  [ 1 47 55]
# Player 2 counts:  [ 1 64 38  1]
# Player 1 pi matrix:  [0.00970874 0.45631068 0.53398058]
# Player 2 pi matrix:  [0.00961538 0.61538462 0.36538462 0.00961538]