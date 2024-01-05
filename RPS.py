import random

RPS = ("rock", "paper", "scissers")
com = random.randint(0,2)
play = ""


while play != "stop":
    play = input("Put \"rock\", \"paper\", \"scissers\" or \"stop\"".lower())
    if play ==  RPS[com]:
        print("the computer put " + str(RPS[com]))
        print("tie")
    elif play == "paper" and RPS[com] == "rock":
        print("the computer put " + str(RPS[com]))
        print("you win")
    elif play == "scissers" and RPS[com] == "rock":
        print("the computer put " + str(RPS[com]))
        print("you lose")
    elif play == "rock" and RPS[com] == "paper":
        print("the computer put " + str(RPS[com]))
        print("you lose")
    elif play == "scissers" and RPS[com] == "paper":
        print("the computer put " + str(RPS[com]))
        print("you win")
    elif play == "rock" and RPS[com] == "scissers":
        print("the computer put " + str(RPS[com]))
        print("you win")
    elif play == "paper" and RPS[com] == "scissers":
        print("the computer put " + str(RPS[com]))
        print("you lose")
    com = random.randint(0,2)