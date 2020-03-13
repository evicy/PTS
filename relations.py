from pyrsistent import *
import warnings

def get_relation_class(M):
    class Relation:
        set = pset(M)

        def __init__(self, relation=s()):
            self.relation = pset(relation)

        def __contains__(self, item):
            return item in self.relation

        def add(self, item):
            if (item[0] in self.set) and (item[1] in self.set):
                return Relation(self.relation.add(item))
            warnings.warn("Couldn't add, element is not in the set of the relation")
            return self

        def remove(self, item):
            if item in self.relation:
                return Relation(self.relation.remove(item))
            return self

        def union(self, rel):
            if rel.set.issubset(self.set):
                return Relation(self.relation.union(rel.relation))
            warnings.warn("Couldn't unify, relations are not on the same set")
            return self

        def intersection(self, rel):
            return Relation(self.relation.intersection(rel.relation))

        def substraction(self, rel):
            return Relation(self.relation.difference(rel.relation))

        def inverse(self):
            return Relation(freeze(set(i[::-1] for i in self.relation)))

        def composition(self, rel):
            if not rel.set.issubset(self.set):
                warnings.warn("Couldn't compose, sets of the relations are not compatible!")
                return self
            result = set()
            for a, b in self.relation:
                for c, d in rel.relation:
                    if (b == c): result.add((a, d))
            return Relation(result)

        def isReflexive(self):
            return all((i,i) in self.relation for i in self.set)

        def isSymmetric(self):
            return all((b,a) in self.relation for (a,b) in self.relation)

        def isTransitive(self):
            return all((a,d) in self.relation or b!=c
                       for (a,b) in self.relation for (c,d) in self.relation)


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
            return Relation(closure)

    return Relation
