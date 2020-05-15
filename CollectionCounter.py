from collections import Counter

c =  Counter(['a','a','a','b','b','c','c','c','d','a'])

print(c['a'])
print(c['b'])
x = c.most_common(1)
print(x)

c1 = Counter('abcdccsssccccssss')
print(c1)
print(c1.most_common(2))
print(list(c1.elements()))

for k,v in c1.items():
    print(k,v)

print(len(c1.keys()))

c2 = Counter(a=5,b=7,c=2)
print(c2)

c3 = Counter({'a':1,'b':5.2})
print(c3)
print(c3.most_common(2))
