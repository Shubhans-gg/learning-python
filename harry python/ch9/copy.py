# with open("ch9/donkey.txt") as p:
#     content=p.read()

# with open("ch9/copy.txt","w") as f:
#     f.write(content)

with open("ch9/donkey.txt") as p:
    c1=p.read()
with open("ch9/copy.txt") as f:
    c2=f.read()

if c1==c2:
    print("The contents of both files are identical.")
else:
    print("They are not identical.")