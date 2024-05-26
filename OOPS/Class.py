#creating class
class Student:
    name = "dipali chavai"

#creating object(instance)
s1 = Student()
print(s1.name)

# constructor 
class Company:
    # default constructor
    def __init__(self):
        pass

    # parameterizd constuctor
    def __init__(self,name,salary):
        # print(self)
        self.name = name
        self.salary = salary
        print("Adding new employee in database:")

    # methods
    def welcome(self):
        print("welcome employee,",self.name)

    def get_salary(self):
        return self.salary
           
s1 = Company('samu',30000)
# print(s1.name, s1.salary)
s1.welcome()
print(s1.get_salary())

s2 = Company('manu',25000)
print(s2.name, s2.salary)


# practice question - Create student class that takes name and marks of 3 subjects as arguments in constructor.
# Then create a method to print the average.

class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def get_avg_marks(self):
        sum = 0
        for val in self.marks:
            sum += val
        print('Hi',self.name, "your avg score is:",sum/3)


s1 = Student("ajay",[67,89,70])
s1.get_avg_marks()

s1.name = "rohan"
s1.get_avg_marks()


# practice question - Create account class with 2 attributes- balance and account no.
# Create methods for debit, credita and printing the balance.

class Account:
    def __init__(self, balance, acc_no):
        self.balance = balance
        self.account_number = acc_no

    def debit(self,amount):
        self.balance -= amount
        print("Rs",amount,"was debited")
        print("Total balance is",self.get_balance())

    def credit(self,amount):
        self.balance += amount
        print("Rs",amount,"was credited")
        print("Total balance is",self.get_balance())


    def get_balance(self):
        return self.balance
    
acc1 = Account(10000,12345)
acc1.debit(3000)
acc1.credit(5000)


