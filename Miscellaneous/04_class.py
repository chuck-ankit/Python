class Person:
    def setname(self, name):
        self.name = name

    def getname(self):
        print("Name:", self.name)


class Student(Person):
    def setage(self, age):
        self.age = age

    def getage(self):
        print("Age:", self.age)


s1 = Student()

name = input("Enter name: ")
age = input("Enter age: ")

s1.setname(name)
s1.setage(age)

s1.getname()
s1.getage()
