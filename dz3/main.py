from cat import Cat
from muska import Muska
cats = list()
muska = Muska()
samelukmukuta = Cat("SamelukMukuta", 3 , "black")
dimakuligin = Cat("DimaKuligin", 2 , "white")
andriiprymenko = Cat("AndriiPrymenko", 5 , "brown", True)
sergiibihun = Cat("SergiiBihun", 4 , "black", True)
cats.append(samelukmukuta)
cats.append(andriiprymenko)
cats.append(dimakuligin)
cats.append(sergiibihun)
for i in cats:
    muska.AddCat(i)
    muska.ToStringCat(i)