class complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img

    def show(self):
        print(self.real,"+",self.img,"i")

    # hard way
    # def sum(n1,n2):

    #easier way(using dunder method)
    def __add__(n1,n2):
        sum_real=n1.real+n2.real
        sum_img=n1.img+n2.img
        return complex(sum_real,sum_img)

n1=complex(2,3) 
n1.show()  
n2=complex(5,6)
n2.show()
n3 = n1.sum(n2)    # old way
n3=n1+n2    #new way
n3.show()