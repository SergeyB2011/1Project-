class Box:
    def __init__(self, width = None, height = None):
        self.Width = width
        self.Height = height
    def __str__(self):
        return f"Width = {self.Width}\n" \
        f"Height = {self.Height}"
