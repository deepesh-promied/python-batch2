#reading file and finding frequency. 
def readfile():
    fp=open('./Data//File1.csv','r')
    for line in fp:
        data=line.strip().split(',')
        yield data[2]

subject={}
for i in readfile():
    
    if i in subject:
        subject[i]+=1
    else:
        subject[i]=1

for i,v in subject.items():
    print(i,v)

#Using list    
'''
#Using List
def readfile():
    with open('./Data//File1.csv','r') as fp:
        lst=[]
        for line in fp:
            data=line.strip().split(',')
            for i in range(len(data)):
                lst.append(data[2])
        return lst


x=readfile()
print(x)
'''

#Frequency:

'''
with open('./Data//File1.csv','r') as fp:
    subject={}
    for line in fp:
        data=line.strip().split(',')
        if data[2] in subject:
            subject[data[2]]+=1
        else:
            subject[data[2]]=1

for i,v in subject.items():
    print(i,v)
'''