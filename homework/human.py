class Human:
    def __init__(self, name=None, age=0.0, gender=None,height=0):
        self.Name = name
        self.Age=age
        self.Gender = gender
        self.Height=height
    def __str__(self):
        return f"Name - {self.Name}\n" \
               f"Age - {self.Age}\n" \
               f"Gender - {self.Gender}\n" \
               f"Height - {self.Height}"

