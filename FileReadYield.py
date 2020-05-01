import memory_profiler as mp

def returnSubjects():
    lst = []
    f = open('./Data/File1.csv','r')
    for i in range(10000):
        f.seek(0)
        for line in f:
            data = line.split(',')
            #yield data[2]
            lst.append(data[2])
    return lst

print(f"Initial Memory Usage: {mp.memory_usage()} MB")

for i in returnSubjects():
    pass

print(f"Final Memory Usage: {mp.memory_usage()} MB")
