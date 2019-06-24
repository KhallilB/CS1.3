#!python

import string
# Hint: Use these string constants to ignore capitalization and/or punctuation
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase

# Use immutable set for constant lookup time
# Roommates told me about this ^
PUNCTUATION = frozenset(string.punctuation)


def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing."""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str), 'input is not a string: {}'.format(text)

    # return is_palindrome_iterative(text)
    return is_palindrome_recursive(text)


def is_palindrome_iterative(text):
    # TODO: implement the is_palindrome function iteratively here
    # once implemented, change is_palindrome to call is_palindrome_iterative
    # to verify that your iterative implementation passes all tests

    left = 0
    right = len(text)-1

    # start checking from front and back, and meet in the middle
    while left != right and left < right:
        # ignore punctuation and space
        if text[left] in PUNCTUATION or text[left] == ' ':
            left += 1
            continue
        if text[right] in PUNCTUATION or text[right] == ' ':
            right -= 1
            continue

        # check for equality, ignore casing
        if (text[left].lower() != text[right].lower()):
            return False
        left += 1
        right -= 1

    return True


def is_palindrome_recursive(text, left=None, right=None):
    # once implemented, change is_palindrome to call is_palindrome_recursive
    # to verify that your iterative implementation passes all tests

    if left == None and right == None:
        left = 0
        right = len(text)-1

    # We've moved through the text
    if left == right or left > right:
        return True

    # check for punctuation
    if text[left] in PUNCTUATION or text[left] == ' ':
        return is_palindrome_recursive(text, left+1, right)

    if text[right] in PUNCTUATION or text[right] == ' ':
        return is_palindrome_recursive(text, left, right-1)

    # check for base case case
    if text[left].lower() == text[right].lower():
        return is_palindrome_recursive(text, left+1, right-1)

    return False


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()
