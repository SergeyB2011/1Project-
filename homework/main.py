#обєкт - class name_of_object(name_of_base_class):enter+tab
#поведінка - методи def name_of_the_method(list_of_parameters): enter+tab
#стан - атрибути self.Name_of_Attribute = value
#конструктор обєкту - def __init__():enter+tab
from son import Son
sergii = Son("Sergii", 11.11, "male", 150, "S2011", 12, "Pytho OOP", "Beginner", "medium")
print(sergii.__str__())
