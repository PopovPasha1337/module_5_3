class House:
    def init(self, name, floors):
        self.name = name
        self.floors = floors

    def str(self):
        return f"Название: {self.name}, кол-во этажей: {self.floors}"

    def eq(self, other):
        if isinstance(other, House):
            return self.floors == other.floors
        elif isinstance(other, int):
            return self.floors == other
        else:
            return NotImplemented

    def lt(self, other):
        if isinstance(other, House):
            return self.floors < other.floors
        elif isinstance(other, int):
            return self.floors < other
        else:
            return NotImplemented

    def le(self, other):
        if isinstance(other, House):
            return self.floors <= other.floors
        elif isinstance(other, int):
            return self.floors <= other
        else:
            return NotImplemented

    def gt(self, other):
        if isinstance(other, House):
            return self.floors > other.floors
        elif isinstance(other, int):
            return self.floors > other
        else:
            return NotImplemented

    def ge(self, other):
        if isinstance(other, House):
            return self.floors >= other.floors
        elif isinstance(other, int):
            return self.floors >= other
        else:
            return NotImplemented

    def ne(self, other):
        if isinstance(other, House):
            return self.floors != other.floors
        elif isinstance(other, int):
            return self.floors != other
        else:
            return NotImplemented

    def add(self, value):
        if isinstance(value, int):
            return House(self.name, self.floors + value)
        else:
            return NotImplemented

    def radd(self, value):
        return self.add(value)

    def iadd(self, value):
        if isinstance(value, int):
            self.floors += value
            return self
        else:
            return NotImplemented


h1 = House('Жк Эльбрус', 10)
h2 = House('Жк Акация', 20)

print(h1)
print(h2)

print(h1 == h2)  # False

h1 = h1 + 10
print(h1)
print(h1 == h2)  # True

h1 += 10
print(h1)

h2 = 10 + h2
print(h2)

print(h1 > h2)
print(h1 >= h2)
print(h1 < h2)
print(h1 <= h2)
print(h1 != h2)