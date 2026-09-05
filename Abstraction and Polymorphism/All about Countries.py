class India():
    def capital(self):
        print("New Delhi is the capital of India.")
    def language(self):
        print("Hindi is the most widely spoken Language of India.")  
    def currency(self):
        print("Indian Rupee is the currency of India.")  

class Nepal():
    def capital(self):
        print("Kathmandu is the capital of Nepal.")
    def language(self):
        print("Nepali is the most widely spoken Language of Nepal.")  
    def currency(self):
        print("Nepal Rupee is the currency of Nepal.")     

obj1 = India()
obj2 = Nepal()

for i in (obj1, obj2):
    i.capital()
    i.language()
    i.currency()