def rem(s, word):
    n=[]  #this creates a new list
    for item in s:  #this checks for each item in the list
        if word in item:
            n.append(item.replace(word, ""))    #what append does is it adds the item to the list
                                                #while replace replaces the word with the given word(nothing in this case)
        else:
            n.append(item)       #as here the word is not found it simply adds the item to the list
    return n    #returns the new list

s=["Harry", "Marry", "Carry", "Shubh"]
word=input("Enter your stripper: ")
print(rem(s, word))      #calls the function and prints the returned list