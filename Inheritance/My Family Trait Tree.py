class FamilyMember:
    def __init__(self, eye_color, hair_color):
        self.eye_color= eye_color
        self.hair_color= hair_color
    def show_traits(self):
        print("Eye color: ",self.eye_color)
        print("Hair color: ",self.hair_color)    

class child(FamilyMember):
    def __init__(self, name,age,eye_color, hair_color):
        self.name=name
        self.age=age
        FamilyMember.__init__(self, eye_color, hair_color)

    def show_traits(self):
        print("Name is: ",self.name)
        print("Age is: ",self.age)
        super().show_traits()   
    def hobby(self, hobby):
        print(self.name, "likes", hobby)

object= child("Rohit",14, "brown", "Blonde")
object.show_traits()
object.hobby("Painting")

print("Is kid a subclass of the FamilyMember? ", issubclass(child, FamilyMember))