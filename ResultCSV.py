#Reading CSV File

fcsv = open('CSVFileDemo.csv','r')
frcsv = open('resultCSV.csv','w')
studentData=[]
for line in fcsv:
    data = line.strip().split(',')
    perc = sum(list(map(int,data[1:])))/150*100
    data.append(perc)
    studentData.append(data)

maxv = studentData[0][-1]
maxp = 0

for i in range(1,len(studentData)):
    if studentData[i][-1] > maxv:
        maxv = studentData[i][-1]
        maxp = i

for i,v in enumerate(studentData):
    if i==maxp:
        frcsv.write(','.join(list(map(str,v))) + ',Topper\n')
    else:    
        frcsv.write(','.join(list(map(str,v)))+'\n')

fcsv.close()
frcsv.close()
#print(f"Topper is {studentData[maxp][0]} with {maxv} percentage")