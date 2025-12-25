class Parrot:
    # instance attribute
    def __init__(self, nm, h):
        self.name = nm
        self.age = h

    def sing(self, song):  # method 1
        return f"{self.name} sings {song}"
    
    def dance(self):  # method 2
        return f"{self.name} is now dancing"
    
# instantiate the Parrot class
blu = Parrot("Blue", 10)

# call the instance methods
print(blu.sing("'Happy'"))
print(blu.dance())