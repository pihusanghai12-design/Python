from abc import ABC, abstractmethod
class AbstractClass(ABC):
    def print(self,x):
        print("Passed value is: ",x)

        @abstractmethod         #This part is ignored in the output as it is an abstract method
        def task(self):
            print("We are inside abstract task")

class testClass(AbstractClass):
    def task(self):
               print("We are inside test class.")

obj = testClass()
obj.task()
obj.print(20)
