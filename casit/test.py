import copy
import os

class MyClass():
    def __init__(self):
        pass

if __name__ == "__main__":
    a = MyClass()
    print(dir(a.__module__.__reduce__))
    b = copy.copy(a)
    print(help(a.__module__.__reduce__))
