p1_score = 0
p2_score = 0

print("\nWelcome to Rock, Paper, Scissors !!!")

while (1 < 2):  
    p1_input = input('\n[Player 1] >> Enter your choice Rock / Paper / Scissors: ').lower()
    p2_input = input('\n[Player 2] >> Enter your choice Rock / Paper / Scissors: ').lower()

    if p1_input == 'rock' and p2_input == "scissors":
        p1_score += 1
        print("\nPoint for player 1.")
    
    elif p1_input == 'scissor' and p2_input == "paper":
        p1_score += 1
        print('\nPoint for player 1.')
    
    elif p1_input == 'paper' and p2_input == "rock":
        p1_score += 1
        print('\nPoint for player 1.')
    
    elif p1_input == p2_input:
        print("\nTie")
    
    elif p2_input == 'rock' and p1_input == "scissors":
        p2_score += 1
        print("\nPoint for player 2.")
    
    elif p2_input == 'scissor' and p1_input == "paper":
        p2_score += 1
        print('\nPoint for player 2.')
    
    elif p2_input == 'paper' and p1_input == "rock":
        p2_score += 1
        print('\nPoint for player 2.')
    
    else:
        print("\nI do not understand !!! Please choose either Pock, Paper or Scissors.")
        continue

    choice = input("\nDo you want to continue? (n/y): ")

    if choice == 'n':
        print("Player 1's score: ",p1_score)
        print("Player 2's score: ",p2_score)

        if p1_score > p2_score:
            print("Player 1 wins !!!")
        
        elif p2_score > p1_score:
            print("Player 2 wins !!!")
        
        elif p1_score == p2_score:
            print("Tie !!!")

        break

    elif choice == 'y':
        continue