from box import Box
from calculatesquare import CalculateSquare
class ColorBox(Box, CalculateSquare):
    def __init__(self, width = None, height = None, color = None):
        super().__init__(width, height)
        self.Color = color
    def __str__(self):
        return f"{super().__str__()}\n" \
        f"Color: {self.Color}\n" \
        f"Square = {self.Calculate(self.Width, self.Height)}"