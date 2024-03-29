#!python


def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return linear_search_iterative(array, item)
    return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests

    # O(n): Where (n) is the amount of items. We're looping over (n) items in the list were
    # given

    # Base case for exiting recusive function
    if index >= len(array):
        # The item doesn't exist
        return

    if array[index] == item:
        return index  # found

    # Move on to the next function call with an increased index
    return linear_search_recursive(array, item, index + 1)


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return binary_search_iterative(array, item)
    return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests

    # 0(log n): Where (n) is the amount of items in the list. Taking the list of
    # items and cutting in half k amount of times depending on the length of the list

    left = 0
    right = len(array) - 1

    # left value shouldnt be greater than right value
    while left <= right:
        mid = (left + right) // 2
        if array[mid] < item:
            # If the item is larger than the mid ignore the left
            left = mid + 1
        elif array[mid] > item:
            # If the item is smaller than the mid ignore the right
            right = mid - 1
        else:
            # Mid becomes the item were looking for
            return mid
    return


def binary_search_recursive(array, item, left=None, right=None):
    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests

    # O(log n): same as iterative

    # When calling the function the first time
    if left is None and right is None:
        left = 0
        right = len(array) - 1

    # Base case for exiting recusive function
    if left > right:
        return

    mid = (left + right) // 2

    if array[mid] > item:
        # If the item is smaller than the mid ignore the right
        right = mid - 1
        return binary_search_recursive(array, item, left, right)
    elif array[mid] < item:
        # If the item is larger than the mid ignore the left
        left = mid + 1
        return binary_search_recursive(array, item, left, right)
    else:
        return mid
