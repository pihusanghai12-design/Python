class MyClass:

    __privateVar= 30

    def __privateMethod(self):
        print("I am inside class MyClass")

    def hello(self):
           print("Private Variable value: ", MyClass.__privateVar)

abc= MyClass()
abc.hello()
abc.__privateVar()