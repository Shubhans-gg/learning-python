n=int(input("Enter upto which number you want to get their sum: "))
#To find sum of first n natural numbers
i=1
sum=0
while i<=n:
    sum=sum+i
    i=i+1

print("The sum of first",n,"natural numbers is:",sum)   

#To find factorial of a number n
j=1
fact=1
while j<=n:
    fact=fact*j
    j=j+1
print("The factorial of",n,"is:",fact)
