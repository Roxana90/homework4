from algorithm import gcd as get_gcd
from algorithm import lcm as get_lcm


class Fraction:
    def __init__(self, numerator, denominator):
        if type(numerator) != int:
            raise ValueError('Numerator should be an integer.')

        if type(denominator) != int:
            raise ValueError('Denominator should be an integer.')

        if denominator == 0:
            raise ValueError('Denominator cannot be 0.')

        gcd = get_gcd(abs(numerator), abs(denominator))

        self.numerator = numerator // gcd
        self.denominator = denominator // gcd

    def __add__(self, other):
        lcm = get_lcm(self.denominator, other.denominator)
        self_multiply_by = lcm // self.denominator
        other_multiply_by = lcm // other.denominator

        new_numerator = self.numerator * self_multiply_by + other.numerator * other_multiply_by


        return Fraction(new_numerator, lcm)

    def __sub__(self, other):
        lcm = get_lcm(self.denominator, other.denominator)
        self_multiply_by = lcm // self.denominator
        other_multiply_by = lcm // other.denominator

        new_numerator = self.numerator * self_multiply_by - other.numerator * other_multiply_by

        return Fraction(new_numerator, lcm)


    def inverse(self):
        return Fraction(self.denominator, self.numerator)


    def __str__(self):
        return f'{self.numerator}/{self.denominator}'


fraction_1 = Fraction(6, 12)
fraction_2 = Fraction(3, 4)
fraction_3 = fraction_1 + fraction_2
fraction_4 = fraction_1 - fraction_2
fraction_5 = fraction_1.inverse() #inverse of 'fraction_1'

print(f'1 = {fraction_1}')
print(f'2 = {fraction_2}')
print(f'3 = {fraction_3}')
print(f'4 = {fraction_4}')
print(f'5 = {fraction_5}')
