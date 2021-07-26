import random

N = int(input("How many sticks(N) in the pile: "))
print("there are", N, "sticks in the pile.")

# function for choosing who is the first picking the sticks
def first_player():
    if random.randint(0, 1) == 0:
        return "player1"
    else:
        return "smart_computer"

# Check the number of stick the player took that must be only 1 or 2
def check_pick(pick):
    if pick < 1:
        return False
    elif pick > 2:
        return False
    else:
        return True

# the strategy the smart com to get win
def win_strategy(N):
    choose = (N-1) % 3
    # the result above has only 0, 1, 2 then continue this loop
    # so the condition made for 3 case choose ==1, 2 and 3
    # we need to get the last number of N is 2 in order to win!
    if choose == 2:
        for i in range(N-(choose-1), choose-1, -3): # ith is the position that computer will take(to win)
            if N - i == 0:
                num_com = 1 #num_com is number of stick that computer will take
                break
            else:
                num_com = 2
                break
    elif choose == 0:
        for i in range(N-2, choose-1, -3):
            if N - i == 0: # if com is the 2nd player(the 1st player take 2 stick)
                num_com = 1
                break
            elif N - i == 1: # if com is the 2nd player(the 1st player take 1 stick) 
                num_com = 2
                break
            else: # if com is the first player
                num_com = random.randint(1, 2)
                break
    else: # in the case choose == 1
        for i in range(N-(choose-1), choose, -3):
            if N - i == 0: # case com is the first: will take 1
                num_com = 1
                break
            elif N - i == 1: # case player1 is the first: takes for 2 at first
                num_com = 2
                break
            else: # case player 1 is the fist: take just 1 stick
                num_com = random.randint(1, 2)

    return num_com


name = input("What is your name: ")
turn = first_player()


if turn == "player1":
    print(f"{name} takes the sticks first!")
else:
    print("Smart computer takes the sticks first!")

# list of player1 and computer to check who takes the last stick.
last_turn = []

while N != 0:

    # player1 turn
    if turn == "player1":
        pick = int(input(f"{name}, How many sticks you will take (1 or 2): "))
        if check_pick(pick) == True: # the function to check number of taking the pile must be only 1 or 2
            if N - pick > 0:
                print("There are", N-pick, "sticks in the pile")
                N = N - pick
                last_turn.append(name)
                turn = "smart computer"
            elif N - pick == 0:
                N = N - pick
            else:
                print("There are no enough sticks to take")
                turn = "player1"
        else:
            print("Try again, the number of sticks is available for only 1 or 2.")
            turn = "player1"


    else:
        # computer's turn
       
        if N == 1:
            pick_com = 1
        else: # Win strategy
            pick_com = win_strategy(N)

        print(f"I, smart computer, takes: {pick_com}")

        if N-pick_com > 0:   
            print("There are", N-pick_com, "sticks in the pile")
            N = N - pick_com
            last_turn.append("smart computer")
            turn = "player1"
        elif N - pick_com == 0:
            N = N - pick_com           
        else:
            print("There are no enough sticks to take")
            turn = "smart computer"

# check who is winning
if last_turn[-1] == name:
    print("I, smart computer, takes the last stick.")
    print(f"{name} win (I, smart computer, am sad T_T)")
else:
    print(f"{name} takes the last stick")
    print("I, smart computer, win !!!!")