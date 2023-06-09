from cat import Cat
class Muska:
    def __init__(self):
        self.CatsEat = list()
        self.CatsNoEat = list()
    def AddCat(self, cat = Cat()):
        if(cat.Iseat == True):
            self.CatsEat.append(cat)
        if (cat.Iseat == False):
            self.CatsNoEat.append(cat)
    def ToStringCat(self, cat = Cat()):
        if (cat.Iseat == True):
            print(f"cat {cat.__str__()}today will eat:) ")
        if (cat.Iseat == False):
            print(f"cat {cat.__str__()}today will not eat:( ")