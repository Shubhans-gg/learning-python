class car:
    @staticmethod
    def start():
        print("The car has started...")
    
   
class toyota_car(car):
    def __init__(self,brand):
        self.brand=brand

class fortuner(toyota_car):
    def __init__(self,type):
        self.type=type

c1=fortuner("Electric")
c1.start()

        
