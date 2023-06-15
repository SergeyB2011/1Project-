from tennis import Tennis
from student import Student
class Son(Student, Tennis):
    def __init__(self, name=None, age=0.0, gender=None, height=0, group=None, grade=0.0, subject=None, skill = None, rang = None):
        super().__init__(name, age, gender, height, group, grade, subject)
        Tennis.__init__(self, skill, rang)
    def __str__(self):
        return f"{super().__str__()}\n" \
               f"{Tennis.__str__(self)}"