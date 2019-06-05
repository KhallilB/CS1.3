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
    # TODO: implement linear search recursively here
    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests

    # Base case to stop the recusive call
    # If you go beyond the length of the array
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
    # TODO: implement binary search iteratively here
    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests

    # Leftmost value
    left = 0

    # Rightmost value
    # Needs to be 1 less because array index starts at 0
    right = len(array) - 1

    # left value shouldnt be greater than right value
    while left <= right:
        # Find the middle value
        # Use integer division (discard decimal places)
        mid = (left + right) // 2
        # If mid value is smaller than the item
        if array[mid] < item:
            # Set the new left value 1 off of our mid
            # We discard anything before mid
            left = mid + 1
        elif array[mid] > item:  # If mid value is greater than the item
            # Set the new right value 1 off our mid
            # We discard anything that is after mid
            right = mid - 1
        else:
            # mid becomes the value were looking for
            return mid
    return


def binary_search_recursive(array, item, left=None, right=None):
    # TODO: implement binary search recursively here
    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests
    if left > right:
        return

    mid = (left + right) // 2

    if array[mid] > item:
        return binary_search_recursive(array, item, left, mid - 1)
    elif array[mid] < item:
        return binary_search_recursive(array, item, mid + 1, right)
    else:
        return mid


array = [0, 32, 131, 2, 34, 12]
item = 12

print(binary_search_iterative(array, item))
