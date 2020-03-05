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

############ TESTING ##############

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
