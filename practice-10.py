class Employee:
    '所有员工基类'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name, " Salary : ", self.salary)


emp1 = Employee("Zara", 2000)

emp2 = Employee("Min", 5000)

emp1.displayCount()
emp1.displayEmployee()

emp2.displayCount()
emp2.displayEmployee()

print('--------------------------')

print(Employee.__doc__)
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__bases__)
print(Employee.__dict__)
