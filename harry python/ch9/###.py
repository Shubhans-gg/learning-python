with open("ch9/donkey.txt") as p:
    content=p.read()

with open("ch9/donkey.txt","w") as f:
    content=content.replace("donkey","d####y")
    f.write(content)

