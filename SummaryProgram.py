import sys
filep = open('StudentsData.csv','r')

gender = {}
college = {}
cat = {}

for line in filep:
    data = line.strip().split(',',3)
    '''
    [0] -> Name
    [1] -> Category
    [2] -> Gender 
    [3] -> College
    '''
    if data[3] in college:
        college[data[3]] = college[data[3]]+1
    else:
        college[data[3]] = 1
    
    if data[2] in gender:
        gender[data[2]] = gender[data[2]] + 1
    else:
        gender[data[2]] = 1
    
    if data[1] in cat:
        cat[data[1]][0] =   cat[data[1]][0] +  1
        #print(','.join(data),file=cat[data[1]][1])
        cat[data[1]][1].write(','.join(data)+'\n')
    else:
        fp = open('./summary/' + data[1] + '.csv', 'w')
        cat[data[1]] = [1,fp]
        #cat[data[1]][1]
        #print(','.join(data),file=cat[data[1]][1])
        cat[data[1]][1].write(','.join(data)+'\n')

#fp = open('./summary/summary.txt','w')
fp = sys.stdout
for i,v in gender.items():
    print(i,v,file=fp)

print('-'*20,file=fp)

for i,v in cat.items():
    print(i,v[0],file=fp)
    v[1].close()
    
print('-'*20,file=fp)

for i,v in college.items():
    print(i,v,file=fp)

fp.close()

