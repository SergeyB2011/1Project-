class Calculate:

    def Divider(self, a, b):
        if a < b:
            raise ValueError("a<b")
        if b > 100:
            raise IndexError("b>100")
        return a / b


