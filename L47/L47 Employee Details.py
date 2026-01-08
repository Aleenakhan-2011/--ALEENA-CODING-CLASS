# parent class
class Person:
    #__init__ is known as the constructor
    def __init__(self, nm, id):
        self.name = nm
        self.idnumber = id

    def display(self):
        print("Name :", self.name)
        print("ID Number :", self.idnumber)

# child class
class Employee(Person):
    def __init__(self, nam, idnum, salary, pos):
        self.salary = salary
        self.position = pos

        # invoking the __init__ of the parent class
        Person.__init__(self, nam, idnum)


#creation of an object variable or an instance
a = Employee("John", 886012, 200000, "Intern")

# calling a function of the class person using its instance
a.display()
print()