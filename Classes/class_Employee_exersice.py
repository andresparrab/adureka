#Employee class
class Employee(object):
      def __init__(self, name):
        self.name = name

      def greet(self, other):
        print("Hello, %s" % other.name)

      def calculate_wage(self, hours):
          self.hours = hours
          return hours * 200.00

class PartTimeEmployee(Employee):
      def calculate_wage(self,hours):
          self.hours = hours
          return  hours * 100.00

#Get the calculate_wage method from Employee parent(super)class and add it to ParTimeEmployee
      def full_time_wage(self, hours):
          return super(PartTimeEmployee, self).calculate_wage(hours)

class CEO(Employee):
      def greet(self, other):
        print("Get back to work, %s!" % other.name)

ceo = CEO("Emily")
emp = Employee("Steve")
part = PartTimeEmployee('Niklas')
emp.greet(ceo)
# Hello, Emily
ceo.greet(emp)
# Get back to work, Steve!

print(emp.calculate_wage(10),' kr')
print(part.calculate_wage(10),' kr')
print(part.full_time_wage(10))