class Employee:
    def __init__(self, name, salary=10000):
        self.name = name
        self.salary = salary

    def work(self, *args, **kwargs):
        print(self.name + "is working")
