#Given an integer x, return true if x is a palindrome, and false otherwise.


def isPalindrome(x: int) -> bool:
        return str(x) == str(x)[::-1] if x >= 0 else False

print(isPalindrome(121))
print(isPalindrome(4))
print(isPalindrome(-121))