import random

#class blackjack():

def ace():
    cho = input("whoudl you like the ace to be worth 11 or 1")
    return int(cho)

def convert(hand):
    val = 0
    for i in range(len(hand)):
        if 'ace' in hand[i]:
            val += ace()
        elif 'jack' in hand[i]:
            val += 10
        elif 'queen' in hand[i]:
            val += 10
        elif 'king' in hand[i]:
            val += 10
        else:
            num = hand[i].split(' of ')
            val += int(num[0])
    return val

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

def dealOne(hand):
    cardsV = ["ace",2 ,3 , 4 , 5, 6, 7, 8, 9, 10, 'king', 'queen' ,'jack']
    cardsS = ["clubs", "hearts", "spades", "dimands"]
    
    hand += [str(random.choice(cardsV)) + ' of ' + random.choice(cardsS)]
    return hand

def Player(hand):
    
    act = 'hit'
    while act != 'stay':
        print(hand)
        act = input("if you would like to stay type \'stay\'")
        
        if act == 'hit':
            hand = dealOne(hand)
    return hand

def dealer(hand):
    while convert(hand) < 16:
        hand = dealOne(hand)
    return hand

def win(hands):
    dealerV = convert(hands[len(hands)-1])
    if dealerV > 22:
        return f"all players won, the dealer had {dealerV}"
    for i in range(len(hands)):
        if convert(hands[i]) > convert(hands[len(hands)-1]) and convert(hands[i]) > 22:
            return f"player {i} you won your bet, the dealer had {dealerV}"
        else:
            return f"player {i} you lost your bet, the dealer had {dealerV}"
    


def play():
    numberP = int(input("how many player / bots do you want to play with (in total)"))
    hands = deal(numberP)
    for i in range(numberP-1):
        Player(hands[i])
   
    dealer(hands[numberP-1])

    print(win(hands))


play()