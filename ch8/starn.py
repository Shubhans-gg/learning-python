def star(n):
    if n==0:
        return
    print("*"*n)
    star(n-1)

n=int(input("Enter the number of rows: "))
star(n)

#Not Recursion
def inch_to_cm(m):
    return m*2.54

m = int(input("Enter the value in inches: "))
print(f"The value in cm is: {inch_to_cm(m)} cm")

#By recursion
def inch(m):
    if (m==0):
        return 0
    return inch(m-1)+2.54

print(f"The value in cm is: {inch(m)} cm")