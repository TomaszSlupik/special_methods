#  __repr__
class Person ():
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(fname='{self.fname}', lname='{self.lname}')"
    
person = Person('Mike', 'Smith')

print (person)

print ("----")

# __str__
class Man():
    def __init__(self, first_name, last_name) -> None:
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self,):
        return f"First name: {self.first_name}\nLast name: {self.last_name}"

man = Man("John", "Doe")
print (man)

print ("----")

# *args - dowolna liczba argumentów i metoda __repr__ do wyświetlenia obiektu - formalna
# __str__ - nieformalna reprezentacja obiekt
class Vector ():
    def __init__(self, *components) -> None:
        self._components = components

    def __repr__(self) -> str:
        return f"Vector{self._components}"


v1 = Vector(-3, 4, 2)
print (v1)

print ("----")

# __len__ 
class LengthOfTheSide:
    def __init__(self, *args) -> None:
        self.args = args

    def __len__ (self):
        return len(self.args)
    
length_of_the_side = LengthOfTheSide(2, 3, 1, 1)
print(f"Liczba długości boków: {len(length_of_the_side)}")
