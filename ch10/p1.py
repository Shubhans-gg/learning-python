class student:
    def __init__(self,name,a,b,c):
        self.name=name
        self.maths=a
        self.physics=b
        self.chem=c
    
    def avg(self,a,b,c):
        print("The average is",(a+b+c)/3)

s1=student("Shubhans", 95, 82, 78)
print(s1.name, s1.maths,s1.physics,s1.chem)
s1.avg(s1.maths,s1.physics,s1.chem)
        