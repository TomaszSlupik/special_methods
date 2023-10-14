#  __repr__
class Person ():
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(fname='{self.fname}', lname='{self.lname}')"
    
person = Person('Mike', 'Smith')

print (person)

# 
