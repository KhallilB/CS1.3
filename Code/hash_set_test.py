from hash_set import HashSet
import unittest

# Python 2 and 3 compatibility
if not hasattr(unittest.TestCase, 'assertCountEqual'):
    unittest.TestCase.assertCountEqual = unittest.TestCase.assertItemsEqual


class HashSetTest(unittest.TestCase):

    def test_init(self):
        new_set = HashSet()
        assert new_set.size == 0
        working_set = HashSet(['Working', 'Set'])
        assert working_set.__length__() == 2

    def test_contains(self):
        new_set = HashSet(['This', 'is', 'my', 'set'])
        assert new_set.contains('This') == True
        assert new_set.contains('my') == True
        assert new_set.contains('set') == True
        assert new_set.contains('Willowwww') == False
        assert new_set.contains('your') == False

    def test_add(self):
        new_set = HashSet()
        assert new_set.__length__() == 0
        new_set.add('red')
        new_set.add('brown')
        new_set.add('gray')
        assert new_set.__length__() == 3
        assert new_set.contains('red') == True
        assert new_set.contains('brown') == True
        assert new_set.contains('purple') == False
        new_set.add('orange')
        new_set.add('purple')
        assert new_set.__length__() == 5
        assert new_set.contains('purple') == True

    def test_remove(self):
        new_set = HashSet(['red', 'brown', 'gray'])
        assert new_set.__length__() == 3
        new_set.remove('brown')
        assert new_set.__length__() == 2
        assert new_set.contains('brown') == False
        assert new_set.contains('red') == True
        assert new_set.contains('gray') == True
        new_set.remove('gray')
        assert new_set.__length__() == 1
        assert new_set.contains('red') == True
        assert new_set.contains('gray') == False

    def test_union(self):
        first_set = HashSet(['One', 'Two', 'Three', 'Four'])
        second_set = HashSet(['Red', 'Green', 'Blue'])
        union = first_set.union(second_set)
        assert union.size == 7
        assert union.contains('Two') == True
        assert union.contains('Three') == True
        assert union.contains('Blue') == True
        assert union.contains('Purple') == False
        assert union.contains('Six') == False

    def test_intersection(self):
        first_set = HashSet(['One', 'Two', 'Three', 'Four'])
        second_set = HashSet(['Red', 'Two', 'Three', 'Orange'])
        intersection = first_set.intersection(second_set)
        assert intersection.size == 2
        assert intersection.contains('Two')
        assert intersection.contains('Three')

    def test_difference(self):
        first_set = HashSet(['One', 'Two', 'Three', 'Four'])
        second_set = HashSet(['Red', 'Two', 'Three', 'Orange'])
        difference = first_set.difference(second_set)
        print(difference.size)
        assert difference.contains('One') == True
        assert difference.contains('Two') == False
        assert difference.contains('Three') == False

    def test_is_subset(self):
        first_set = HashSet(
            ['Let', 'Me', 'Reck', 'Orange', 'Pill', 'Good', 'Sir'])
        second_set = HashSet(['Let', 'Me', 'Reck'])
        assert first_set.is_subset(second_set) == False
        assert second_set.is_subset(first_set) == True

    def test_is_superset(self):
        first_set = HashSet(
            ['Let', 'Me', 'Reck', 'Orange', 'Pill', 'Good', 'Sir'])
        second_set = HashSet(['Let', 'Me', 'Reck'])
        assert first_set.is_superset(second_set) == True
        assert second_set.is_superset(first_set) == False
