
class Employee:

    raise_amount = 1.04     #class variable
    num_emps = 0

    def __init__(self, first, last, pay):
        self.first = first  # same with this [emp_1.first = "Kim"]
        self.last = last
        self.pay = pay
        self.email = first+"."+"@bla.com"

        Employee.num_emps += 1

    def fullname(self):     #all method get instance as first argument
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)
        self.pay = int(self.pay * self.raise_amount)



emp_1 = Employee("Kim", "yonghee",5000)     #this line __init__ automatically
emp_2 = Employee("Test","User",500000000)

print(emp_1.__dict__)
print(Employee.__dict__)
#instance don't have constant variable "raise_amount"

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
#but they can get from class -> 상속

Employee.raise_amount = 1.05

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
#all values changed


emp_1.raise_amount = 2.0
print(emp_1.__dict__)
#if overrice class variable instance have namespace of it

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)


print(Employee.num_emps)
emp_3 = Employee("Test","User",500000000)
print(Employee.num_emps)


