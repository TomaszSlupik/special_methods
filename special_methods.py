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

# __mul__

class MulNumber():
    def __init__(self, *args):
        self.args = args

    def __mul__(self, numbers):
        finallMul = tuple(x * y for x, y in zip(self.args, numbers.args))
        return finallMul
    
    def __str__(self):
        return {self.args}
    
oneMul = MulNumber(4, 2)
twoMul = MulNumber(-1, 3)
print (oneMul * twoMul)

print ("----")

# __truediv__
class TrueDivNumber():
    def __init__(self, *args):
        self.args = args

    def __truediv__(self, numbers):
        truediv = tuple(x / y for x, y in zip(self.args, numbers.args))
        return truediv

    def __str__(self) -> str:
        return self.args
    
oneTrueDiv = TrueDivNumber(4, 2)
twoTrueDiv = TrueDivNumber(-1, 4)
print(oneTrueDiv / twoTrueDiv)

print ("----")

# __floordiv__
class NumberTotal ():
    def __init__(self, *args):
        self.args = args

    def __floordiv__(self, number):
        floorNumber = tuple(x // y for x,y in zip(self.args, number.args))
        return floorNumber

    def __str__(self):
        return {self.args}
    
firstTotal = NumberTotal(4, 2)
secondTotal = NumberTotal(-1, 4)

print(firstTotal // secondTotal)


print ("----")

# dodawanie stringów 
class Doc:
    def __init__(self, string) -> None:
        self.string = string

    def __repr__(self) -> str:
        return f"Doc(string='{self.string}')"
    
    def __str__(self) -> str:
        return f"{self.string}"
    
    def __add__(self, added):
        if isinstance(added, Doc):
            return Doc (self.string + ' ' + added.string)
        else:
            raise TypeError("Możesz tylko dodać obiekty w klasie Doc")
    
doc1 = Doc('Python')
doc2 = Doc('3.8')

print(doc1 + doc2)

print ("----")
     

# 
class Hashtag:
    def __init__(self, string):
        self.string = string

    def __str__(self) -> str:
        return f"#{self.string}"
    
    def __add__(self, addHash):
        if isinstance(addHash, Hashtag):
            return Hashtag(self.string+ ' ' + '#'+ addHash.string)
    

hash1 = Hashtag('python')
hash2 = Hashtag('developer')
hash3 = Hashtag('oop')

print (hash1 + hash2 + hash3)
    
print ("----")

# __eq__
class CheckString ():
    def __init__(self, string) -> None:
        self.string = string

    def __str__(self) -> str:
        return {self.string}
    
    def __eq__(self, other) -> bool:
        if isinstance(other, CheckString):
            return self.string == other.string
        return False

oneCheck = CheckString('Python')
twoCheck = CheckString('3.8')

print (oneCheck ==  twoCheck)

print ("----")

# __lt__

class WhatBigger():
    def __init__(self, value):
        self.value = value
    
    def __repr__(self) -> str:
        return str(self.value)
    
    def __lt__(self):
        return len(self.value)
    
oneWhatBigger = WhatBigger('sport')
twoWhatBigger = WhatBigger('activity')

print (len(oneWhatBigger.value) < len(twoWhatBigger.value))

print ("----")

# __iadd__
class Gluing ():
    def __init__(self, string):
        self.string = string

    def __iadd__(self, addValue):
        finall = (self.string) +" & " + (addValue.string)
        return finall
    
    def __repr__(self) -> str:
        return f"{self.string}"
    
gluOne = Gluing('sport')
gluTwo = Gluing('activity')

gluOne += gluTwo
print (gluOne)

print ("----")

# __str__
import uuid
class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author

    @staticmethod
    def get_id():
        return str(uuid.uuid4().fields[-1])[:6]
    
    def __str__(self):
        return f"Book ID: {book.get_id()} | Title: {self.title} | Author {self.author}"
    
book = Book('The Lord of the Rings', 'J.R.R. Tolkien')
print (book)
    
print ("----")

# mro()
class Food ():
    def __init__ (self, quantity):
        self.quantity =  quantity

class Fish:
    def __init__(self, brand):
        self.brand = brand

class Macronutrients(Food, Fish):
    def __init__(self, protein, quantity, brand):
        Food.__init__(quantity)
        Fish.__init__(brand)
        self.protein = protein

print (Macronutrients.mro())

print ("----")