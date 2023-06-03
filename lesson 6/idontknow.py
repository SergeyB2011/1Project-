from buildingerror import BuildingError
class Validation:
    def Check(self, amount, limit):
        if(amount > limit):
            raise BuildingError(amount, limit)
        return True
