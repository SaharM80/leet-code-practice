#Given two binary strings a and b, return their sum as a binary string.


def addBinary(a: str, b: str) -> str:
    n = max(len(a), len(b)) + 1
    a = a.zfill(n)
    b = b.zfill(n)

    digit = 0
    carry = 0
    sum = 0
    for i in range(n - 1, -1, -1):
        digit = carry + int(a[i]) + int(b[i])
        carry = digit // 2 
        digit = digit % 2
        sum += (10 ** (n - i - 1)) * digit
    
    return str(sum)

print(addBinary('101', '11'))

