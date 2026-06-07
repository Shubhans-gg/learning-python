s1=int(input("Enter marks in maths: "))
s2=int(input("Enter marks in science: "))
s3=int(input("Enter marks in english: "))

if s1>=33 and s2>=33 and s3>=33 and (s1+s2+s3)/3>=40:
    print("You have passed the exam")
    print("Congratulations!")

else:
    print("You have failed the exam")
    print("Better luck next time!")

print("Thank you")  