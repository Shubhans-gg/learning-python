A="*"
n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    print(A*i)


print("ANOTHER ONE")
B=" "

for j in range(1,n+1):
    print(B*(n-j)+A*(2*j-1))


print("AGAIN")
for k in range(1,n+1):
    if k==1 or k==n:
        print(A*n)
    else:
        print(A+ B*(n-2)+A)



