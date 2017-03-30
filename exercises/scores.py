""" Python training exercise

Snooker scores

In snooker, two players compete to score the most points in games.  In each
game, the player with the highest points wins.  The overall winner is the player
who wins the most games out of 19.  The maximum score in one game is 147.

The score list below contains pairs of points for a snooker match (two
players).  The points are in order: player 1, player 2, player 1, player 2...
The pairs are in order of the games played.  Hence, the points scored for the
first game is:

  player1 = scores[0]
  player2 = scores[1]

(a) What were the scores of the following games, and which player won?

  (i)   The first game.
  (ii)  The second game.
  (iii) The last game (hint: use negative list indices).
  (iv)  The 10th game (hint: the player 1 index has been calculated for you).

  The first one has been completed already as an example.

(b) Use list slicing to get all the scores for player 1.  Hint: use a step size
    of 2.

(c) What was the player's total score?  Hint: use the sum() function.

(d) What was the player's best and worst score?  Hint: Try sorting the list
    first.

BONUS (after learning about lists).

(e) Compare the scores for all games to determine who won the match.

"""

# This list contains pairs of scores for a snooker match (two players).
scores = [
    40, 122, 89, 95, 5, 15, 130, 128, 37, 117, 144, 115, 14, 110, 86, 21, 75,
    109, 70, 44, 131, 142, 9, 98, 98, 77, 44, 122, 114, 78, 137, 33, 106, 104,
    103, 62, 81, 41
]


# YOUR CODE BELOW HERE.

# (a i) What is the score of the 1st game?
p1 = scores[0]
p2 = scores[1]
if p1 > p2:
    print("Player 1 won the first game.")
elif p1 < p2:
    print("Player 2 won the first game.")
else:
    print("The first game was a draw.")

# (a ii) What is the score of the 2nd game?
# <<<<<<< SOLUTION
p1 = scores[2]
p2 = scores[3]
if p1 > p2:
    print("Player 1 won the 2nd game.")
elif p1 < p2:
    print("Player 2 won the 2nd game.")
else:
    print("The 2nd game was a draw.")
# =======

# (a iii) What is the score of the last game?
# <<<<<<< SOLUTION
p1 = scores[-2]
p2 = scores[-1]
if p1 > p2:
    print("Player 1 won the last game.")
elif p1 < p2:
    print("Player 2 won the last game.")
else:
    print("The last game was a draw.")
# =======

# (a iv) What is the score of the 10th game?
game = 10
index1 = (game - 1) * 2
# <<<<<<< SOLUTION
p1 = scores[index1]
p2 = scores[index1 + 1]
if p1 > p2:
    print("Player 1 won the 10th game.")
elif p1 < p2:
    print("Player 2 won the 10th game.")
else:
    print("The 10th game was a draw.")
# =======

# (b) Player 1 scores.
# <<<<<<< SOLUTION
p1_scores = scores[0::2]
print("Player 1 scores are:\n", p1_scores)
# =======

# (c) Player 1 total score.
# <<<<<<< SOLUTION
total = sum(p1_scores)
print("Player 1 total score is:", total)
# =======

# (d) Player 1 best and worst scores.
# <<<<<<< SOLUTION
p1_scores.sort()
best = p1_scores[-1]
worst = p1_scores[0]
print("Player 1 best score is", best, "and worst score is", worst)
# =======


# BONUS (after learning loops).

# (e)  Who won?

# <<<<<<< SOLUTION
p1_scores = scores[0::2]
p2_scores = scores[1::2]

wins = [0, 0]
draws = 0

for p1, p2 in zip(p1_scores, p2_scores):
    if p1 > p2:
        wins[0] += 1
    elif p1 < p2:
        wins[1] += 1
    else:
        draws += 1

if wins[0] > wins[1]:
    print("Player 1 won the match with", wins[0], "games.")
elif wins[0] < wins[1]:
    print("Player 2 won the match with", wins[1], "games.")
else:
    print("The match was a draw with", wins[0], "games each.")
# =======
