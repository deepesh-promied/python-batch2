lst = []
with open("../python-batch2/Data/File1.csv",'r') as fp:
    for line in fp:
        lst.append(line.split(',')[2])

d = {}

for i in lst:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1