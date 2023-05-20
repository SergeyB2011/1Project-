class Human:
    def __init__(self,name = None,role = None):
        self.Name = name
        self.Role = role

    def __str__(self):
        return f"Name: {self.Name}"