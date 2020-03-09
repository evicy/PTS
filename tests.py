from functions import get_relation_class
from relations import Relation

print("---Test for get_relation_class---")

M = {5,10,15,20}
rel = get_relation_class(M)
print('rel is: ', rel, ' rel relation = ', rel.relation, ' rel.set = ', rel.set, '\n')


print("---Tests for Relation class---")
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
