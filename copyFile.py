#Program to Copy a File
from sys import argv

if len(argv)==3:
    fsrc = open(argv[1],'rb')
    fdest = open(argv[2],'wb')

    fdata = fsrc.read()
    fdest.write(fdata)

    fsrc.close()
    fdest.close()

elif len(argv)==2:
    fsrc = open(argv[1],'rb')
    
    fname = argv[1].split('.')
    fname[0] = fname[0]+'(Copy)'
    fdest = '.'.join(fname)

    fp = open('./copy/' + fdest,'wb')
    fdata = fsrc.read()
    fp.write(fdata)

else:
    print("Invalid Command")


