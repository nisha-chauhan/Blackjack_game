import random
import os
from Art import logo
#creating  function for random cards
def deal_cards():
    cards=[11,2,3,4,5,6,7,8,9,10,10,10]
    card=random.choice(cards)
    return card
#calculating score function

def calculate_score(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)   
def compare_score(user_score,computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose 😤"

    if user_score== computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"
def play_game():
    print(logo)
    
    user_cards=[]
    computer_cards=[] 
    stop=False
    for _ in range(2):
        user_cards.append(deal_cards())
        computer_cards.append(deal_cards())
        
    while not stop:
        user_score=calculate_score(user_cards)  
        computer_score=calculate_score(computer_cards) 
        print(f"   Your cards: {user_cards}, current score: {user_score}")
        print(f"   Computer's first card: {computer_cards[0]}")
        if user_score==0 or computer_score==0 or user_score  > 21:
            stop=True
        else:
            user_choice= input("Type 'y' to continue and 'n' for pass or exit\n")
            if user_choice=="y":
                user_cards.append(deal_cards())
            else:
                stop=True
                print("game end")
            
    while computer_score!=0 and computer_score<17:
        computer_cards.append(deal_cards())
        computer_score=calculate_score(computer_cards)
    print(f"user final hand:{user_cards},final_score:{user_score} ")
    print(f"computer final hand:{computer_cards},final_score:{computer_score} ")
    print(compare_score(user_score,computer_score))
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    os.system('cls')
    play_game()