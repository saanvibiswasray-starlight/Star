import random

rno = random.randint(0, 6)
valid_guesses = list(range(7))
player1_score = 0
player2_score = 0
turns = 0

while True:
    turns += 1
    print("\n\t======= \tTHE GAME BEGINS \t=======\n")

    print("\t======= \tPLAYER 1'S TURN \t=======")
    player1_guess = int(input("\tEnter a number between 0 to 6 : "))
    if player1_guess not in valid_guesses:
        print("\tPLEASE ENTER A VALID NUMBER")
        turns -= 1
        continue

    print("\t======= \tPLAYER 2'S TURN \t=======")
    player2_guess = int(input("\tEnter a number between 0 to 6 : "))
    if player2_guess not in valid_guesses:
        print("\tPLEASE ENTER A VALID NUMBER")
        turns -= 1
        continue

    if player1_guess == rno:
        print("\n\tPlayer 1's guess is correct. Player 1 gets a point")
        player1_score += 1
    elif player2_guess == rno:
        print("\n\tPlayer 2's guess is correct. Player 2 gets a point")
        player2_score += 1
    else:
        print("\n\tOops! None of the guesses were correct")

    play_again = input("\n\tDo you want to guess again? (y/n) ")
    if play_again not in "Yy":
        break

print("\n\n\t======= \tTHE FINAL SCORES ARE DISPLAYED BELOW \t=======")
print("\n\tPLAYER 1'S SCORE : ", player1_score)
print("\n\tPLAYER 2'S SCORE : ", player2_score)
print("\n\tTOTAL NUMBER OF TURNS : ", turns)
if player1_score > player2_score:
    print("\n\tTHE WINNER IS PLAYER 1 ! :) ")
elif player2_score > player1_score:
    print("\n\tTHE WINNER IS PLAYER 2 ! :) ")
else:
    print("\n\t IT'S A DRAW ! PLAYER 1 AND PLAYER 2 ")
print("\n\t======= \tTHANK YOU FOR PLAYING OUR GAME \t=======")