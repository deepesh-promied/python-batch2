#map Function
#this is the file for map function. We also practiced custom map function which is in the same repository
def doubleF(x):
    return 2*x

def breakName(x):
    return x.split()

def concat(x,y):
    return x + ' ' + y

lst = [20,30,40,50,60,70]

nlist = ['Sarthak Joshi','Divyansh Bhutra','Saransh Sethi','Anvi Jain']
mlist = ['Python','Java','Java','Machine Learning']


#map Function
#x = list(map(doubleF,lst))
#print(x)

#snlist = list(map(breakName,nlist))
#print(snlist)
snlist = list(map(concat,mlist,nlist))
print(snlist)