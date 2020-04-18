#Reading CSV File

fcsv = open('CSVFileDemo.csv','r')
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

print(f"Topper is {studentData[maxp][0]} with {maxv} percentage")

fcsv.close()

