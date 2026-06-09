class A:
    varA="you are in class A"

class B:
    varB="you are in class B"

class C(A,B):
    varC="you are in class C"

s1=C()
print(s1.varC)
print(s1.varB)
print(s1.varA)
