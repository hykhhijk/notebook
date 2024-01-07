
class Employee:
    pass

emp_1 = Employee()
emp_2 = Employee()

print(emp_1)    
print(emp_2)    #different memory loaction

emp_1.first = "Kim"
emp_1.last = "Yonghee"
emp_1.email = "Kim@bla.com"
emp_1.ply = 5000

emp_2.first = "Test"
emp_2.last = "User"
emp_2.email = "Testuser@bla.com"
emp_2.ply = 500000

print(emp_1.email)
print(emp_2.email)
#이러한 방식도 기존 클래스 생성과 똑같이 작동하지만 비효율적


class Employee:
    def __init__(self, first, last, pay):
        self.first = first  # same with this [emp_1.first = "Kim"]
        self.last = last
        self.pay = pay
        self.email = first+"."+"@bla.com"

    def fullname(self):     #all method get instance as first argument
        return "{} {}".format(self.first, self.last)


emp_1 = Employee("Kim", "yonghee",5000)     #this line __init__ automatically
emp_2 = Employee("Test","User",500000000)

print(emp_1.email)
print(emp_2.email)

print("{} {}".format(emp_1.first, emp_1.last))
print(emp_1.fullname())
print(Employee.fullname(emp_1))     #input self argument as emp_1