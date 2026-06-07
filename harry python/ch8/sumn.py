def sum(n):
    if n==1:
        return 1
    return sum(n-1)+n

n=int(input("Enter upto which number you want to get their sum: "))
print(f"The sum of first {n} natural numbers is {sum(n)}")
