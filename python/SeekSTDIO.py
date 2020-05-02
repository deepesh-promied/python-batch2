#seek Function for Standard Output
import sys
fp=sys.stdout
fp.write('This is a message using write function\n')
#fp.seek(14)
fp.write('Second Message\n')
print('This is a message using write function')
