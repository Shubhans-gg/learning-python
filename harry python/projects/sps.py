import random

def sps_game():
    comp= random.choice([1,2,3])
    
    print("Press 1 for Stone")
    print("Press 2 for Paper")
    print("Press 3 for Scissors")
    gamer= int(input("Enter your choice: "))

    dict={1:"Stone",2:"Paper",3:"Scissors"}
    print(f"Computer chose: {dict[comp]}")

    if gamer==comp:
        print("It's a Tie!\n")
        return 0
    elif gamer in [1,2,3]:
        if (gamer==1 and comp==2) or (gamer==2 and comp==3) or (gamer==3 and comp==1):
            print("You lose!\n")
            return -1
        else:
            print("You win!\n")
            return 1
            
    else:
        print("Invalid input! Please choose 1, 2, or 3.")

n=int(input("Enter number of rounds you want to play: "))

gamer_score=0
comp_score=0

for i in range(1,n+1):
    print(f"--- Round {i} ---")
    result = sps_game()
    if result == -1:
        comp_score += 1
    elif result == 1:
        gamer_score += 1
print()
print(f" FINAL SCORE - You: {gamer_score}, Computer: {comp_score}")
if gamer_score > comp_score:
    print("Congratulations! You won the game!")
elif comp_score > gamer_score:
    print("Computer wins the game! Better luck next time.")
else:
    print("The game is a tie!")
print()

print("         !!Game Over!!        ")
print("     Thank you for playing   ")
