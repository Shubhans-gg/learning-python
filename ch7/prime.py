i=int(input("Enter a number: "))
n=2
while n<i:
    if i%n==0:
        print("not a prime no")
        break
    n=n+1
else:
    print("It's a prime no")
    

