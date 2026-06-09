class demo:
    a=4
x=demo()
print(x.a) #prints class attrinute as instance attribute is not present
x.a=7 #instance attribute is created
print(x.a) #prints instance attribute as instance attribute is present
print(demo.a) #prints class attribute as instance attribute is not present in class