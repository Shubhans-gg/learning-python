import random

target=random.randint(1,100)
guess=int(input("Enter a guess between 1 to 100:"))
attempts=1
while(guess!=target):
    if (guess>target):
        print("Your guess is greater than the target number")
        guess=int(input("Common have an another guess:"))
        attempts=attempts+1
    
    else:
        print("Your guess is smaller than the target number")
        guess=int(input("Common have an another guess:"))
        attempts=attempts+1
    
print("!!YOU GUESSED IT!!")
print("The number was",target,"and you guessed it in",attempts,"attempts")