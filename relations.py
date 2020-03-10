from pyrsistent import *
import warnings

class Relation:
    def __init__(self, M, relation=s()):
        self.set = pset(M)
        self.relation = pset(relation)

    def __contains__(self, item):
        return item in self.relation

    def add(self, item):
        if (item[0] in self.set) and (item[1] in self.set):
            return Relation(self.set, self.relation.add(item))
        else:
            warnings.warn("Couldn't add, element is not in the set of the relation")
            return self

    def remove(self, item):
        if item in self.relation:
            return Relation(self.set, self.relation.remove(item))
        else:
            return self

    def union(self, rel):
        if self.set == rel.set:
            return Relation(self.set.union(rel.set), self.relation.union(rel.relation))
        else:
            warnings.warn("Couldn't unify, relations are not on the same set")
            return self

    def intersection(self, rel):
        return Relation(self.set, self.relation.intersection(rel.relation))

    def substraction(self, rel):
        return Relation(self.set, self.relation.difference(rel.relation))

    def inverse(self):
        result = set()
        for a, b in self.relation:
            result.add((b, a))
        return Relation(self.set, result)

    def composition(self, rel):
        result = set()
        for a, b in self.relation:
            for c, d in rel.relation:
                if (b == c): result.add((a, d))
        return Relation(self.set.union(rel.set), result)

    def isReflexive(self):
        for i in self.set:
            if (i,i) not in self.relation: return False
        return True

    def isSymmetric(self):
        for a, b in self.relation:
            if (b,a) not in self.relation: return False
        return True

    def isTransitive(self):
        for a, b in self.relation:
            for c, d in self.relation:
                if (b == c) and ((a,d) not in self.relation): return False
        return True

    def R_F_Closure(self):
        closure = set(self.relation)
        for i in self.set:
            closure.add((i, i))
        while True:
            new_relations = set((x, w) for x, y in closure for q, w in closure if q == y)
            closure_until_now = closure | new_relations

            if closure_until_now == closure:
                break
            closure = closure_until_now
        return Relation(self.set, closure)
