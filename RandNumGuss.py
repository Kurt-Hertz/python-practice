import random

def guess():
    ran = random.randrange(0, 1000)
    guess = int(input("Guess the number between 0 and 1000"))

    while guess != ran:
    
        if guess > ran: 
            print("Your guess is to High")
            guess = int(input("Guess the number between 0 and 1000"))
        elif guess < ran:
            print("Your guess is to Low")
            guess = int(input("Guess the number between 0 and 1000"))
        else:
            print("Error")
        
    print("you got it right")

def inguess():
    print("Think of a random number between 0 and 1000")
    top = 1000
    bot = 0
    com = random.randrange(bot, top)
    ans = ""

    while ans != "right":
        print(com)
        ans = input("is this number to \"high\" or to \"low\" or right".lower())
        if ans == "high":
            top = (com-1)
            com = random.randrange(bot, top)
        elif ans == "low":
            bot = (com+1)
            com = random.randrange(bot, top)
    print("lets go")

inguess()