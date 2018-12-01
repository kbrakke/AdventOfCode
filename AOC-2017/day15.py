# Generator A starts with 289
# Generator B starts with 629

class generator:
    def __init__(self, initial_value, factor, picky = False, picky_multiplier = 0):
        self.factor = factor
        self.previous_value = initial_value
        self.divisor = 2147483647
        self.picky = picky
        self.picky_multiplier = picky_multiplier

    def get_next(self):
        new_value = (self.previous_value * self.factor) % self.divisor
        if self.picky:
            while (new_value % self.picky_multiplier) > 0:
                new_value = (new_value * self.factor) % self.divisor
        self.previous_value = new_value
        return new_value


def compare_lowest(a, b):
    return str(bin(a))[-16:] == str(bin(b))[-16:]

generator_a = generator(289, 16807)
generator_b = generator(629, 48271)

count = 0
for i in range(40000000):
    if compare_lowest(generator_a.get_next(), generator_b.get_next()):
        count += 1

print(count)

generator_a_picky = generator(289, 16807, True, 4)
generator_b_picky = generator(629, 48271, True, 8)

count = 0
for i in range(5000000):
    if compare_lowest(generator_a_picky.get_next(), generator_b_picky.get_next()):
        count += 1

print(count)