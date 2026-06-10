class person:
    name="anonymous"

    # changes name across all the objects inside the class
    @classmethod
    def change_name1(cls,name):
        cls.name=name  

    #changes the name for the specific object only
    # def change_name2(self,name):
    #     self.name=name
    
s1=person()
s2=person()
s1.change_name1("Shubh")
print(s1.name)
print(s2.name)