#Command Line Arguments
import sys #Import package

lst = [98,34,26,58,28,12,1,76,30]

if len(sys.argv)==2:
    nts = int(sys.argv[1])
    pos = -1
    for i in range(len(lst)):
        if nts == lst[i]:
            pos = i 
            break 
    if pos==-1:
        print(f"{nts} not found")
    else:
        print(f"{nts} found at position {pos+1}")

else:
    print("Invalid Input")
