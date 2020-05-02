# Sort Files
import os
extmap = {
    'txt':'text',
    'py' :'python',
    'java' : 'java',
    'csv': 'datafile',
    'other':'others'
}
try:
    for v in extmap.values():
        os.mkdir(v)
except:
    print('Directory Already Exists')

lstdir = os.listdir()

for v in lstdir:
    if(os.path.isfile(v)):
        ext = v.split('.')[-1]
        directory = 'others'
        if ext in extmap.keys():
            directory = extmap[ext]
        fp = open(v,'rb')
        filedata = fp.read()
        fpd = open(directory + '/' + v,'wb')
        fpd.write(filedata)
        fp.close()
        fpd.close()
        #os.remove(v)