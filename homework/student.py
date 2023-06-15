#успадкування - створення нового обєкту на основі уже існуючого.
from human import Human
class Student(Human):
    def __init__(self, name=None, age=0.0, gender=None, height=0, group=None, grade=0.0, subject=None):
        super().__init__(name, age, gender, height)
        self.Group = group
        self.Grade = grade
        self.Subject = subject
    def __str__(self):
        return f"{super().__str__()}\n" \
               f"Group - {self.Group}\n" \
               f"Grade - {self.Grade}\n" \
               f"Subject - {self.Subject}"