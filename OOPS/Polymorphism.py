# polymorphism
class India:
    
    def language(self):
        print('Hindi is widely spoken language in India')
        
    def capital(self):
        print('Capital of India is New Delhi')


class USA:
    
    def language(self):
        print('English is widely spoken language in USA')
    
    def capital(self):
        print('Capital of USA is Washington D.C.')

c1 = India()
c2 = USA()
for i in [c1,c2]:
    print(type(i))
    i.capital()
    i.language()
    print('\n==============================\n')


# practice question - calculating area of different shapes
class Rectangle:
    
    def __init__(self,w,h):
        self.w = w
        self.h = h
        
    def area(self):
        ar = (self.w*self.h)
        return ar
    

class Circle:
    def __init__(self,rad):
        self.rad = rad
        
    def area(self):
        ar = 3.14*(self.rad**2)
        return ar
    
r1 = Rectangle(7,8)
c1 = Circle(5)
for i in [r1,c1]:
    print(type(i))
    print(f'Area of given object is : {i.area():.4f}')
    print('\n========================\n')