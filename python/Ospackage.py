#OS Package
import os

print(os.getcwd())
lstdir = os.listdir()

for i in lstdir:
    if os.path.isfile(i):
        #print(i)
        pass

#os.mkdir('DemoTest')
#os.makedirs('DemoTest1/DemoTest2')
#os.rmdir('DemoTest')
#os.removedirs('DemoTest/DemoTest2')
#os.chdir('D:\Promied Batches\Python')

#print(os.getcwd())
#print(os.listdir())

