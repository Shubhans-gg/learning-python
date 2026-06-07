s=set()
s.add(18)
s.add("18")
print(s)

b=set()
b.add(20)
b.add(20.0)
b.add("20")
print(b)
print(len(b))  
#len=2 because it treats 20==20.0

