class Cat:
    def __init__(self, name = None, age = None, color = None, iseat = False):
        self.Name = name
        self.Age = age
        self.Color = color
        self.Iseat = iseat
    def __str__(self):
        return f"\nName: {self.Name}\n"\
               f"Age: {self.Age}\n"\
               f"Color: {self.Color}\n"

