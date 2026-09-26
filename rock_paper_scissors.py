# Rock-Paper-Scissors game
import random
print("\n\t======= \tWELCOME PLAYER \t=======")
opt = ["r", "p", "s"]  # list of options
h_p = 0  # human point
c_p = 0  # computer point
turns = 0
print("\n\t====== \tABBREVIATIONS \t=======")
print("\n\tR \tFOR \tROCK ")
print("\n\tP \tFOR \tPAPER ")
print("\n\tS \tFOR \tSCISSORS ")
print("\n\tQ \tFOR \tTO QUIT ")
while True:
    print("\n\t======= \tROUND BEGINS \t=======\n")
    human = input("\tEnter (R) OR (P) OR (S) OR (Q) : ")
    user = human.lower()

    if user in opt:
        turns += 1
        pass
    elif user in "q":
        print("\n\t======= \tYOU HAVE QUIT THE GAME \t=======")
        break
    else:
        print("\n\t======= \tPLEASE ENTER A VALID OPTION \t=======")
        continue

# computer game
    num = random.randint(0, 2)
    comp = opt[num]
    print("\t THE COMPUTER CHOOSES : ", comp)

    if comp in "r":
        if user in "r":
            print("\n\tIT IS A DRAW")
        if user in "p":
            print("\n\tUSER WINS A POINT")
            h_p += 1
        if user in "s":
            print("\n\tCOMPUTER WINS A POINT")
            c_p += 1

    elif comp in "p":
        if user in "p":
            print("\n\tIT IS A DRAW")
        if user in "s":
            print("\n\tUSER WINS A POINT")
            h_p += 1
        if user in "r":
            print("\n\tCOMPUTER WINS A POINT")
            c_p += 1

    else:
        if user in "s":
            print("\n\tIT IS A DRAW")
        if user in "r":
            print("\n\tUSER WINS A POINT")
            h_p += 1
        if user in "p":
            print("\n\tCOMPUTER WINS A POINT")
            c_p += 1

print("\n\t======= \tTHE DETAILS OF THE GAME ARE SHOWN BELOW \t=======")
print("\n\tYOUR SCORE : ", h_p)
print("\n\tCOMPUTER'S SCORE : ", c_p)
print("\n\tTOTAL NUMBER OF TURNS : ", turns)
if h_p > c_p:
    print("\n\t======= \tYOU WON THE GAME \t=======")
elif h_p < c_p:
    print("\n\t======= \tCOMPUTER WON THE GAME \t=======")
else:
    print("\n\t======= \tIT IS A DRAW \t=======")

print("\n\t======= \tTHANK YOU FOR PLAYING \t=======")
