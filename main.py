############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

################################################################

import random, os, art

card = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "A": [1, 11], "K": 10, "Q": 10, "J": 10}

def card_distribution(score):
    random_card = random.choice(list(card.keys()))
    if score < 11 and random_card == "A":
        score += card[random_card][1]
    elif score >= 11 and random_card == "A":
        score += card[random_card][0]
    else:
        score += card[random_card]
    
    return random_card, score

def print_cards(final, user_score, pc_score, user_inhand, pc_inhand):
    if final:
        print(f"Your Final Cards: {user_inhand}, Current Score: {user_score}")
        print(f"PC's Final Cards: {pc_inhand}, PC's Score: {pc_score}")
    else:
        print(f"Your Cards: {user_inhand}, Current Score: {user_score}")
        print(f"PC's Card: {pc_inhand[0]}")
        
def compare_score(user, pc):
    if user == 21 and pc == 21 or user == pc:
        print(art.draw)        
    elif pc == 21:
        print("PC got the Blackjack")
        print(art.lose)
    elif user == 21:
        print("You got the Blackjack")
        print(art.win)
    elif user > 21:
        print("You went over. PC Win")
        print(art.lose)
    elif pc > 21:
        print("PC went over")
        print(art.win)
    elif user > pc:
        print(art.win)
    else:
        print("PC Win")
        print(art.lose)

def blackjack():
    print(art.logo)
    user_inhand = []
    user_score = 0
    pc_inhand = []
    pc_score = 0
    
    clear = lambda: os.system('cls')
    
    should_play = True
    while should_play:
        for _ in range(2):
            user_card, user_score = card_distribution(user_score)
            user_inhand.append(user_card)
            
            pc_card, pc_score = card_distribution(pc_score)
            pc_inhand.append(pc_card)
        
        print_cards(False, user_score, pc_score, user_inhand, pc_inhand)
        
        while user_score < 21:
            choice = input("Type 'Y' to HIT another card or 'N' to PASS - ").lower()
            if choice == 'y':
                user_card, user_score = card_distribution(user_score)
                user_inhand.append(user_card)
            else:
                while pc_score <= 16:
                    pc_card, pc_score = card_distribution(pc_score)
                    pc_inhand.append(pc_card)
                break
            print_cards(False, user_score, pc_score, user_inhand, pc_inhand)

        print_cards(True, user_score, pc_score, user_inhand, pc_inhand)
        
        compare_score(user_score, pc_score)
        
        round_choice = input("Type 'Y' to play another round or type 'N' to exit - ").lower()        
        if round_choice == 'y':
            clear()
            blackjack()
        else:
            should_play = False
            print("Thank you for playing the game. Hope you liked it. Goodbye!")
blackjack()