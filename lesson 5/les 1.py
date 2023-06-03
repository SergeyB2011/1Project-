import random
import requests
#help(requests)
'''
import requests
r = requests.get('https://www.python.org')
#print(r.content)
payload = dict(key1='Student', key2='Sergii')
r = requests.post('https://httpbin.org/post', data=payload)
print(r.text)
'''
'''
print(type(requests.Request))
print(dir(requests.Request))
print(dir(requests))
students = list()
for method in dir(students):
print(method)
'''

name = "Ippial"
print(hasattr(name, "index"))
print(name.index("l", 0, 6))

name = "Ippial"
print(hasattr(name, "index"))
print(getattr(name, "startswith"))
print(callable(name))
print(f'Is method requests.get callable?: {callable(requests.get)}')