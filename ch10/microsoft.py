class Programmer:
    company= "Microsoft"
    def __init__(self, name, salary, department):  #__init__ function is always present in a class.even if you dont create it python automatically creates it(by default they just have 'pass' inside them)
                                                  #it always gets executed first when a class is called
        self.name = name
        self.salary = salary
        self.department= department
        print("Hello")

p1= Programmer("Shubh", 100000, "AI")
print(p1.name, p1.salary, p1.department)
p2= Programmer("Shivam", 90000, "Web Development")
print(p2.name, p2.salary, p2.department)

