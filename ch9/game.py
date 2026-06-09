import random

def game():
    score=random.randint(1,100)
    print("You scored",score)
    with open("ch9/hiscore.txt") as f:    #by using 'with' you dont need to close the file after use as with does it automatically for you
        hiscore=f.read()
        if hiscore=="":
            hiscore=0
        else:
            hiscore=int(hiscore)

    if score>hiscore:
        print("Congrats! You got the highest score!")
        with open("ch9/hiscore.txt","w") as f:
            f.write(str(score))
    else:
        print("You did not beat the highest score of",hiscore)

game()
