from CaT import Cat
class muska:
    def __init__(self,eat):
        self.Eat = eat
        self.cats = list()
        self.catout = list()
    def addcat(self,cat = Cat()):
        if(cat.Role == 2):
            self.cats.append(cat.Name)
    def catuot(self,cat = Cat()):
        if(cat.Role == 1):
            self.catout.append(cat.Name)
    def catoutofmuska(self,cat = Cat()):
        print(f"")

