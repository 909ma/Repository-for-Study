def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def reduce_fraction(numerator, denominator):
    gcd_value = gcd(numerator, denominator)
    reduced_numerator = numerator // gcd_value
    reduced_denominator = denominator // gcd_value
    return reduced_numerator, reduced_denominator


numerator, denominator = map(int, input().split(':'))
reduced_numerator, reduced_denominator = reduce_fraction(numerator, denominator)
print(f"{reduced_numerator}:{reduced_denominator}")
