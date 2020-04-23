#SeekFunctionDemo
'''
fp.seek(10) #(10,0) 
fp.seek(10,1) #Current Position
fp.seek(-10,2) #From End of File
'''
fp = open('filePractice.txt','rb')

fp.seek(2)
x = fp.read()
print(x)

fp.seek(-5,1)
x = fp.read()
print(x)

fp.seek(-5,2)
x = fp.read()
print(x)

