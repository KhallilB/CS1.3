#!python


def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # Time:
    # Worst Case: O(n): because it must go through text to find the pattern
    # Best Case: would be O(1) if the pattern is in the beginning
    # Space: O(1) because it will always be simply true or false
    if pattern in text:
        return True
    else:
        return False


def index_helper(text, pattern):
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)

    # Time: O(n): Where n is the amount of letters in the text.
    # Space: 0(1): Creating an array that doesnt grow based on input is constant time

    indices = []
    for index, _ in enumerate(text):
        if pattern == text[index: (index + len(pattern))]:
            indices.append(index)

    return indices


def find_index(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)

    # Time:
    # Worst case: O(n): Where (n) is the amount of indexes in the text.
    # It needs to duplicate the array then go through all of the indices
    # in the array.
    # Best case: O(1): If the item is None or 0
    # Space: 0(1): Only duplicating an array that doesnt grow

    indices = index_helper(text, pattern)  # call the helper function
    if len(indices) is not 0:
        return indices[0]  # return the first index

    return None  # unless there's nothing, in which case, return None


def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)

    # Time: O(n): For the same reasons as above, array duplication
    # Space: O(1): Only duplicating an array that doesnt grows

    return index_helper(text, pattern)  # call the helper function


def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    # TODO: Uncomment these lines after you implement find_index
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    # TODO: Uncomment these lines after you implement find_all_indexes
    indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
    main()
