from django.test import TestCase

# Create your tests here.

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  pass

x = Person("Mike", "Olsen")
Y= Student("nay",42)
x.printname()
Y.printname()
