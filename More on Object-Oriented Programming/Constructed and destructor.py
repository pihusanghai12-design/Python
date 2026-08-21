class Employees:

    def __init__(self):
        print("Constructor created: Employee object created.")

    def __del__(self):
        print("Destructor created: Employee object deleted.")

def create_obj():
    print("making object...")
    obj= Employees()
    del obj

print("Object created and then deleted.")    


