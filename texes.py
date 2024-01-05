import random



def deal(players):
    cardsV = ["ace",2 ,3 , 4 , 5, 6, 7, 8, 9, 10, 'king', 'queen' ,'jack']
    cardsS = ["clubs", "hearts", "spades", "dimands"]
    Hands = []
    for j in range(int(players)):
        Hand = []
        for i in range(2):
            Hand.append(str(random.choice(cardsV)) + ' of ' + random.choice(cardsS))
        Hands.append(Hand)
    return Hands

def game():
    bets = []
    numberP = int(input("how many player / bots do you want to play with (in total)"))
    hands = deal(numberP)
    for i in range(1,numberP):
        bets.append(input(f"how much do you want to bet player {i}"))
