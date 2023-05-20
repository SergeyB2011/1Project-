class Student:
    def __init__(self, name, age, group):
        self.Name = name
        self.Age = age
        self.Group = group
    def ShowInfo(self):
        print(f"Name: {self.Name}\n"
            f"Age: {self.Age}\n"
            f"Group: {self.Group}")