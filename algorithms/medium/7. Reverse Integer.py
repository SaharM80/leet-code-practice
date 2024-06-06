# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).


def reverse(x: int) -> int:
        upper_limit = 2 ** 31
        lower_limit = -1 * upper_limit

        sign = -1 if x < 0 else 1
        x = abs(x)

        reversed_x = 0
        while x > 0:
            digit = x % 10
            x = int(x / 10)
            reversed_x = reversed_x * 10 + digit

        reversed_x *= sign

        return reversed_x if lower_limit <= reversed_x < upper_limit else 0

print(reverse(123))
print(reverse(-123))
print(reverse(120))