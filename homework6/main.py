'''
try:
    your_code
except Exception as ex:
    your_code_handler
'''
from source_code import Calculate
result = []
calculate = Calculate()
try:
    data = {10: 2, 2: 5, "123": 4, 18: 0, 1: 15, 8: 4, 102:101}
    for key in data:
        try:
            res = calculate.Divider(key, data[key])
            result.append(res)
        except ValueError as ve:
            print(ve)
        except IndexError as ie:
            print(ie)
        except ZeroDivisionError as zde:
            print(zde)
        except Exception as ex:
            print(ex)
except TypeError as te:
    print(te)
print(result)