import math


def intToRoman(num: int) -> str:
    digit_to_roman = {1:'I', 5:'V', 10:'X', 50:'L', 
                    100:'C', 500:'D', 1000:'M'}
    n = int(math.log10(num))+1
    roman_list = []

    for i in range(n - 1, -1, -1):
        digit = int(num % (10 ** (i + 1)) / (10 ** i))
        if digit == 4:
            roman_list.append(digit_to_roman[1 * (10 ** i)])
            roman_list.append(digit_to_roman[5 * (10 ** i)])

        elif digit == 9:
            roman_list.append(digit_to_roman[1 * (10 ** i)])
            roman_list.append(digit_to_roman[1 * (10 ** (i + 1))])
            
        else:
            if int(digit / 5) < 1:
                roman_list.append(digit_to_roman[10 ** i] * digit)
            else:
                roman_list.append(digit_to_roman[5 * (10 ** i)])
                digit -= 5
                roman_list.append(digit_to_roman[10 ** i] * digit)

    
    return ''.join(roman_list)

print(intToRoman(3749))
         
        