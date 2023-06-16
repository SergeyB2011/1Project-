from colorama import Fore, Back, Style, Cursor
fore = Fore.BLACK
if(fore == Fore.RED):
    print("red")
elif(fore == Fore.YELLOW):
    print("yellow")
elif(fore == Fore.BLACK):
    print("black")
else:
    print(fore.__str__())
    print(fore.title())
#1.метод fore з бібліотеки colorama дає доступ до переліку змінних які зберегають значення про кольори в AnsiCodes.
#2.метод back з бібліотеки colorama тей саме щой fore тільки це для задньоого фона.
#3.метод Style з бібліотеки colorama за допомогою нього ви можете редагувати текст наприклад зробити нахилині літер.
#4.метод Cursor з бібліотеки colorama управляє переміщенням курсора в сторону яку було вказано у коді наприклад forward 50