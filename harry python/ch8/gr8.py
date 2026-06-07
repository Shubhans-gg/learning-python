def gr8(a,b,c):
    if a>b and a>c:
        return a 
    elif b>a and b>c:
        return b    
    else:
        return c
    
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))   
c=int(input("Enter third number: "))

print("The greatest of the 3 nos is", gr8(a,b,c))

print("a")
print("b")
print("c", end="")
print("d", end=" ")
print("e")
print(a)