def gcd(num1, num2):
    dividend = max(num1, num2)
    divisor  = min(num1, num2)
    remainder = dividend % divisor

    if remainder == 0:
        return divisor
    else:
        dividend = divisor
        divisor = remainder
        return gcd(dividend,divisor)

print(gcd(80, 100))