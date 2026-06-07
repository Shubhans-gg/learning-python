class Programmer:
    company= "Microsoft"
    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department= department

p1= Programmer("Shubh", 100000, "AI")
print(p1.name, p1.salary, p1.department)
p2= Programmer("Shivam", 90000, "Web Development")
print(p2.name, p2.salary, p2.department)

