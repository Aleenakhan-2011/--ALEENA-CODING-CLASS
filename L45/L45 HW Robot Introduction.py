class Robot:

    # class static attribute
    species = "robot"

    # instance attribute
    def __init__(self, nm, co):
        self.name = nm
        self.country = co

    def introduction(self):  
        print("Hi, I am a", self.species)

    def details(self):
        print("My name is", self.name)
        print("I am from", self.country)

jarvis = Robot("Jarvis", "USA")
metro = Robot("Metro", "UK")

jarvis.introduction()
jarvis.details()
print()

metro.introduction()
metro.details() 
