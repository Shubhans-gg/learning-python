class car:
    def __init__(self,type):
        self.type=type
    
    @staticmethod
    def start():
        print("The car started...")
    
class Toyota(car):
    def __init__(self,name,type):    
        self.name=name
        super().__init__(type)
        super().start()

c1=Toyota("Fortuner","Petrol")
print(c1.type)
print(c1.name)
print(c1.start)
