import memory_profiler as mp 

def readSub(path):
    lst = []
    with open(path,'r') as fp:
        for line in fp:
            lst.append(line.split(',')[2])
    return lst

print(mp.memory_usage())
d = {}

for i in readSub('../python-batch2/Data/File1.csv'):
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

print(mp.memory_usage())
#print(d)

'''
def readStud(sub):
    with open('../python-batch2/Data/File1.csv','r') as fp:
        for line in fp:
            x = line.split(',')
            if x[2] == sub:
                yield x[0]

print(list(readStud('Chemistry')))
'''