class parent:
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def calcualate(self):
        print ( self.l * self.b)

class child(parent):
    pass

a=parent(2,3)
a.calcualate()
