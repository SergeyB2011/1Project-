class BuildingError(Exception):
    def __init__(self, amount = 0, limit = 0 ):
        self.Amount = amount
        self.Limit = limit
    def __str__(self):
        return f"Amount: {self.Amount} is greater than limit: {self.Limit}"

