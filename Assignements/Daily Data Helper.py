class DailyHelper:
    def __init__(self):
        self.message= ""
    def get_message(self):
        self.message =input("Enter your daily message: ")
    def print_message(self):
        print("Message in Uppercase: ", self.message.upper())      

daily_text=DailyHelper()    
daily_text.get_message()
daily_text.print_message()

class HelperSession:
    def __init__(self):
        print("Helper session created")
    def __del__(self):
        print("Helper session deleted.")

def create_session():
    session = HelperSession()
    return session

print("")
print("Calling create_session() function...")
session_obj = create_session()
print("Program is running...")

class Pairfinder:
     
    def find_pair(self, numbers, target):
        lookup = {}
 
        # enumerate() gives both index and value
        for index, number in enumerate(numbers):
            needed_number = target - number
 
            if needed_number in lookup:
                return (lookup[needed_number], index)
 
            lookup[number] = index
 
        return None
 
 

numbers = (10, 20, 30, 40, 50, 60, 70)
 
target_value = int(input("Enter target sum to search: "))
 
result = Pairfinder().find_pair(numbers, target_value)
 
if result is not None:
    print("index1=%d, index2=%d" % result)
else:
    print("No matching pair found.")
 

del session_obj
print("Program End")









        


