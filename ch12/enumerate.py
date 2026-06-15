s = ["Harry", "Marry", "Carry"]

#enumerate is used when you want both the index and the value while looping through a list

for index, value in enumerate(s):
    print(index, value)

#You can also change the starting index:
for index, value in enumerate(s, start=1):
    print(index, value)

#finding position of an item:
for index, value in enumerate(s):
    if value == "Marry":
        print(f"Marry is at position {index}")