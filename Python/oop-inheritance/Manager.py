from Clerk import Clerk
from Employee import Employee


class Manager(Employee):
    def __init__(self, employees, name, salary=20000):
        super().__init__(name, salary)
        self.employees = employees

    def hire_employee(self, name):
        """ A function that adds s a new clerk """
        new_employee = Clerk(name, [])
        self.employees.append(new_employee)

    def work(self, office):
        """ make all the employees work """
        for emp in self.employees:
            if isinstance(emp, Clerk):
                emp.work(office)
            else:
                emp.work()
