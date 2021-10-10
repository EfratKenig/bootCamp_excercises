class CircleIter():
    def __init__(self, iterable, num):
        self.iterable = iterable
        self.num_of_times = num

    def __iter__(self):
        self.index = 0
        self.times_counter = 0
        return self

    def __next__(self):
        if self.times_counter < self.num_of_times:
            if self.index < len(self.iterable)-1:
                res = self.iterable[self.index]
                self.index += 1
            else:
                res = self.iterable[self.index]
                self.index = 0
            self.times_counter += 1
            return res
        else:
            raise StopIteration


for x in CircleIter([1, 2], 5):
    print(x, end=" ")
print()
