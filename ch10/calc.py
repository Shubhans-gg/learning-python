a=int(input("Enter a number: "))

class calculator:
    def __init__(self,a):
            self.a=a
    def square(self):
         return self.a**2
    def cube(self):
        return self.a**3
    def sqrt(self):
        return self.a**0.5
    
    @staticmethod
    def hello():
         print("Hello, I am a static method. I don't have access to instance variables or methods.")

damn=calculator(a)
calculator.hello()
print(damn.square(),damn.cube(),damn.sqrt())         
    