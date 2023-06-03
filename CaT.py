class Cat:
    def __init__(self,name = None,age = None,color = None,role = None):
        self.Name = name
        self.Age = age
        self.Color = color
        self.Role = role
    def ShowInfo(self):
        print(f"Name: {self.Name}\n"
            f"Age: {self.Age}\n"
            f"Color: {self.Color}\n")

