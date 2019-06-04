#!python

import string


def num_to_letter(num):

    letters = 'abcdefghijklmnopqrstuvwxyz'
    return letters[num - 10]


def letter_to_digit(letter):

    num = ord(letter) - 97 + 10
    return num


def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: result is int -- integer representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)

    result = 0

    for index, digit in enumerate(digits):

        if digit.isdigit():
            digit_to_add = int(digit)

        else:
            digit_to_add = letter_to_digit(digit)
        result += digit_to_add

        if index is not len(digits) - 1:
            result *= base

        else:
            1

    return result


def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    new_base_number = ''

    while number != 0:
        remainder = number % base
        number = number // base

        if (remainder >= 10 and base > 10):
            remainder = num_to_letter(remainder)

        else:
            remainder

        new_base_number += str(remainder)

    new_base_number = new_base_number[::-1]
    return new_base_number


def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)

    if base1 == 10:
        new_base_number = encode(int(digits), base2)

    else:
        decimal_digit = decode(digits, base1)
        new_base_number = encode(decimal_digit, base2)

    return new_base_number


def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        # Convert given digits between bases
        result = convert(digits, base1, base2)
        print('{} in base {} is {} in base {}'.format(
            digits, base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')


if __name__ == '__main__':
    main()
