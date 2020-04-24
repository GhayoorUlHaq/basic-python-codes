def gcd(num1, num2):
    dividend = max(num1, num2)
    divisor  = min(num1, num2)
    remainder = dividend % divisor

    while remainder >= 0:
        if remainder == 0:
            return divisor
        else:
            dividend = divisor
            divisor = remainder
            remainder = dividend % divisor

print(gcd(36, 60))