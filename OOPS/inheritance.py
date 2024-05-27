# single inheritance
class Car:
    color = 'black'
    @staticmethod
    def start():
        print('car started....')

    @staticmethod
    def stop():
        print('car stopped....')

class ToyotaCar(Car):
    def __init__(self, name):
        self.name = name

car1 = ToyotaCar('fortuner')
car2 = ToyotaCar('prius')
print(car1.name)
print(car2.name)
print(car1.color)

# multilevel inheritance
class Car:
    color = 'black'
    @staticmethod
    def start():
        print('car started....')

    @staticmethod
    def stop():
        print('car stopped....')

class ToyotaCar(Car):
    def __init__(self, name):
        self.name = name

class Fortuner(ToyotaCar):
    def __init__(self,type):
        self.type = type

car1 = Fortuner('diesel')
car1.start()


# multiple inheritance
class A:
    varA = "welcome to class A"

class B:
    varB = "welcome to class B"

class C(A,B):
    varC = "welcome to class C"

c1 = C()
print(c1.varC)
print(c1.varB)
print(c1.varA)

# del keyword
class Student:
    def __init__(self,name):
        self.name = name
    
s1 = Student('sanika')
print(s1.name)
del s1.name
# print(s1.name)



#private attributes and class
class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass

    def reset_pass(self):
        print(self.__acc_pass)

acc1 = Account("12345","abcde")
print(acc1.acc_no)
# print(acc1.__acc_pass)


# example 2
class Person:
    __name = "anonymous"

    def __hello(self):
        print('hello everyone')

    def welcome(self):
        self.__hello()

p1  = Person()
p1.welcome()



# class method
class Person:
    name = 'anonymous'

    @classmethod
    def changename(cls,name):
        cls.name = name

p1 = Person()
p1.changename('rupali')
print(p1.name)
print(Person.name)



# property decorator
class Student:
    def __init__(self,phy,chem,maths):
        self.phy = phy
        self.chem = chem 
        self.maths = maths

    @property
    def percentage(self):
        return str((self.phy+self.chem+self.maths)/3) + "%"
    
stu1 = Student(98,95,90)
print(stu1.percentage)

stu1.phy = 85
print(stu1.percentage)



# dunder method 
class Complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img

    def shownumber(self):
        print(self.real,"i +",self.img,"j")

    def __add__(self,num2):
        newreal = self.real + num2.real
        newimg = self.img + num2.img 
        return Complex(newreal,newimg)
    
num1 = Complex(1,2)
num1.shownumber()

num2 = Complex(3,4)
num2.shownumber()

num3 = num1+num2