class Counter:
    def __init__(self, max_number):
        self.I = 0
        self.Max_Number = max_number
    def __iter__(self):
        self.I = 0
        return self
    def __next__(self):
        self.I += 1
        if(self.I > self.Max_Number):
            raise StopIteration
        return self.I