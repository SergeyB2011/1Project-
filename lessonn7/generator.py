class Degree:
    def CountDegrees(self, number, max_degree):
        i = 0
        for _ in range(max_degree):
            yield number ** i
            i += 1

            class Checker:
                def Check(self, function):
                    def check(*args, **kwargs):
                        try:
                            result = function(*args, **kwargs)
                        except Exception as ex:
                            print(ex)
                        else:
                            print("No exceptions")

                    return check

                def Calculate(self, expression):
                    return eval(expression)