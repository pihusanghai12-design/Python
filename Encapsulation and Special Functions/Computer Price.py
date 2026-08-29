class Computer:
    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: ",self.__maxprice)

    #Setter Method
    def setMaxPrice(self, price):
        self.__maxprice= price

c= Computer()
c.sell() #Shows 900

c.setMaxPrice(1000) #Updating the value of the private variable
c.sell()  #This will show 1000