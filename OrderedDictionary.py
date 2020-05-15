from collections import OrderedDict

d = OrderedDict()
d['x'] = 1
d['y'] = 2
d['z'] = 3

#print(d)

for k,v in d.items():
    print(k,v)

d['x'] = 10

for k,v in d.items():
    print(k,v)

d.pop('x')
d['x'] = 55

for k,v in d.items():
    print(k,v)

lst = d.keys()
print(lst)
