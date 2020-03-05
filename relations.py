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
            # if (i,i) not in self.relation: return False
            if not self.relation.__contains__((i, i)): return False
        return True

    def isSymmetric(self):
        for a, b in self.relation:
            if not self.relation.__contains__((b, a)): return False
        return True

    def isTransitive(self):
        for a, b in self.relation:
            for c, d in self.relation:
                if (b == c) and not self.relation.__contains__((a, d)): return False
        return True

    def R_F_Closure(self):
        closure = set()
        for i in self.set:
            closure = closure.add((i, i))
            closure = closure.union(self.relation)
        while True:
            new_relations = set((x, w) for x, y in closure for q, w in closure if q == y)
            closure_until_now = closure.union(new_relations)
            if closure_until_now == closure:
                break
            closure = closure_until_now 
        return closure


######################## TESTING ########################

print("---Initializing, contains, add, remove---")

r = Relation({1, 2, 3})
print(r.__contains__(1))
print(r.relation)

r = r.add((1, 2))
r = r.add((2, 3))
r = r.add((1, 3))
print(r.relation)

r = r.add((5, 3))
print('Contains (5,3)? ', r.__contains__((5,3)))
print(r.relation)

r = r.remove((5, 3))
print('r after removing (5,3) ', r.relation)

r = r.remove((1,3))
print('r after removing (1,3) ', r.relation)

p = Relation({2, 3, 4})
p = p.add((2, 3))
p = p.add((3, 4))
print('p: ', p.relation,'\n')


print("-------UNION---------")
print('r=', r.relation)
print('p=', p.relation)
q = r.union(p)
print('q = r U p = ', q.relation, ' M = ', q.set, '\n')

print("----INTERSECTION----")
print('r=', r.relation)
print('p=', p.relation)
q = r.intersection(p)
print('q = r intersect p=', q.relation, ' M = ', q.set)
e = Relation({1,2,3,4,5,6})
q = r.intersection(e)
print('q = r intersect with empty ', q.relation, ' M = ', q.set, '\n')

print("-----SUBSTRACTION-----")
print('r=', r.relation)
print('p=', p.relation)
q = r.substraction(p)
print('q = r U p = ', q.relation, ' M = ', q.set, '\n')
