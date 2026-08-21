class IOstring():
    def __int__(self,string):
        self.str1 = "" 

    def get_string(self):
        self.str1= input("Enter string: ")

    def print_string(self):
        print("Result is: " , self.str1.lower())

str1 = IOstring()

str1.get_string()
str1.print_string()

