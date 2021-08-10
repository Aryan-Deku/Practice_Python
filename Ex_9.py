import random

guesses = 0
c_guesses =0
w_guesses = guesses - c_guesses

while(1<2):
    n = random.randint(1,9)
    
    g = input("""\nEnter Exit to stop the
Enter your guess from 1 to 9: """)

    if g == 'exit':
        print("\n===================================================================================\nYour Guesses: ",guesses)
        print("\n===================================================================================\nYour Correct Guesses: ",c_guesses)
        print("\n===================================================================================\nYour Wrong Guesses: ",w_guesses)
        break
    
    elif int(g) < n:
        print('The Number was ',n)
        print("\nWrong Answer, your guess was too low.\n===================================================================================")
        
        guesses += 1
        continue
    

    elif int(g) > n:
        print('The Number was ',n)
        print("\nWrong Answer, your guess was too high.\n===================================================================================")

        guesses += 1
        continue

    
    elif int(g) == n:
        print("\nBingo !!!")
        print("Jackpot !!!\n===================================================================================")
        
        guesses += 1
        c_guesses += 1
        continue

    else:
        print("\nI do not understand, please enter a number from 1 to 9 or exit only.\n ===================================================================================")
        continue