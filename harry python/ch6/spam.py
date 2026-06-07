p1="Make a lot of money fast!!!"
p2="buy now"
p3="limited time offer"
p4="click this"
p5="free free"

msg=input("Enter the message: ")

if p1 in msg or p2 in msg or p3 in msg or p4 in msg or p5 in msg:
    print("This message is spam")
else:
    print("This message is not spam")   


