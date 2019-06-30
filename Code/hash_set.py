from hashtable import HashTable


class HashSet(object):

    def __init__(self, elements=None):
        self.hashset = HashTable()
        self.size = 0

        if elements is not None:
            for element in elements:
                self.add(element)

    def __iter__(self):
        for item in self.all_entries():
            yield item

    def __length__(self):
        return self.size

    def all_entries(self):
        return self.hashset.keys()

    def contains(self, key):
        pass

    def add(self, element):
        pass

    def remove(self, element):
        pass

    def union(self, set):
        pass

    def intersection(self, set):
        pass

    def difference(self, set):
        pass

    def is_subset(self, set):
        pass

    def is_superset(self, set):
        pass
