def gcd(a, b):
    if a == 0:
        return b

    return gcd(b % a, a)


def lcm(a, b):
    _gcd = gcd(a, b)
    return (a // _gcd) * b


