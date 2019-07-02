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
        return self.hashset.contains(key)

    def add(self, key_value):
        self.size += 1
        return self.hashset.set(key_value, key_value)

    def remove(self, key_value):
        self.size -= 1
        return self.hashset.delete(key_value)

    def union(self, sec_set):
        union = sec_set
        for key_value in self:
            union.add(key_value)
        return union

    def intersection(self, sec_set):
        intersection = HashSet()

        if sec_set.size < self.size:
            smaller = sec_set
            larger = self
        else:
            smaller = self
            larger = sec_set
        for key_value in smaller:
            if larger.contains(key_value):
                intersection.add(key_value)
        return intersection

    def difference(self, sec_set):
        difference = self
        intersection = self.intersection(sec_set)

        for item in intersection:
            difference.remove(item)
        return difference

    def is_subset(self, sec_set):
        for key_value in self:
            if key_value not in sec_set:
                return False
        return True

    def is_superset(self, sec_set):
        for key_value in sec_set:
            if key_value not in self:
                return False
        return True
