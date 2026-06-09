n1=int(input("Enter first number: "))
n2=int(input("Enter second number: "))
n3=int(input("Enter third number: "))
n4=int(input("Enter fourth number: "))

if n1>n2 and n1>n3 and n1>n4:
    print(n1,"is the largest no")
elif n2>n1 and n2>n3 and n2>n4:
    print(n2,"is the largest no")
elif n3>n1 and n3>n2 and n3>n4:
    print(n3,"is the largest no")
else:
    print(n4,"is the largest no")

print("Thank you")