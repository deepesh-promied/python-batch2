fp = open('StudentDataMarks.csv','r')
fp1 = open('Percentage.csv','w')

fp.readline()

student_data=[]

Sub1 = open('SUb1'+ '.csv', 'w')
Sub2 = open('SUb2 failed'+ '.csv', 'w')
sub3 = open('sub3 failed'+ '.csv', 'w')
sub4 = open('sub4 failed'+ '.csv', 'w')
sub5 = open('sub5 failed'+ '.csv', 'w')
fp2 = open('More than 2'+ '.csv', 'w')
for line in fp:
    fail_count = 0
    data=line.strip().split(',')
    x = list(map(int,data[5:]))    
    perc = sum(list(map(int,data[5:])))/500*100
    data.append(str(perc))
    #student_data.append(data)
    print(f"The percentage of student {data[0]} is {perc}",file = fp1)

    if x[0]<40:
        Sub1.write(line)
        fail_count+=1
    if x[1]<40:
        Sub2.write(line)
        fail_count+=1
    if x[2]<40:
        sub3.write(line)
        fail_count+=1
    if x[3]<40:
        sub4.write(line)
        fail_count+=1
    if x[4]<40:
        sub5.write(line)
        fail_count+=1
    if fail_count > 1:
        fp2.write(line)
    else:
        print("Pass in all subjects")

print('Total Student failed in subject 1',fail_count)

fp.close()
fp1.close()

'''
when loop runs for first ttime-
data=[Anvi,30,45,56]
when loop runs second time-
data=[saransh,34,56,67]
studentdata=[[anvi,30,45,56],[Saransh,34,45,56]
'''



