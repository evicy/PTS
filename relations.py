from pyrsistent import *

class Relation:
    def __init__(self, M, relation=s()):
        self.set = pset(M)
        self.relation = pset(relation)

    def __contains__(self, item):
        return self.relation.__contains__(item)

    def add(self, item):
        if (self.set.__contains__(item[0])) and (self.set.__contains__(item[1])):
            return Relation(self.set, self.relation.add(item))
        else:
            return self

    def remove(self, item):
        if self.relation.__contains__(item):
            return Relation(self.set, self.relation.remove(item))
        else:
            return self

    def union(self, rel):
        return Relation(self.set.union(rel.set), self.relation.union(rel.relation))

    def intersection(self, rel):
        return Relation(self.set.intersection(rel.set), self.relation.intersection(rel.relation))

    def substraction(self, rel):
        return Relation(self.set, self.relation.difference(rel.relation))
