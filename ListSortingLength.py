lst_string = ['Apple','Cat','Ball','Elephant','Drum']
metalist = []
for i in range(len(lst_string)):
    metalist.append([len(lst_string[i]),lst_string[i]])
metalist.sort()
sortList = []
for i in metalist:
    sortList.append(i[1])
print(sortList)

