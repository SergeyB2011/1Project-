from box import Box
from colorbox import ColorBox
box = Box(10, 5)
print(f"Base class:\n{box.__str__()}")
cBox = ColorBox(box.Width, box.Height, "Green")
print(f"Derived class:\n{cBox.__str__()}")