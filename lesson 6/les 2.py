'''
try:
    your_code
except type_of_the_error:
    your_code
'''
'''
while(True):
    try:
        digit1 = int(input("Enter digit1:"))
        digit2 = int(input("Enter digit2:"))
        print(digit1/digit2)
    except Exception as ex:
        yes = input(f"{ex}\n"
                    f"You have to enter digit2 not equal 0!\n"
                    f"Do you want try to continue? Y/N: ")
        if (yes.lower() == "n"):
            break
'''
from buildingerror import BuildingError
from idontknow import Validation
checker = Validation()
try:
    amount=int(input("Enter amount: "))
    limit=int(input("Enter limit: "))
    checker.Check(amount, limit)
    print(10/0)
except BuildingError as be:
    print(f"Custom exception: {be}")
except ValueError as ve:
    print(f"ValueError: {ve}")
except Exception as ex:
    print(f"Standart exception: {ex}")

