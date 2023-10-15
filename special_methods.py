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

print ("----")

# __bool__ 
class CheckNumber:
    def __init__(self, *args) -> None:
        self.args = args

    def __bool__ (self):
        if not self.args:  
            return False
        if self.args[0] == 0:
            return False
        elif self.args == "":
            return False
        else:
            return True

v1 = CheckNumber()

v2 = CheckNumber(3, 2)

v3 = CheckNumber(0, -3, 2)

v4 = CheckNumber(5, 0, -1)

for check in [v1, v2, v3, v4]:
    print(bool(check))

print ("----")

# __add__
class AddNumber():
    def __init__(self, *args) -> None:
        self.args = args

    def __add__(self, numbers):
        args = tuple(x + y for x, y in zip(self.args, numbers.args))
        return AddNumber(*args)
    
    def __str__(self) -> str:
        return f"Wynik dodawanie tupli: {self.args}"

firstNumber = AddNumber(4, 2)
secondNumber = AddNumber(-1, 3)

print(firstNumber.__add__(secondNumber))

print ("----")

# Try except 
class TestVector ():
    def __init__(self, *value) -> None:
        self.value = value
    

vectorOne = TestVector(1, 3)
vectorTwo = TestVector(2, 2)

try:
    vectorOne + vectorTwo
except TypeError as error:
    print(f'Błąd, nie możesz dodać liczb ${error}')


print ("----")

# __sub__
class SubNumber():
    def __init__(self, *args) -> None:
        self.args = args

    def __sub__(self, numbers):
        finallSub = tuple(x - y for x,y in zip(self.args, numbers.args))
        return finallSub

    def __str__(self) -> str:
        return {self.args}
    
oneSub = SubNumber(4, 2)
twoSub = SubNumber(-1, 3)

print(oneSub - twoSub)

print ("----")