import math

class circle:
    def __init__(self,radius):
        self.radius=radius
    
    def area(self):
        return math.pi*self.radius*self.radius
    
    def peri(self):
        return 2*math.pi*self.radius

radius=int(input("Enter the radius of the circle:"))
c1=circle(radius)
print("The area of the circle is", c1.area())
print("The circumference of the circle is",c1.peri())