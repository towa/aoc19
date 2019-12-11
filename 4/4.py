import functools

class Passwordfinder():
    def __init__(self, start, end):
        self.range = range(start, end)

    def is_six_digit(self, number):
        # check if password is a six digit number
        if number > 999999 or number < 100000:
            return False
        return True

    def get_digits(self, number):
        digits = functools.reduce(lambda x, y: x + list(divmod(x.pop(), y)),
            [[number]]  + [10**(i + 1) for i in range(5)][::-1])
        return digits

    def is_password(self, number):
        if not self.is_six_digit(number):
            return False
        # check if always increasing
        digits = self.get_digits(number)
        pairs = list(zip(digits, digits[1:]))
        descending = [(x,y) for x, y in pairs if x > y]
        if len(descending) > 0:
            return False
        # look for doubles
        doubles = [x for x, y in pairs if x == y]
        if len(doubles) == 0:
            return False
        return doubles

    def is_password_b(self,number):
        doubles = self.is_password(number)
        if not doubles:
            return False
        if not (1 in [doubles.count(x) for x in list(set(doubles))]):
            return False
        return True

    def get_passwords(self):
        passwords = [n for n in self.range if self.is_password(n)]
        return passwords

    def get_passwords_b(self):
        passwords = [n for n in self.range if self.is_password_b(n)]
        return passwords


x = Passwordfinder(246515, 739105)
print(len(x.get_passwords()))
print(len(x.get_passwords_b()))
