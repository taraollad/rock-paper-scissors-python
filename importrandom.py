import random
score1=0
score2=0
score_total=10
while score1<score_total or score2<score_total :
    user_action = input("enter a choice(rock, paper,scissors): ")
    possible_action = ["rock", "paper", "scissors"]
    computer_action = random. choice(possible_action)
    print (f"\nYou choose {user_action}, computer chose {computer_action}.\n") 
    if user_action == computer_action :
        print(f"both players selected ({user_action}. its a tie !")
    elif user_action == "rock":
        if computer_action == "scissors":
            print ("rock smashes scissors ! you win.")
            score1+=1
            print (score1)
        else :
            print("paper cover rock! you lose.")
            score2+=1
            print (score2)
    elif user_action == "paper":
        if computer_action == "rock":
            print("paper covers rock! you lose.")
            score1+=1
            print (score1)
        else :
            print("scissors cuts paper! you lose.")
            score2+=1
            print (score2)
    elif user_action == "scissors":
        if computer_action == "paper":
            print ("scissors cuts paper ! you win.")
            score1+=1
            print (score1)
    else :
        print ("rock smash scissors ! you lose.")