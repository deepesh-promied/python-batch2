# File Handling
#fp = open('<filename>','<mode>')

fp = open('filepractice.txt','r')
fp1 = open('filepractice1.txt','w')

x = fp.readline()
fp1.write(x)
y =fp.readline()
fp1.write(y)
fp.close()
fp1.close()