#Create Dictionary from two lists

lstkey = ['name','age','surname']
lstval = ['Divyansh',17,'Bhutra']

dc={}
for k,v in zip(lstkey,lstval):
    dc[k]=v

print(dc)
del(dc['name'])
print(dc)


