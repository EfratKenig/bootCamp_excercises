from Employee import Employee


class Cleaner(Employee):
    def __init__(self, name, salary=10000):
        super().__init__(name, salary)

    def work(self):
        print(self.name + " is cleaning")
