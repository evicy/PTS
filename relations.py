from pyrsistent import *

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
            return self

    def remove(self, item):
        if item in self.relation:
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

print('Contains (1,3)? ', r.__contains__((1,3)))
r = r.remove((1,3))
print('r after removing (1,3) ', r.relation)
print('Contains (1,3)? ', r.__contains__((1,3)))

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

print("-------INVERSE---------")
print('p=', p.relation)
print(type(p))
q = p.inverse()
print('q = p.inverse=', q.relation, ' M = ', q.set, '\n')

print("-------COMPOSITION---------")
print('p= ', p.relation)
print('q= ', q.relation)
q = p.composition(q)
print('q = p composed with q', q.relation,  '\n')
print(p.set)

print("-------isReflexive---------")
print('p=', p.relation, ' set> ', p.set, ' isReflexive? ', p.isReflexive())
a = Relation({1,2})
a = a.add((1,1))
a = a.add((2,2))
a = a.add((1,2))
print('a=', a.relation, ' set> ', a.set, ' isReflexive? ', a.isReflexive())
print('empty e=', e.relation, ' set> ', e.set, ' isReflexive? ', e.isReflexive(), '\n')

print("-------isSymmetric---------")
print('p=', p.relation, ' set> ', p.set, ' isSymmetric? ', p.isSymmetric())
print('a=', a.relation, ' set> ', a.set, ' isSymmetric? ', a.isSymmetric())
a=a.add((2,1))
print('a=', a.relation, ' set> ', a.set, ' isSymmetric? ', a.isSymmetric())
print('empty e=', e.relation, ' set> ', e.set, ' isSymmetric? ', e.isSymmetric(), '\n')


print("-------isTransitive---------")
print(p.relation, ' set> ', p.set, ' isTRansitive? ', p.isTransitive())
print('a=', a.relation, ' set> ', a.set, ' isTRansitive? ', a.isTransitive())
a=a.remove((1,1))
print('a=', a.relation, ' set> ', a.set, ' isTRansitive? ', a.isTransitive())
print('empty e=', e.relation, ' set> ', e.set, ' isTRansitive? ', e.isTransitive(), '\n')
